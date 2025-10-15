import { Component,useState} from "@odoo/owl";
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class ContactForm extends Component{
    static template ="contact_form_view_owl.ContactForm"

    setup(){
        this.orm = useService("orm")

        this.state =useState({
            name : ""
        })
    }

    async setbtn(){

         const x = await this.orm.searchRead(
                "res.partner",[],["name"]
            )
         if (x.length) {
            this.state.name = x[0].name;
            alert(`Partner Name: ${this.state.name}`);
        } else {
            alert("No partner found!");
        }
    }
}
registry.category("view_widgets").add('say_hello',{component:ContactForm})
