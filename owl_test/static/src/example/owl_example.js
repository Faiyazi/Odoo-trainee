import { Child } from "../child/child";
import { Component,useState} from "@odoo/owl";
import {registry} from '@web/core/registry'


export class Example extends Component{
    static template = 'owl_test.Example';
    static components = { Child }; 

    setup(){
        this.state = useState({
            counter : 0
        })
    }
    increment(){
        this.state.counter += 1;
    }

    decrement(){
        this.state.counter -= 1;
    }
}

registry.category("view_widgets").add('example',{component:Example})