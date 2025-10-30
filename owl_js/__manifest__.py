{
    "name": "Owl JS",
    "description": "Owl JS module for practice.",
    "license": "LGPL-3",
    "website": "www.example.com",
    "author": "John Doe",
    "depends": ["base"],
    "installable" : True,
    "application" : True,
    "data": [
        "views/owl_js_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            # ✅ Include ALL CSS and JS under your static/src
            "owl_js/static/src/js/*.js",
            "owl_js/static/src/xml/*.xml",
            "owl_js/static/src/css/*.css",
        ],
    }
}
