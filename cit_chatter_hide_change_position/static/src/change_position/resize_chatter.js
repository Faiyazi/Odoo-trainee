/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { browser } from "@web/core/browser/browser";
import { Chatter } from "@mail/chatter/web_portal/chatter";

const STORAGE_KEY = "cit_chatter_hide_change_position.width";
const MIN_WIDTH = 250;

patch(Chatter.prototype, {
    setup() {
        super.setup();

        const saved = browser.localStorage.getItem(STORAGE_KEY);
        if (saved) {
            queueMicrotask(() => {
                const aside = this.el?.closest(".o-mail-Form-chatter.o-aside");
                if (aside) {
                    aside.style.width = `${saved}px`;
                }
            });
        }
    },

    onStartChatterResize(ev) {
        if (ev.button !== 0) return;

        if (
            ev.target.closest(
                "input, textarea, button, select, a"
            )
        ) {
            return;
        }

        ev.preventDefault();
        ev.stopPropagation();

        const aside = ev.currentTarget.closest(
            ".o-mail-Form-chatter.o-aside"
        );
        if (!aside) return;

        const startX = ev.pageX;
        const startWidth = aside.offsetWidth;

        const previousUserSelect = document.body.style.userSelect;
        document.body.style.userSelect = "none";

        const resize = (e) => {
            e.preventDefault();
            e.stopPropagation();

            const delta = startX - e.pageX;
            const newWidth = Math.max(MIN_WIDTH, startWidth + delta);

            aside.style.width = `${newWidth}px`;
            browser.localStorage.setItem(STORAGE_KEY, newWidth);
        };

        const stop = (e) => {
            e?.preventDefault();
            e?.stopPropagation();

            document.removeEventListener("mousemove", resize, true);
            document.removeEventListener("mouseup", stop, true);

            document.body.style.userSelect = previousUserSelect;
        };

        document.addEventListener("mousemove", resize, true);
        document.addEventListener("mouseup", stop, true);
    },

    onDoubleClickChatterResize(ev) {
        ev.preventDefault();
        ev.stopPropagation();

        const aside = ev.currentTarget.closest(
            ".o-mail-Form-chatter.o-aside"
        );
        if (!aside) return;

        aside.style.width = "";
        browser.localStorage.removeItem(STORAGE_KEY);
    },
});
