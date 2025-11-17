from odoo import models, api

class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.onchange("account_type")
    def _onchange_account_type(self):

        group_mapping = {
            'asset': '200001',
            'liability': '100001',
            'income': '400001',
            'expense': '500001',
        }

        if self.account_type:
            main_group = self.account_type.split('_')[0]

            default_code = group_mapping.get(main_group)
            if not default_code:
                return

            prefix = default_code[0]

            last_account = self.search([
                ('account_type', 'like', main_group + '%'),
                ('code', 'like', prefix + '%'),
            ], order="code desc", limit=1)

            if last_account and last_account.code.isdigit():
                next_code = str(int(last_account.code) + 1).zfill(6)
            else:
                next_code = default_code

            self.code = next_code
