/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class StarRating extends Component {
    static template = "star_rating_task.StarRating";

    static props = {
        id: { type: [Number, String], optional: true },
        record: Object,
        name: String,
        readonly: { type: Boolean, optional: true },
    };

    setup() {
        console.log(" Star Rating Widget Loaded");

        this.state = useState({
            stars: [1, 2, 3, 4, 5],
        });

        this.hover = useState({ value: 0 });

        this.setRating = this.setRating.bind(this);
    }

    get value() {
        return this.props?.record?.data?.[this.props.name] || 0;
    }

    async setRating(ev) {
        const rating = ev.currentTarget.dataset.value;

        if (!this.props?.record || this.props.readonly) return;

        console.log("Rating set to:", rating);

        await this.props.record.update({
            [this.props.name]: Number(rating),
        });
    }
}

registry.category("fields").add("star_rating", {
    component: StarRating,
    supportedTypes: ["integer", "float"],
});
