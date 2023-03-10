{
    'name' : 'interior_design',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'It is to decorate your real estate,property,home,office',
    'description': 'App for interior desiging',
    'author': 'sami',
    'license': 'LGPL-3',
    'depends':['mail'],
    'data':[
            'security/ir.model.access.csv',
            'views/design_view_action.xml',
            'views/design_rennovation.xml',
            'views/consultation_virtual_meet_view.xml',
            'views/consultation_real_meet_view.xml',
            'views/rennovation_stories_view.xml',
            'views/design_interior_paint.xml',
            'views/employee_info.xml',
            'views/employee_tag_view.xml',
            'views/customer_informatio_page.xml',
            'views/design_menu_view.xml'
    ],
    'demo':[
        'demo/employee_info_demo.xml',
        'demo/consultation_real_meet_demo.xml',
        'demo/type_of_property_demo.xml',
        'demo/paint_colors_demo.xml',
        'demo/employee_tag_demo.xml',
        'demo/customer_demo_data.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,


}