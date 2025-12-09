import { registry } from '@web/core/registry';
import { useService,useAutofocus } from "@web/core/utils/hooks";
import { Component, useState, onWillStart, useRef } from '@odoo/owl';

class OwlJs extends Component {
    setup() {
        console.log('OwlJs Component Initialized');

        this.orm = useService('orm');
        this.notification = useService('notification');
        this.effectService = useService('effect');
        this.httpService = useService('http');  

        this.model = 'testing.owl';
        this.searchInputRef = useRef("search-input");

        this.state = useState({
            message: {
                name: "Test",
                description: `This is only for test purpose.`,
                price: 0,
                image: null,
            },
            set_message: [],
            all_message: [],   
            isEdit: false,
            activeId: null,
        });

        this.inputdata = useAutofocus();

        onWillStart(async () => {
            await this.fetchData();
        });
    }

    searchData() {
        const el = this.searchInputRef.el;
        if (!el) {
            return;
        }

        const query = el.value.toLowerCase().trim();
        if (!query) {
            // reset from all_message
            this.state.set_message = this.state.all_message;
            return;
        }

        this.state.set_message = this.state.all_message.filter(record =>
            (record.name || '').toLowerCase().includes(query) ||
            (record.description || '').toLowerCase().includes(query)
        );
        console.log('Searching for:', query);
    }

    addData() {
        this.state.message = { image: null, name: "", description: "", price: "" };
        this.state.isEdit = false;
        this.state.activeId = null;
        console.log('Adding new data');
    }

    async fetchData() {
        try {
            const result = await this.orm.searchRead(
                this.model,
                [],
                ['image', 'name', 'price', 'description']
            );
            this.state.all_message = result;
            this.state.set_message = result;

            console.log('Data fetched from the server:', result);
        } catch (error) {
            console.error('Error fetching data from the server:', error);
        }
    }

    async savetask() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.message]);
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.message);
        }

        await this.fetchData();
        console.log('saving task');
    }

    btnClick(val) {
        this.notification.add(`Thank you for buying ${val.name}`, {
            type: 'info',
            className: 'my_notify',
        });
    }

    btnCartClick(val) {
        console.log('Adding sepia effect');
        this.effectService.add({
            type: "cart",
        });
    }

    btnCart() {
        window.location.href = "/shop/cart";
    }

    reloadPage() {
        location.reload();
    }

    onImageChange(ev) {
        const file = ev.target.files?.[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = () => {
            const result = reader.result;
            if (typeof result === "string") {
                const base64 = result.split(',')[1];
                this.state.message.image = base64;
            }
        };
        reader.readAsDataURL(file);
    }

    async setToForm(record) {
        const data = await this.httpService.get(`/owl_js/get_record/${record.id}`);
        this.state.message = data;
        this.state.isEdit = true;
        this.state.activeId = record.id;
    }

    async postData() {
        console.log('Posting data to the server');
        await this.httpService.post('/owl_js/post_data', {
            data: this.state.message,
        });
    }
}

OwlJs.template = 'owl_js.owl_js_template';

registry.category('actions').add('owl_js', OwlJs);
