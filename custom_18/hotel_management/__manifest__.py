{
    "name": "Hotel Management",
    "version": "1.0",
    "summary": "Rooms, Reservations, Housekeeping, Pricing, Folios, Website & Portal",
    "category": "Services/Hotel",
    "author": "Your Company",
    "license": "LGPL-3",
    "depends": [
        "base", "mail", "web", "sale", "account", "stock", "website", "portal",
        "point_of_sale"
    ],
    "data": [
        "security/hotel_security.xml",
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "data/cron_data.xml",
        "data/mail_template_data.xml",
        "views/hotel_menus.xml",
        "views/hotel_room_views.xml",
        "views/hotel_pricing_views.xml",
        "views/hotel_reservation_views.xml",
        "views/hotel_folio_views.xml",
        "views/hotel_housekeeping_views.xml",
        "wizard/checkin_wizard_views.xml",
        "wizard/checkout_wizard_views.xml",
        "report/hotel_reports.xml",
        "report/hotel_reservation_report.xml",
        "views/portal_templates.xml",
        "views/website_templates.xml"
    ],
    "assets": {
        # "web.assets_backend": ["hotel_management/static/src/**/*"],
        # "web.assets_frontend": ["hotel_management/static/src/website/**/*"],
    },
    "application": True,
    "installable": True
}
