/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";

export class BellMessage extends Component {

    setup() {
        console.log("Bell systray setup...");

        this.state = useState({
            alerts: [],
            unread: 0,
        });

        // services
        this.action = useService("action");

        // load once when systray widget is mounted
        onMounted(() => {
            this.loadAlerts();
        });
    }

    async loadAlerts() {
        const result = await rpc("/web/dataset/call_kw", {
            model: "x.alert",
            method: "search_read",
            args: [[]],
            kwargs: {
                fields: ["title", "message", "is_read"],
                order: "id desc",
                limit: 5,
            },
        });

        this.state.alerts = result;
        this.state.unread = result.filter(r => !r.is_read).length;

        console.log("Alerts:", result, "Unread:", this.state.unread);
    }

    // click on one notification → mark read + open form view
    async openAlert(id) {
        try {
            // mark as read in DB
            await rpc("/web/dataset/call_kw", {
                model: "x.alert",
                method: "write",
                args: [[id], { is_read: true }],
                kwargs: {},
            });

            // update local state
            const alert = this.state.alerts.find(a => a.id === id);
            if (alert) {
                alert.is_read = true;
            }
            this.state.unread = this.state.alerts.filter(a => !a.is_read).length;

            // open record form
            this.action.doAction({
                type: "ir.actions.act_window",
                res_model: "x.alert",
                res_id: id,
                views: [[false, "form"]],
                target: "current",   // or "new" for popup
            });

            console.log("Opened alert:", id);
        } catch (e) {
            console.error("Failed to open alert:", e);
        }
    }
}

BellMessage.template = "bell_message.BellMessage";

registry.category("systray").add("bell_message", {
    Component: BellMessage,
});
