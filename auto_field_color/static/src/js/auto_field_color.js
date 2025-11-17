/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class AutoFieldColor extends Component {
    static template = "auto_field_color.AutoFieldColor";
    static props = { ...standardFieldProps, color: { type: String, optional: true } };

    setup() {
        this.state = useState({});
    }

    get fieldStyle() {
        const value = this.props.record.data[this.props.name];
        return value > 0 ? "grey-field" : "default-field";
    }

    get inlineStyle() {
        const bgColor = this.props.color;
        return `background-color: ${bgColor};`;
    }

    get formattedValue() {
        const val = this.props.record.data[this.props.name];
        if (typeof val === "number") return val.toFixed(2);
        return val || "";
    }
}

registry.category("fields").add("auto_field_color", {
    component: AutoFieldColor,
    extractProps({ options }) {
        return { color: options?.color };
    },
});




///** @odoo-module **/
//
//import { registry } from "@web/core/registry";
//import { Component } from "@odoo/owl";
//import { standardFieldProps } from "@web/views/fields/standard_field_props";
//
//export class AutoFieldColor extends Component {
//    static template = "auto_field_color.AutoFieldColor";
//    static props = {
//        ...standardFieldProps,
//        color: { type: String, optional: true }, // color from XML option
//    };
//
//    // CSS class based on field value
//    get fieldStyle() {
//        const value = this.props.record.data[this.props.name];
//        return value > 0 ? "grey-field" : "default-field";
//    }
//
//    // Inline background color from option or default
//    get inlineStyle() {
//        const bgColor = this.props.color || "#6c757d"; // default grey
//        return `background-color: ${bgColor};`;
//    }
//
//    // Display formatted value
//    get formattedValue() {
//        const val = this.props.record.data[this.props.name];
//        if (typeof val === "number") return val.toFixed(2);
//        return val || "";
//    }
//}
//
//// Register widget
//registry.category("fields").add("auto_field_color", {
//    component: AutoFieldColor,
//    extractProps({ options }) {
//        return { color: options?.color };
//    },
//});
//
