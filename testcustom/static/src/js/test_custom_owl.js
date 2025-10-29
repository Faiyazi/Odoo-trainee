/** @odoo-module **/

import { Component, mount, useState } from "@odoo/owl";

class DemoComponent extends Component {
    static template = "my_module.DemoComponent";

    setup() {
        // Reactive state
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

// Auto-mount on page load (for testing)
document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("owl-demo");
    if (container) {
        mount(DemoComponent, { target: container });
    }
});
