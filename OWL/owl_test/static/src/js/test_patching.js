/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

patch(FormController.prototype, "custom_form_save_logger", {
    async saveButtonClicked() {
        console.log("📝 Form is being saved...");
        await this._super(...arguments);
        console.log("✅ Form saved successfully!");
    },
});
