from odoo import http
from odoo.http import request
import base64


class TestControllerOn(http.Controller):

    @http.route('/shopping', type='http', auth='public', website=True)
    def shopping_page(self, **kw):

        details = request.env['test.controller'].sudo().search([])

        products = []
        for rec in details:
            products.append({
                    'id': rec.id,
                    'name': rec.name,
                    'price': rec.price,          
                    'discount': rec.discount,    
                    'total': rec.total,
                    'stock': rec.stock,
                    'is_published': rec.is_published,
                    'image_128': rec.image_128.decode('utf-8') if rec.image_128 else False,

                })


        return request.render("controller_test.shopping_controller_template", {
            'details': products
        })

    @http.route('/buy/<int:product_id>', type='http', auth='public', website=True)
    def buy_product(self, product_id, **kw):

        product = request.env['test.controller'].sudo().browse(product_id)
        qty = int(kw.get('qty', 1))

        if not product.is_published:
            message = "Product is not published / sold out."
            status = 'danger'

        elif qty > product.stock:
            message = f"Sorry! Only {product.stock} item(s) left in stock."
            status = 'warning'

        else:
            request.env['test.purchase.log'].sudo().create({
                'product_name': product.name,
                'price': product.total * qty,
                'name': request.env.user.id,
                'purchase_quantity': qty,
            })

            product.stock -= qty

            message = f"You bought {product.name} for {product.total}!"
            status = 'success'

        details = request.env['test.controller'].sudo().search([])

        products = []
        for rec in details:
            products.append({
                    'id': rec.id,
                    'name': rec.name,
                    'price': rec.price,          
                    'discount': rec.discount,    
                    'total': rec.total,
                    'stock': rec.stock,
                    'is_published': rec.is_published,
                    'image_128': rec.image_128.decode('utf-8') if rec.image_128 else False,

                })

        return request.render("controller_test.shopping_controller_template", {
            'details': products,
            'message': message,
            'status': status,
        })
