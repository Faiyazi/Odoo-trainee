/** @odoo-module **/

import { EmailField } from "@web/views/fields/email/email_field";
import { registry } from "@web/core/registry";

// export class EmailValidation extends EmailField {

//     get isValidEmail() {
//         const value = this.value || "";
//         const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         return re.test(value);
//     }

//     // Odoo 19 recommended way: override render()
//     render() {
//         const el = super.render();  // render original email field

//         // Remove previous message if exists
//         const old = el.querySelector(".email-validation-msg");
//         if (old) old.remove();

//         // Add message container
//         const msg = document.createElement("div");
//         msg.className = "email-validation-msg";
//         msg.style.fontSize = "12px";

//         if (this.value) {
//             if (this.isValidEmail) {
//                 msg.style.color = "green";
//                 msg.textContent = "✔ Valid Email";
//             } else {
//                 msg.style.color = "red";
//                 msg.textContent = "✘ Invalid Email Address";
//             }
//         }

//         // Append message AFTER the existing email input field
//         el.appendChild(msg);

//         return el;
//     }

//     // Handle input change in Odoo 19
//     onInput(ev) {
//         const newValue = ev.target.value;

//         // correct Odoo 19 update
//         this.props.record.update({
//             [this.props.name]: newValue,
//         });
//     }
// }

// // Register field widget
// registry.category("fields").add("valid_email", {
//     component: EmailValidation,
//     supportedTypes: ["char"],
// });


class ValidEmailField extends EmailField {
    setup() {
        super.setup()
        console.log('email field is working')
        console.log('props', this.props)
    }

    get isValidEmail() {
    const value = this.props?.record?.data?.[this.props.name];

    console.log("Email value:", value);
    console.log("Field name:", this.props.name);

    let re = /\S+@\S+\.\S+/;
    return re.test(value);
}

}

ValidEmailField.template = "owl.ValidEmailField"
ValidEmailField.supportedTypes = ["char"]

registry.category("fields").add("valid_email", {
    component: ValidEmailField
})