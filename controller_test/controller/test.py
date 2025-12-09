from odoo import http
from odoo.http import request
import base64


class TestControllerOn(http.Controller):

    @http.route('/shopping', type='http', auth='public', website=True)
    def shopping_page(self, **kw):

        message = kw.get('message')
        status = kw.get('status')

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


    @http.route('/buy/<int:product_id>', type='http', auth='public',
            website=True, methods=['POST'], csrf=False)
    def buy_product(self, product_id, **kw):

        product = request.env['test.controller'].sudo().browse(product_id)

        # ✅ Safety check
        if not product.exists():
            return request.redirect("/shopping?message=Invalid product&status=danger")

        qty = int(kw.get('qty', 1))

        if not product.is_published:
            message = "Product is not published / sold out."
            status = 'danger'

        elif qty > product.stock:
            message = f"Sorry! Only {product.stock} item(s) left in stock."
            status = 'warning'

        else:
            user = request.env.user

            existing_log = request.env['test.purchase.log'].sudo().search([
                ('name', '=', user.id),
                ('product_name', '=', product.name)
            ], limit=1)

            if existing_log:
                existing_log.write({
                    'price': existing_log.price + (product.total * qty),
                    'purchase_quantity': existing_log.purchase_quantity + qty,
                })
            else:
                request.env['test.purchase.log'].sudo().create({
                    'product_name': product.name,
                    'price': product.total * qty,
                    'name': user.id,
                    'purchase_quantity': qty,
                })

            product.sudo().write({
                'stock': product.stock - qty
            })

            message = f"You bought {product.name} successfully!"
            status = 'success'

        return request.redirect(
            "/shopping?message=%s&status=%s" % (message, status)
        )
