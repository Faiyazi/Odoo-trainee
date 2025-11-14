from odoo import models, api


class AccountAccount(models.Model):
    _inherit = "account.account"


    @api.onchange("account_type")
    def _onchange_account_type(self):

        mapping = {
            'asset_receivable': '100000',
            'asset_cash': '200000',
            'asset_current': '300000',
            'asset_non_current': '400000',
        }

        if self.account_type:
            default_code = mapping.get(self.account_type)
            if default_code:
                # Generate next sequence number by checking existing accounts
                last_account = self.search([
                    ('account_type', '=', self.account_type),
                    ('code', 'like', default_code[:1] + '%')
                ], order="code desc", limit=1)
                print("\n\n\n\n\n=============>",default_code[:1])

                if last_account and last_account.code.isdigit():
                    next_code = str(int(last_account.code) + 1).zfill(6)
                else:
                    next_code = default_code

                self.code = next_code
