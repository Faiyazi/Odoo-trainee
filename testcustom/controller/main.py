from odoo import http
from odoo.http import request

# from odoo.addons.website_sale.controllers.main import WebsiteSale


# class WebsiteSaleInherit(WebsiteSale):
#     @http.route([
#         '/shop',
#         '/shop/page/<int:page>',
#         '/shop/category/<model("product.public.category"):category>',
#         '/shop/category/<model("product.public.category"):category>/page/<int:page>',
#     ], type='http', auth="public", website=True)
    
#     def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
#         res = super(WebsiteSaleInherit,self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post)
#         print('Faiyaz')
#         return res
    
    
    
    
    # class WebsiteSaleInherit(WebsiteSale):

    # @http.route(['/shop'], type='http', auth="public", website=True)
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
    #     # Call parent without passing self explicitly
    #     res = super(WebsiteSaleInherit, self).shop(
    #         page=page,
    #         category=category,
    #         search=search,
    #         min_price=min_price,
    #         max_price=max_price,
    #         ppg=ppg,
    #         **post
    #     )
    #     return res


# class Practice(http.Controller):

#     @http.route('/testcustom/hello', type="http", website=True, auth="public")
#     def practice_task(self, **kw):
#         details = request.env['task.custom'].sudo().search([])

#         return request.render('testcustom.test_custom_website', {
#             'details': details   # pass recordset
#         })


class Practice(http.Controller):
    @http.route('/Custom', type="http", website=True, auth='public' , cors='*')
    def practice_task(self, **kw):
        details = request.env['task.custom'].sudo().search([])
        
        return request.render('testcustom.test_custom_website', {
            'details': details  })
        
       
       

# class Practice(http.Controller):
#     @http.route('/Custom', type="http", website=True, auth='user')
#     def practice_task(self, **kw):
#         details = request.env['task.custom'].sudo().search([])
        
#         return request.render('testcustom.test_custom_website', {
#             'details': details  })
        
        
        
# class Practice(http.Controller):
#     @http.route('/Custom', type="json", website=True, auth='public' ,method=['GET'])
#     def practice_task(self, **kw):
#         details = request.httprequest.json
        
#         return  {
#             'success':'Susceess',
#             'details': details  }
        
        
        
