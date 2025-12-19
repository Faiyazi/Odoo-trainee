/** @odoo-module **/

import { registry } from "@web/core/registry";

let lastState = null;
let scheduled = false;


function getForm() {
    return document.querySelector(".o_form_view");
}

function getChatter() {
    return document.querySelector(".o-mail-Form-chatter");
}

function isChatterHiddenOrBottom() {
    const chatter = getChatter();
    if (!chatter) return true;

    if (chatter.classList.contains("o_chatter_hidden")) {
        return true;
    }

    const style = window.getComputedStyle(chatter);
    if (style.display === "none" || style.visibility === "hidden") {
        return true;
    }

    const sheet = chatter.closest(".o_form_sheet_bg");
    if (sheet) {
        return true;
    }

    const renderer = chatter.closest(".o_form_renderer");
    if (!renderer) {
        return true;
    }

    return false;
}

function applyFullWidthSafe() {
    const form = getForm();
    if (!form) return;

    const shouldBeFull = isChatterHiddenOrBottom();

    if (lastState === shouldBeFull) return;
    lastState = shouldBeFull;

    document.body.classList.toggle("o-form-full-width", shouldBeFull);
}


function scheduleApply() {
    if (scheduled) return;
    scheduled = true;

    requestAnimationFrame(() => {
        scheduled = false;
        applyFullWidthSafe();
    });
}


function watchChatterAndForm() {
    const observer = new MutationObserver(() => {
        scheduleApply();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ["class"],
    });

    applyFullWidthSafe();
}


registry.category("services").add("full_form_view_service", {
    start() {
        watchChatterAndForm();
    },
});
