# -*- coding:utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nombre Profesor", copy=False, default="Nombre", required=True)
    teacher_card = fields.Char(string="Cedula", copy=False, required=True)
    school_id = fields.Many2one(comodel_name="res.company", string="Escuela", copy=False, required=True)
    
    
    @api.constrains('teacher_card')
    def _check_card(self):
        for record in self:
            existing_teacher = self.search([('teacher_card', '=', record.teacher_card), ('id', '!=', record.id)])
            if existing_teacher:
                raise ValidationError("Ya existe un profesor con ese numero de cedula")