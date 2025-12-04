from odoo import http
from odoo.http import request
import base64


class TestControllerOn(http.Controller):

    @http.route('/shopping', type='http', auth='public', website=True)
    def shopping_page(self, **kw):
        print( "********** Shopping Page **********" )
        details = request.env['test.controller'].sudo().search([])
        return request.render("controller_test.shopping_controller_template", {
            'details': details
        })

    @http.route('/buy/<int:product_id>', type='http', auth='public', website=True)
    def buy_product(self, product_id, **kw):
        product = request.env['test.controller'].sudo().browse(product_id)
        message = ""

        if product.exists():
            request.env['test.purchase.log'].sudo().create({
                'product_name': product.name,
                'price': product.total,
                'name': request.env.user.id,
            })
            message = f" You bought {product.name} for {product.total}!"
        else:
            message = " Product not found."

        details = request.env['test.controller'].sudo().search([])
        return request.render("controller_test.shopping_controller_template", {
            'details': details,
            'message': message
        })
