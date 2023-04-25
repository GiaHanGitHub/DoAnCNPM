from odoo import api, fields, models

class HospitalPatient(models.Models):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    
    name = fields.Char(string='Name', require=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], require = True, default='male')
    note = fields.Text(string= 'Description')
