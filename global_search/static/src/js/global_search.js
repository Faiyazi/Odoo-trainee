/** @odoo-module **/
import { Component, useState, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";

export class GlobalSearch extends Component {
    setup() {
        this.action = useService("action");
        this.state = useState({
            open: false,
            query: "",
            loading: false,
            result: [],
        });
        this.inputRef = useRef("input");
    }

    togglePanel = () => {
        if (this.state.open) {
            this.state.open = false;
        } else {
            this.state.open = true;
            this.state.query = "";
            this.state.result = [];
            setTimeout(() => this.inputRef.el?.focus(), 50);
        }
    };

    onInput = (ev) => {
        this.state.query = ev.target.value;
    };

    search = async () => {
        if (!this.state.query || !this.state.query.trim()) return;
        this.state.loading = true;
        try {
            const res = await rpc("/global_search/search", { query: this.state.query });
            this.state.result = res.result || [];
        } catch (e) {
            console.error("Search Error", e);
        } finally {
            this.state.loading = false;
        }
    };

    onResultClick = async (ev) => {
        const { model, id } = ev.currentTarget.dataset;
        this.state.open = false;
        await this.action.doAction({
            type: "ir.actions.act_window",
            res_model: model,
            res_id: parseInt(id),
            views: [[false, "form"]],
            target: "current",
        });
    };
}

GlobalSearch.template = "global_search.GlobalSearch";
registry.category("systray").add("global_search.GlobalSearch", { Component: GlobalSearch, sequence: 10 });