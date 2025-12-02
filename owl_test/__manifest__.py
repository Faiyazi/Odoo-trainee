{
    "name": "Owl Test",
    "description": "Owl JS module for practice.",
    "license": "LGPL-3",
    "website": "www.example.com",
    "author": "John Doe",
    "depends": ["base", "web","sale_management"],
    "installable" : True,
    "application" : True,
    "sequence" : 1,
    "data": [
        "security/ir.model.access.csv",
        "views/todo_list_owl.xml",
        "views/owl_sale_inherit.xml",
        "views/owl_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # Js
            "owl_test/static/src/js/owl_component.js",
            "owl_test/static/src/js/owl_counter.js",
            "owl_test/static/src/js/text.js",
            "owl_test/static/src/example/owl_example.js",
            "owl_test/static/src/child/child.js",
            # "owl_test/static/src/lub/services.js",
            "owl_test/static/src/components/todo_list/todo_list.js",
            # "owl_test/static/src/js/test_patching.js",
            
            # XML
            "owl_test/static/src/xml/owl_home_demo_fetch.xml",
            "owl_test/static/src/xml/owl_templates.xml",
            "owl_test/static/src/xml/testowl.xml",
            "owl_test/static/src/example/owl_example_view.xml",
            "owl_test/static/src/child/child.xml",
            "owl_test/static/src/components/todo_list/todo_list.xml",
            
            # CSS
            "owl_test/static/src/css/owl_test_component.css",
        ],
    },
    
    "image":"owl_test/static/description/icon.png",
}