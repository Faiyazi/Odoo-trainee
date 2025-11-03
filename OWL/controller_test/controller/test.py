from odoo import http
from odoo.http import request


class TestControllerOn(http.Controller):

    # 🛍️ Show all products
    @http.route('/shopping', type='http', auth='public', website=True)
    def shopping_page(self, **kw):
        print( "********** Shopping Page **********" )
        details = request.env['test.controller'].sudo().search(['is_published','=',True])
        return request.render("controller_test.shopping_controller_template", {
            'details': details
        })

    # 🛒 Handle Buy button click
    @http.route('/buy/<int:product_id>', type='http', auth='public', website=True)
    def buy_product(self, product_id, **kw):
        product = request.env['test.controller'].sudo().browse(product_id)
        message = ""

        if product.exists():
            # Example: log purchase into another model (optional)
            request.env['test.purchase.log'].sudo().create({
                'product_name': product.name,
                'price': product.total,
            })
            message = f"✅ You bought {product.name} for ₹{product.total}!"
        else:
            message = "❌ Product not found."

        # Re-render the product list with message
        details = request.env['test.controller'].sudo().search([])
        return request.render("controller_test.shopping_controller_template", {
            'details': details,
            'message': message
        })
