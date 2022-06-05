# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


{
    "name" : "POS Stock in Odoo",
    "version" : "14.0.0.7",
    "category" : "Point of Sale",
    "depends" : ['base','sale_management','stock','point_of_sale'],
    "author": "BrowseInfo",
    'summary': 'Display POS Stock Quantity on POS screen stock Product stock in POS product stock orders POS Order stock POS Mobile POS Inventory Management pos stocks pos item stock point of sale stock POS Product Warehouse Quantity pos product qty pos product stock Quantity pos product Quantity',
    'price': 29,
    'currency': "EUR",
    "description": """
    """,
    "data": [
        # 'views/assets.xml',
        'views/custom_pos_config_view.xml',
    ],
    'assets': {
        'web.assets_tests': [],
        'point_of_sale.assets': [
            'amcl_pos_stock/static/src/Chrome.js',
            'amcl_pos_stock/static/src/models.js',
            'amcl_pos_stock/static/src/SyncStock.js',
            'amcl_pos_stock/static/src/js/Screens/ProductScreen.js',
            'amcl_pos_stock/static/src/js/Screens/ProductsWidget.js',
            'amcl_pos_stock/static/src/js/Screens/ReceiptScreen.js'
        ],
        'web.assets_backend': [],
        'point_of_sale.pos_assets_backend': [],
        'point_of_sale.pos_assets_backend_style': [],
        'point_of_sale.tests_assets': [],
        'point_of_sale.qunit_suite_tests': [],
        'point_of_sale.assets_backend_prod_only': [],
        'web.assets_qweb': [
            'amcl_pos_stock/static/src/xml/**/*',
        ],
    },
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/X1GSrJl9iWY',
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
