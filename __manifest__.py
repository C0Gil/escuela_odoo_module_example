# -*- coding:utf-8 -*-
{
    'name': 'exdoo_school',
    'version': '1.0',
    'depends': [
        'base',
        'mail',
    ],
    'author': 'Gilberto C. O.',
    'category': 'Sale',
    'website': 'http://www.google.com',
    "license" : "AGPL-3",
    'description': '''

      Este modulo realiza un control de materias, alumnos y maestros

    ''',
    'data':[
      'security/groups.xml',
      'security/ir.model.access.csv',
      'views/view_subject.xml',
      'views/view_teacher.xml',
      'views/view_student.xml',
      'views/menu.xml'
    ],
}