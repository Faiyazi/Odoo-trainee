import { Component, xml ,useState} from "@odoo/owl";
import { registry } from "@web/core/registry";

export class TestApp extends Component{
    // static template = xml`<h1>hello World</h1>`;
    static template = "test_owl.TestApp";
    setup(){
        this.state = useState({
            price : '5100',
            setprice : ''
        })
    }

    settotal(){
        this.total = this.state.price 
    }
}

registry.category("actions").add("owl_demo_action1",TestApp);

