/** @odoo-module **/

import { registry} from "@web/core/registry";
const { Component, useState, onWillStart } = owl;
import {useService} from "@web/core/utils/hooks";

export class OwlTodoList extends Component{
    setup() {
        this.state = useState({
            task:{name:"", color:"#FF0000", completed:false},
            taskList:[],
            isEdit:false,
            activeId : false,
        })
        this.orm = useService("orm")
        this.model = "owl.todo.list"

        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "completed"])
    }

    addTask(){

    }

    editTask(){

    }
    
    async saveTask(){
        await this.orm.create(this.model, [this.state.task])

        await this.getAllTasks()
    }
}

OwlTodoList.template = 'owl_todo_app.TodoList'
registry.category('actions').add('owl_todo_app.action_todo_list_js', OwlTodoList);