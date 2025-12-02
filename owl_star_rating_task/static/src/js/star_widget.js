/** @odoo-module */

import { registry } from "@web/core/registry";
import { useState } from "@odoo/owl";
import { Field } from "@web/views/fields/field";
import { rpc } from "@web/core/network/rpc";


export class StarRating extends Field {
    static template = "owl_star_rating_task.StarRating"
    setup() {
        super.setup(...arguments);
        console.log("PROPS: ", this.props)
        console.log("RECORD: ", this.props.record)
        console.log("RES_MODEL: ", this.props.record.resModel)
        console.log("RES_ID: ", this.props.record.resId)

        const initialRating = this.props.record.data[this.props.name] || 0;
        this.state = useState({ rating: initialRating });
    }

    get stars() {
        return [1, 2, 3, 4, 5];
    }

    onStarClick = async(star) => {
        this.state.rating = star;

        try{
            await rpc("/web/dataset/call_kw",{
                model: this.props.record.resModel,
                method: 'write',
                args: [[this.props.record.resId], { record_rating: star }],
                kwargs:{}
            });

            this.props.record.data[this.props.name] = star;
        } catch(error){
            console.error("Error saving star rating:", error);
        }
    };
}


export const starRating = {
    supportedTypes: ["integer"],
    component: StarRating,
}

registry.category("fields").add("star_rating", starRating);