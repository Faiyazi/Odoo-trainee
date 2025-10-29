/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

export class AutoFieldColor extends Component {
    static template = "auto_field_color.AutoFieldColor";
    static props = { ...standardFieldProps };

    setup() {
        super.setup();
    }

    get fieldStyle() {
        const value = this.props.record.data[this.props.name];
        if (value > 0) {
             return "background-color: #008000; color: white;";
        }else{
            return "background-color: #d3d3d3; color: black;";

        }
        return "";
    }

    // always show two decimal places
    get formattedValue() {
        const value = this.props.record.data[this.props.name];
        if (typeof value === "number") {
            return value.toFixed(2);
        }
    return value || "";
    }
}

registry.category("fields").add("auto_field_color", {
    component: AutoFieldColor,
});
