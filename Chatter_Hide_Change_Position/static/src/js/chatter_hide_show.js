/** @odoo-module **/

import { registry } from "@web/core/registry";

function getChatter() {
    return document.querySelector(".o-mail-Form-chatter"); 
}

function hideChatterSafe(chatter) {
    chatter.style.transform = "translateX(-5000px)";
    chatter.style.position = "absolute";
}

function showChatterSafe(chatter) {
    chatter.style.transform = "";
    chatter.style.position = "";
}

function showShowButton() {
    const btn = document.querySelector("#my_show_chatter_btn");
    if (btn) btn.classList.remove("d-none");
}

function hideShowButton() {
    const btn = document.querySelector("#my_show_chatter_btn");
    if (btn) btn.classList.add("d-none");
}

registry.category("services").add("toggle_chatter_service", {
    start() {

        document.addEventListener("click", (ev) => {

            const chatter = getChatter();
            if (!chatter) return;

            if (ev.target.closest("#hide_chatter_btn")) {
                hideChatterSafe(chatter);
                showShowButton();
                return;
            }

            if (ev.target.closest("#my_show_chatter_btn")) {
                showChatterSafe(chatter);
                hideShowButton();
                return;
            }

        });

    }
});
