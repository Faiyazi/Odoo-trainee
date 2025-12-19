/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { append, setAttributes } from "@web/core/utils/xml";
import { FormCompiler } from "@web/views/form/form_compiler";

const KEY = "chatter_position";

patch(FormCompiler.prototype, {
    compile(node, params) {
        const res = super.compile(node, params);

        if (localStorage.getItem(KEY) !== "bottom") {
            return res;
        }

        const chatter = res.querySelector(
            ".o_form_renderer > .o-mail-Form-chatter"
        );
        const sheet = res.querySelector(".o_form_sheet_bg");

        if (!chatter || !sheet) return res;

        const clone = chatter.cloneNode(true);
        clone.classList.add("o-isInFormSheetBg");
        append(sheet, clone);
        setAttributes(chatter, { "t-if": "false" });

        return res;
    },
});
