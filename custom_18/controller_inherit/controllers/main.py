from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class DiscountProductsController(WebsiteSale):

    @http.route(['/shop/discounted'],type='http',auth='public',website=True)
    def shop_discounted(self, **kwargs):
        """
        Render discounted product on a custom page.
        """
        products = http.request.env['product.product'].search([('discount','>',0)])

        return http.request.render('controller_inherit.products_discounted', {
            'products': products,
        })