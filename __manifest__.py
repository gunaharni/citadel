{
    'name': 'Citadel',
    'version': '13.0.1.0',
    'category': 'Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    'license': 'AGPL-3',
    'summary': 'Citadels training management app',
    'description': """Module to manage courses""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/course.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False

}