# -*- coding:utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Subject(models.Model):
    _name = 'subject'
    _description = "Subject"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nombre", copy=False, default="Nuevo", required=True)    
    company_id = fields.Many2one(comodel_name="res.company", string="Escuela", default=lambda self: self.env.company, context={'create': False}, required=True)
    
    teacher_id = fields.Many2one(comodel_name="teacher", string="Maestros")
    teacher_card = fields.Char(string="Cedula", related="teacher_id.teacher_card")
    
    grade = fields.Selection(selection=[
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
    ], string="Grado", copy=False)
    
    classroom = fields.Selection(selection=[
        ('salon_1', 'Salon 1'),
        ('salon_2', 'Salon 2'),
        ('salon_3', 'Salon 3'),
        ('salon_4', 'Salon 4'),
        ('salon_5', 'Salon 5'),
    ], string="Salon", copy=False)
    
    states = fields.Selection(selection=[
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
    ], default='activa', string='Estados', copy=False)
        
    students_ids = fields.One2many(comodel_name="student.subject", 
                                   inverse_name="subject_id", string="ids de alumnos")
    
    starting_date = fields.Datetime(string="Fecha de inicio", copy=False)
    ending_date = fields.Datetime(string="Fecha de Fin", copy=False)
    schedule = fields.Selection(selection=[
        ('7-8', 'De 7:00 am a 8:00 am'),
        ('8-9', 'De 8:00 am a 9:00 am'),
    ], string="Horario", copy=False)
    
    def activate_subject(self):
        self.states = 'activa'
    
    def deactivate_subject(self):
        self.states = 'inactiva'
        
class StudentForSubject(models.Model):
    _name = "student.subject"
    _description = "students.subject"        
    
    #name = fields.Many2one(comodel_name="student", string="Alumno", domain="[('id', 'in', students_domain)]") #forma 1: utilizando compute
    name = fields.Many2one(comodel_name="student", string="Alumno", domain="[('grade', '=', parent.grade),('school_id','=',parent.compnay_id)]") #filtro con padre
    students_domain = fields.Many2many(
        comodel_name ='student',
        compute="_compute_students_grade",
        string="Alumnos con grado"
    )
    
    age = fields.Integer(string="Edad", copy=False)
    student_num = fields.Char(string="Numero de alumno", copy=False)
    
    grade = fields.Selection(selection=[
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
    ], string="Grado")
    
    subject_id = fields.Many2one(comodel_name="subject", string="Materia",)
    school_id = fields.Many2one(comodel_name="res.company", string="Escuela")
    
    @api.onchange('name')
    def _onchange_student(self):
        if self.name:
            self.gre = self.name.age
            self.student_num = self.name.student_num
            
    @api.depends('subject_id')
    def _compute_studade = self.name.grade
            self.agents_grade(self):
        for record in self:
            if record.subject_id:
                record.students_domain = record.env['student'].search([('school_id', '=', record.subject_id.company_id.id), ('grade', '=', record.subject_id.grade)])
            