/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

export class DemoComponent extends Component {
    static template = "owl_test.DemoComponent";

    setup(){
        this.state = useState({
            items: ["Apple"],
            newItem :""
        });

         this.tyu = useState({
            options: ["Good", "Bad", "Not Good"],
            selected: "Good",   
        });
    }

    addItem() {
        if (this.state.newItem.trim()) {
             this.state.items.push(`${this.state.newItem.trim()} - ${this.tyu.selected}`);
            this.state.newItem = "";
            
    }}

    updateNewItem(ev) {
        this.state.newItem = ev.target.value;
    }

     updateSelection(ev) {
        this.tyu.selected = ev.target.value;
    }


}
registry.category("actions").add("owl_demo_action",DemoComponent);
