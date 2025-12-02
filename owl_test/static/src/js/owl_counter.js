import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class HomeDemo extends Component{
    static template = 'owl_text.HomeDemo'

    setup(){
        this.state = useState({
            item : 0,           
        })
    }
    
    increaseItem(){    
        this.state.item += 1;
    }

    decrementItem(){
        this.state.item -= 1;
    }

}

registry.category("actions").add("test_owl",HomeDemo);
