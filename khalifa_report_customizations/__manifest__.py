# -*- coding: utf-8 -*-
{
    'name': "Report Csutomizations",

    'summary': """
         Modify Purchase Order Reports""",

    'description': """
        Modify Purchase Order Reports
    """,

    'author': "AMCL",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '15.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'purchase', 'sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/purchaseorder_report_customizations.xml',
        'views/purchase_order.xml',
        'views/stock.xml',
        'report/goods_delivery_note_report_menu.xml',
        'views/sale_order_view.xml',
    ],
    'assets': {
            'web.report_assets_pdf': [
                'khalifa_report_customizations/static/src/scss/**/*',
            ],
            'web.report_assets_common': [
                'khalifa_report_customizations/static/src/scss/**/*',
            ],
        }
    # only loaded in demonstration mode

}