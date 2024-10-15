from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nombre", default="Nombre Alumno", copy=False, required=True)
    grade = fields.Selection(selection=[
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('tercero', 'Tercero'),
    ], string="Grado", copy=False, required=True)
    age = fields.Integer(string="Edad", copy=False)
    
    student_num = fields.Char(string="Numero de alumno", copy=False, required=True)
    school_id = fields.Many2one(comodel_name="res.company", string="Escuela", copy=False)
    
    @api.constrains('student_num')
    def _check_card(self):
        for record in self:
            existing_student = self.search([('student_num', '=', record.student_num), ('id', '!=', record.id)])
            if existing_student:
                raise ValidationError("Ya existe un alumno con ese numero")
