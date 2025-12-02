import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

import { registry } from "@web/core/registry";

export class ThemeChange extends Component {
    static template = "ThemeChange.theme_change_template_owl"


    setup() {
        this.state = useState({
            menubar: { color: "#FF0000" },
            tasklist: [],
            isEdit: false
        })

        this.orm = useService('orm')
        this.model = "theme.change"


    }

    async getAllTasks() {
        this.state.tasklist = await this.orm.searchRead(this.model, [], ['menubar'])


    }
}



registry.category("actions").add("theme_change", ThemeChange);


