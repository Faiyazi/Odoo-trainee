/** @odoo-module **/

import { registry } from "@web/core/registry";

function getChatter() {
    return document.querySelector(".o-mail-Form-chatter");
}

function getForm() {
    return document.querySelector(".o_form_view");
}

function moveChatterBottom(chatter, form) {
    const sheet = form.querySelector(".o_form_sheet_bg");
    if (!sheet) return;

    chatter.classList.add("chatter-bottom");
    chatter.classList.remove("o-aside-chatter");

    chatter.style.height = "380px";
    chatter.style.width = "100%";
    chatter.style.maxWidth = "";
    chatter.style.overflowY = "auto";

    sheet.appendChild(chatter);
}

function moveChatterRight(chatter, form) {
    const renderer = form.querySelector(".o_form_renderer");
    if (!renderer) return;

    chatter.classList.remove("chatter-bottom");
    chatter.classList.add("o-aside-chatter");

    chatter.style.height = "";
    chatter.style.width = "";
    chatter.style.maxWidth = "";
    chatter.style.overflowY = "";

    renderer.appendChild(chatter);
}

function updateButtonState(isBottom) {
    const btn = document.querySelector("#toggle_chatter_position_btn");
    if (!btn) return;

    btn.textContent = isBottom ? "Right" : "Bottom";
}

registry.category("services").add("toggle_chatter_position_service", {
    start() {

        let isBottom = false;  // save position state in memory

        document.addEventListener("click", (ev) => {

            const btn = ev.target.closest("#toggle_chatter_position_btn");
            if (!btn) return;

            const chatter = getChatter();
            const form = getForm();
            if (!chatter || !form) return;

            if (!isBottom) {
                moveChatterBottom(chatter, form);
                isBottom = true;
            } else {
                moveChatterRight(chatter, form);
                isBottom = false;
            }

            updateButtonState(isBottom);

        });

    }
});
