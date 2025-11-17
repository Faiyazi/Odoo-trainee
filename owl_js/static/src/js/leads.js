/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class CrmLeads extends Component{
    static template = "owl_js.CrmLeads"

    setup(){
        this.orm = useService("orm")
        this.action = useService("action")
        this.state = useState({leads : []})

        onWillStart(async () => {
            this.state.leads = await this.orm.searchRead(
                "crm.lead",
                [],
                ["name", "partner_id", "expected_revenue"]
            )
        })
    }

    async createLead(){
        this.action.doAction({
            type:"ir.actions.act_window",
            res_model:"crm.lead",
            views:[[false,"form"]],
            target:"current",
        })
    }

    async editLead(id){
        this.action.doAction({
            type:"ir.actions.act_window",
            res_model:"crm.lead",
            res_id:id,
            views:[[false,"form"]],
            target:"current",
        })
    }

    async deleteLead(id){
        if (confirm("Are you sure you want to delete this lead?")){
            await this.orm.unlink("crm.lead", [id])
            this.state.leads = await this.orm.searchRead(
            "crm.lead",
            [],
            ["name", "partner_id", "expected_revenue"]
        )
        }
    }


}

registry.category("actions").add("owl_js.action_leads", CrmLeads)