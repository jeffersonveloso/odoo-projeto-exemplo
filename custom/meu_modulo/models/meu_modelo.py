from odoo import models, fields

class MeuModelo(models.Model):

    _name = 'meu.modelo'

    name = fields.Char(string=u'Nome Completo', required=True)
    date = fields.Date(string=u'Data')
    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string=u'Parceiro',
    )

    def imprimir(self):
        print(self.name, self.date)

class Books(models.Model):

    _name = 'meu.modelo_teste'

    title = fields.Char(string=u'Título', required=True)
    author = fields.Many2many(
        comodel_name='res.users',
        string=u'Autor'
    )
    editora = fields.Many2many(
        comodel_name='res.partner',
        string=u'Editora'
    )


