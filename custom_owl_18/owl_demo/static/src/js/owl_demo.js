/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class OwlDemo extends Component {
    setup() {
        this.state = useState({ count: 0 });
    }

    increment() {
        this.state.count++;
    }

    decrement() {
        this.state.count--;
    }
}

OwlDemo.template = "owl_demo.OwlDemoTemplate";

registry.category("actions").add("owl_demo_action", OwlDemo);
