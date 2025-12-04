import { Component } from "@odoo/owl";

export class ChildComponent extends Component {
    notifyParent() {
        this.trigger('child-clicked', { message : 'Hello from Child!' });
}
}
ChildComponent.template = "my_module.ChildComponent";