from odoo import models, fields, api

class CovidSintomas(models.Model):
    _name='covid.sintomas'
    _description = 'Sintomas da Covid'

    _rec_name = 'display_name'

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "[{} - {}".format(record.codigo_sid, record.sintomas)))
        return result

    codigo_sid = fields.Char(string='Sid')
    sintomas = fields.Char(string='Sintomas')

    def botao_criar_sintoma_dor_corpo(self):
        # self.env['covid.sintomas'] Não é necessária
        self.create(
            {'codigo_sid': '12', 'sintomas': 'Dor no corpo'}
        )


    def botao_criar_comorbidade(self):
        """ Criando um registro a partir de outro
        :return:
        """
        self.env['covid.comorbidade'].create(
            {'codigo_sid': '12', 'comorbidade': 'Dor no corpo'}
        )

    def converter_em_sintomas_graves(self):
        print(self)
        print(self.env)
        for record in self:
            record.sintomas = record.sintomas + ' !!!'