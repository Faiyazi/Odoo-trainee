/** @odoo-module **/

import { CharField } from "@web/views/fields/char/char_field";
import { registry } from "@web/core/registry";


class UsernameField extends CharField {
    setup() {
        super.setup()
        console.log('char field is working')
        console.log('props', this.props)
    }

    get emaildomain() {
        const {email} = this.props.record.data
        return email ? email.split('@')[1] : ''
    }

}

UsernameField.template = "owl.UsernameField"
UsernameField.components = { CharField }
UsernameField.supportedTypes = ["char"]

registry.category("fields").add("username", {
    component: UsernameField
})