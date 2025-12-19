# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    "name": "Chatter Hide & Change Position",
    "version": "1.0",
    "description": """
    
    [Hide Chatter From Chatter]: Step 1:  Go to any module in which chatter exist.
                    Step 2: You well see an "X" click on it chatter will hide
                    Step 3: After Chatter hide there well be an "Show Chatter,
                            well be appaer in contronal panel before page change buttons.
                    Step 4: Click that button Chatter well appear again.        
                    "
                    
    [Hide Chatter From User Preference]:Step 1: Open'My Preference' you will see
                                                Hide Chatter make it true 
                                        
                                        Step 2: To Show Chatter again goto 'My Preference'
                                                make Hide Chatter False                       
    """,
    "license": "LGPL-3",
    'category': 'Tools',
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com',
    'support': 'sales@caretit.com',
    "depends": ["base","mail","web"],
    "installable": True,
    "application": True,
    "sequence": 1,

    "data": [
        'views/chatter_button_inherit.xml',
    ],

    "assets": {
        "web.assets_backend": [
            
            # Inherited from MUK module
            'cit_chatter_hide_change_position/static/src/chatter/chatter.js',
            'cit_chatter_hide_change_position/static/src/chatter/chatter.xml',
            'cit_chatter_hide_change_position/static/src/core/thread/thread.js',
            'cit_chatter_hide_change_position/static/src/core/thread/thread.xml',
        
            # Resize of chatter
            'cit_chatter_hide_change_position/static/src/change_position/resize_chatter.js',
            'cit_chatter_hide_change_position/static/src/change_position/resize_chatter.xml',
            'cit_chatter_hide_change_position/static/src/change_position/chatter.scss',
            
            # Fill Form view
            'cit_chatter_hide_change_position/static/src/change_position/full_form_view.js',
            
            # Hide Chatter
            'cit_chatter_hide_change_position/static/src/hide_chatter/hide_chatter.xml',
            'cit_chatter_hide_change_position/static/src/hide_chatter/show_chatter.xml',
            'cit_chatter_hide_change_position/static/src/hide_chatter/chatter_hide_show.js',
            'cit_chatter_hide_change_position/static/src/hide_chatter/chatter_hide_user_service.js',
            
            # Position Change
            'cit_chatter_hide_change_position/static/src/change_position/chatter_change_position.js',
            'cit_chatter_hide_change_position/static/src/change_position/chatter_reloader.js',
            'cit_chatter_hide_change_position/static/src/change_position/change_position.xml',
           
            # CSS
            'cit_chatter_hide_change_position/static/src/css/hide_chatter.css',
            'cit_chatter_hide_change_position/static/src/css/position_change.css',
            'cit_chatter_hide_change_position/static/src/css/full_form_view.css',
            
    
        ],
    },
    
    'image':['static/description/icon.png'],
}
