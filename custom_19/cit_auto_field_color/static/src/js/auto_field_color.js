/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class AutoFieldColor extends Component {
        /**
        * AutoFieldColor
        * ------------------------------------------------------------------------
        * A reusable widget for dynamically coloring Odoo field values.
        * Supports both value-based and XML option–based color customization.
        */
    static template = "auto_field_color.AutoFieldColor";

    static props = {
        ...standardFieldProps, color: { type: String, optional: true },
    };

    get fieldStyle() {
        const value = this.props.record.data[this.props.name];
        return value > 0 ? "grey-field" : "default-field";
    }

    get inlineStyle() {
        /**
        * Returns inline background style based on the 'color' option
        * passed from XML. Example: options="{'color': 'green'}".
        */
        const bgColor = this.props.color;
        return `background-color: ${bgColor};`;
    }

    get formattedValue() {
        /**
        * Formats the field value for display.
        * - Numeric values are shown with two decimal places.
        * - Other values are shown as-is or as an empty string.
        */
        const value = this.props.record.data[this.props.name];
        if (typeof value === "number") {
            return value.toFixed(2);
        }
        return value || "";
    }
}

registry.category("fields").add("auto_field_color", {
    component: AutoFieldColor,
    extractProps({ options }) {
        return { color: options?.color };
    },
});
