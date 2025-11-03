import { Component, onWillStart,useRef} from "@odoo/owl";
import {useService} from '@web/core/utils/hooks';


export class Child extends Component {
    static template = 'child_view.Child'
    static props = {
        title: { type: String },
        list: { type: Array },
        slots: { type: Object },
        counter: {type: Number},
    }

    setup(){
        // this.myService = useService("my-service");
        this.myInputRef = useRef("my-input");
        onWillStart(() => {console.log('Child Started')})
    }

    focusInput(){
        this.myInputRef.el.focus()
    }
    
}
