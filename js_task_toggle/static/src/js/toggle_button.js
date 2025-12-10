/** @odoo-module **/

import { Field } from "@web/views/fields/field";
import { registry } from "@web/core/registry";
import { useState } from "@odoo/owl";

class ToggleButtonRES extends Field {
    setup() {
        super.setup();
        console.log("Toggle Loaded");

        this.state = useState({
            value: this.props.value,
        });
    }

    toggle() {
        const newValue = !this.state.value;
        this.state.value = newValue;

        this.props.record.update({
            [this.props.name]: newValue,
        });

        this.props.record.save()
    }
}

ToggleButtonRES.template = "js_task_toggle.ToggleButtonRES";
ToggleButtonRES.supportedTypes = ["boolean"];

registry.category("fields").add("toggle_res", {
    component: ToggleButtonRES,
});
