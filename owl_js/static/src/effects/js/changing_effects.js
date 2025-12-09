/** @odoo-module **/

import { Component } from "@odoo/owl";
import { rainbowMan } from "@web/core/effects/rainbow_man";

export class TestingRPC extends Component {

    async RPCBtn() {
        // ✅ 1. Call Python using RPC
        const result = await this.env.services.rpc({
            model: "testing.owl",
            method: "onclickbtn",
            args: [],   // always safer to include args
        });

        // ✅ 2. Trigger Rainbow Effect after success
        rainbowMan(this.env, {
            message: result || "Operation Successful!",
        });
    }
}
