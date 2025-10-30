/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

export class AutoFieldColor extends Component {
    static template = "auto_field_color.AutoFieldColor";

    // only essential props
    static props = {
        record: Object,
        name: String,
        color: { type: String, optional: true },
    };

    // dynamic class
    get fieldStyle() {
        const value = this.props.record.data[this.props.name];
        return value > 0 ? "grey-field" : "default-field";
    }

    // inline color (from XML)
    get inlineStyle() {
        const bgColor = this.props.color;
        return `background-color: ${bgColor};`;
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

// Register widget
registry.category("fields").add("auto_field_color", {
    component: AutoFieldColor,
    extractProps({ options }) {
        return { color: options?.color };
    },
});
