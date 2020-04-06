from odoo import models, fields
class CovidDiagnostico(models.Model):

    _name = "covid.diagnostico"
    _description = "Diagnostico Covid"

    # def default_get(self, vals):
    #

    name = fields.Char()
    data_diagnostico = fields.Date()
    paciente_id = fields.Many2one(
        comodel_name='res.partner',
        string='Paciente',
        required = True,
    )
    medico_id = fields.Many2one(
        comodel_name='res.partner',
        string='Médico',
        required=True,
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('suspect', 'Suspeito'),
            ('confimed', 'Confirmado'),
            ('negative', 'Negativo'),
        ],
        default='draft',
        string="Situação",
    )
    comorbidade_ids = fields.Many2many(
        comodel_name="covid.comorbidade",
        name="Comorbidade",
    )
    sintomas_ids = fields.Many2many(
        comodel_name="covid.sintomas",
        string="Sintomas",
    )

    def imprimir(self):
        for record in self:
            print(record.pacient_id, record.comorbidade_ids, record.sintomas_ids)