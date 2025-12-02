/** @odoo-module **/
import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { CheckBox } from "@web/core/checkbox/checkbox";


export class OWLTodoList extends Component {
static template = 'owl_text.Todolist'


    static components = { CheckBox };

    setup() {
        this.state = useState({
            task: { id: "", name: "", color: "#FF0000", completed: false },

            tasklist: [],
            isEdit: false
        })

        this.orm = useService('orm')
        this.model = "todo.list.owl"
        this.searchInput = useRef("search-input")

        /** Asynchronous Operations which get element before render */
        onWillStart(async () => {
            await this.getAllTasks()
        })
    }
     

    /** This ORM method which extract element from Database table 
     [ Note:- Use useService to get ORM methods ] 
     
     */
    async getAllTasks() {
        this.state.tasklist = await this.orm.searchRead(this.model, [], ['name', 'color', 'completed'])

    }

    /** Its Reset form value */
    addtask() {
        this.resetform()
        this.state.activeId = false
        this.state.isEdit = false
    }

    /** Its for edit button */
    edittask(task) {
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = { ...task }
    }
    

    /** Its use for save elements  */
    async savetask() {

        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.task])
        }

        else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)

        }

        await this.getAllTasks()
        console.log('saving task')
    }
    

    /** Its Help for Reset the form view which set value from previous save */

    resetform() {
        this.state.task = { id: "", name: "", color: "#FF0000", completed: false }
    }

    async deletetask(task) {
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()

    }
    

    /** Its use for Search*/
    async searchtask() {
        const text = this.searchInput.el.value
        console.log('searching....', text)

        this.state.tasklist = await this.orm.searchRead(this.model,
            [['name', 'ilike', text]], ["name", "color", "completed"])

    }

    async toggletask(e, task) {
        await this.orm.write(this.model, [task.id], { completed: e.target.checked })
        await this.getAllTasks()
    }

    async updatecolortask(e, task) {
        await this.orm.write(this.model, [task.id], { color: e.target.value })
        await this.getAllTasks()
    }


}


registry.category("actions").add('action_owl_todo_list_js', OWLTodoList)