import { Component } from "@odoo/owl";
import { ChildComponent} from "./childcomponent";

export class Parentcomponent extends Component {
    setup() {
        this.state = useState({ message : "No message yet" });
    }

    handleChildClick(ev) {
        this.state.message = ev.details.message;
    }
}

Parentcomponent.template = "my_module.ParentComponent";
Parentcomponent.component = { ChildComponent };