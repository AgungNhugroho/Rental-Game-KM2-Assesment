# -*- coding: utf-8 -*-
{
    'name': "RENTAL GAME",

    'summary': """
        Rental Game KM 2""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/game_view.xml',
        'views/playstation_view.xml',
        'views/perlengkapan_view.xml',
        'views/katalog_view.xml',
        'views/order_view.xml',
        'views/pegawai_rental_view.xml',
        'views/pengembalian_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
