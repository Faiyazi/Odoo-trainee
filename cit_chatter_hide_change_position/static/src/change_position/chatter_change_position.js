/** @odoo-module **/

import { registry } from "@web/core/registry";

const KEY = "chatter_position";
const FORCE_WIDTH = 1400;

let activeForm = null;
let resizeObserver = null;


function getForm() {
    return document.querySelector(".o_form_view");
}

function getChatter() {
    return document.querySelector(".o-mail-Form-chatter");
}

function getButton() {
    return document.querySelector("#toggle_chatter_position_btn");
}


function applyPosition(pos) {
    const form = getForm();
    const chatter = getChatter();
    if (!form || !chatter) return;

    if (pos === "bottom") {
        document.body.classList.add("o-chatter-bottom");

        const sheet = form.querySelector(".o_form_sheet_bg");
        if (sheet && chatter.parentElement !== sheet) {
            sheet.appendChild(chatter);
        }

        chatter.style.width = "100%";
        chatter.style.maxWidth = "100%";
        chatter.style.minWidth = "100%";
        chatter.style.flex = "0 0 100%";
        chatter.style.position = "static";
        chatter.style.marginTop = "12px";
    } else {
        document.body.classList.remove("o-chatter-bottom");

        const renderer = form.querySelector(".o_form_renderer");
        if (renderer && chatter.parentElement !== renderer) {
            renderer.appendChild(chatter);
        }

        chatter.style.width = "";
        chatter.style.maxWidth = "";
        chatter.style.minWidth = "";
        chatter.style.flex = "";
        chatter.style.position = "";
        chatter.style.marginTop = "";
    }
}

function updateButtonLabel() {
    const btn = getButton();
    if (!btn) return;

    const pos = localStorage.getItem(KEY) || "right";
    btn.textContent = pos === "bottom" ? "Right" : "Bottom";
}

function enforceWidthRule() {
    const form = getForm();
    const btn = getButton();
    if (!form || !btn) return;

    const width = form.offsetWidth;
    let pos = localStorage.getItem(KEY) || "right";

    if (width <= FORCE_WIDTH) {
        pos = "bottom";
        localStorage.setItem(KEY, "bottom");
        btn.classList.add("d-none");
    } else {
        btn.classList.remove("d-none");
    }

    applyPosition(pos);
    updateButtonLabel();
}

function initForForm() {
    const form = getForm();
    const btn = getButton();

    if (!form || form === activeForm || !btn) return;

    activeForm = form;

    if (!localStorage.getItem(KEY)) {
        localStorage.setItem(KEY, "right");
    }

    enforceWidthRule();

    if (resizeObserver) {
        resizeObserver.disconnect();
    }

    resizeObserver = new ResizeObserver(enforceWidthRule);
    resizeObserver.observe(form);

    btn.onclick = () => {
        const current = localStorage.getItem(KEY) || "right";
        const next = current === "right" ? "bottom" : "right";

        localStorage.setItem(KEY, next);
        applyPosition(next);
        updateButtonLabel();

    };

}


function watchForms() {
    const observer = new MutationObserver(() => {
        initForForm();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true,
    });
}


registry.category("services").add("toggle_chatter_position_service", {
    start() {
        watchForms();
        initForForm();
    },
});
