# -*- coding: utf-8 -*-
# from odoo import http


# class Contacts(http.Controller):
#     @http.route('/contacts/contacts', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacts/contacts/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacts.listing', {
#             'root': '/contacts/contacts',
#             'objects': http.request.env['contacts.contacts'].search([]),
#         })

#     @http.route('/contacts/contacts/objects/<model("contacts.contacts"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacts.object', {
#             'object': obj
#         })

