/** @odoo-module **/

import {registry} from '@web/core/registry';
const { Component , useState, onWillStart } = owl;
import { useService } from '@web/core/utils/hooks';

    export class OwlTodoList extends Component {
      setup() {
        this.state = useState({
            task: { name: "", color: "#ff0000", completed: false },
            taskList: [],
            isEdit: false,
            activeId: false,
        });
        this.orm =useService("orm")
        this.model = "owl.todolist"

        onWillStart(async ()=>{
            await this.getAllTasks()
        });
    }
        async getAllTasks(){
              this.state.taskList = await this.orm.searchRead(this.model,[],["name","color","completed"])
        }

        addTask(){

        }

        editTask(){

        }

        async saveTask(){
               console.log(this.state.task)
        }
}
OwlTodoList.template = 'owl.TodoList'
registry.category('actions').add('owl.action_todo_list_js',OwlTodoList);

