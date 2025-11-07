/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class AutoFieldColor extends Component {
       /**
        * AutoFieldColor
        * ------------------------------------------------------------------------
        * A reusable widget that dynamically applies color to field values.

        * Features:
        * - Compatible with standard Odoo field types:
        *   ('char', 'text', 'integer', 'float', 'date', 'datetime',
        *   'monetary', 'boolean', 'many2one', 'selection'. etc.).
        * - Applies a default grey background color if no `color` option is provided.
        * - Supports custom colors via XML field options (`color`).*/

    static template = "cit_auto_field_color.AutoFieldColor";

    static props = {
        ...standardFieldProps,
        color: { type: String, optional: true },
    };

    setup() {
        const { name, color } = this.props;
        const fieldInfo = this.props.field || this.props.record?.fields?.[name];

        const baseWidget = fieldInfo?.widget || fieldInfo?.type || null;
        const base = baseWidget ? registry.category("fields").get(baseWidget) : null;
        this.BaseField = base?.component || null;
    }

    get fieldColor() {
        return this.props.color || "grey";
    }

    get baseFieldProps() {
        const { color, field, ...cleanProps } = this.props;
        return {
            ...cleanProps,
            readonly: this.props.readonly,
            record: this.props.record,
            name: this.props.name,
        };
    }
}

registry.category("fields").add("auto_field_color", {
    component: AutoFieldColor,
    supportedTypes: [
        "char", "text", "integer", "float", "date", "datetime",
        "monetary", "boolean", "many2one", "selection",
    ],
    extractProps({ options }) {
        return { color: options?.color };
    },
});