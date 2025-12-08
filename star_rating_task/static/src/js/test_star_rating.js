import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

/* -----------------------------
   RPC TEST COMPONENT
-------------------------------- */
export class TestContactForm extends Component {

    static props = {};   // ✅ avoids OWL warning

    async setup() {
        console.log("✅ TestContactForm loaded...");

        try {
            const result = await rpc("/web/dataset/call_kw", {
                model: "res.partner",
                method: "name_search",   // safest built-in test
                args: [""],
                kwargs: { limit: 1 },
            });

            console.log("✅ RPC Running Successfully:", result);

        } catch (error) {
            console.error("❌ RPC Failed:", error);
        }
    }
}

/* -----------------------------
   REGISTER COMPONENT AS ACTION
-------------------------------- */
registry.category("actions").add("rpc_test", TestContactForm);

/* -----------------------------
   DIRECT AUTO-RUN RPC TEST
   (Runs even without opening action)
-------------------------------- */
(async () => {
    try {
        const result = await rpc("/web/dataset/call_kw", {
            model: "res.partner",
            method: "name_search",
            args: [""],
            kwargs: { limit: 1 },
        });

        console.log("✅ RPC DIRECT AUTO TEST:", result);

    } catch (e) {
        console.error("❌ RPC DIRECT AUTO TEST FAILED:", e);
    }
})();
