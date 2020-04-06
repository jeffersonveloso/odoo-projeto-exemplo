from odoo import models, fields, api

class CovidComorbidade(models.Model):
    _name = 'covid.comorbidade'
    _description = 'Comobirdade Covid'

    _rec_name = 'display_name'

    codigo_sid = fields.Char(string='Sid')
    comorbidade = fields.Char(string='Comorbidade')

    display_name= fields.Char(string='_compute_display_name', store=True)

    @api.depends('codigo_sid','comorbidade')
    def _compute_display_name(self):
        for record in self:
            record.display_name = "[{}] - {}".format(
                    record.codigo_sid, record.comorbidade
                )

