/** @odoo-module **/
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

/* ---------------- HelloWorld Component ---------------- */
export class HelloWorld extends Component {
    static template = "owl_demo.HelloWorldTemplate";
}

/* ---------------- Counter Component ---------------- */
import { useState } from "@odoo/owl";

export class Counter extends Component {
    setup() {
        this.state = useState({ count: 0 });
    }
    increment() { this.state.count++; }
    decrement() { this.state.count--; }
}

Counter.template = "owl_demo.CounterTemplate";

// Register both components
registry.category("actions").add("owl_demo.hello_world_action", HelloWorld);
registry.category("actions").add("owl_demo.counter_action", Counter);
