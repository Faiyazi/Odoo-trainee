/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";


class DemoComponent extends Component {
    static template = "owl_demo.DemoComponent";

    setup() {
        this.state = useState({
            items: ["Apple", "Banana", "Orange"],
            newItem: ""
        });
    }

    addItem() {
        if (this.state.newItem.trim()) {
            this.state.items.push(this.state.newItem.trim());
            this.state.newItem = "";
        }
    }

    updateNewItem(ev) {
        this.state.newItem = ev.target.value;
    }
}

// ✅ Register this component as a client action
registry.category("actions").add("owl_demo_action", DemoComponent);
