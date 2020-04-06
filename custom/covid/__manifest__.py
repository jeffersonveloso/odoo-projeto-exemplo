{
    # -*- coding: utf-8 -*-
    'name': "Covid",
    'summary': "Esta é uma descrição simples do novo módulo que estou desenvolvendo",
    'description': """Este campo deve ser usado para fornecer uma descrição mais completa
                      sobre o módulo o qual estou desenvolvendo""",
    'author': "MeuNomeCompleto",
    'license': "AGPL-3",
    'website': "http://www.meuwebsite.com.br",
    'category': 'Uncategorized',
    'version': '12.0.1.0.0', # esta é a versão padrão para se começar um módulo!
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'views/covid_menu.xml',

        'views/covid_comorbidade_view.xml',

        'views/covid_diagnostico_view.xml',

        'views/covid_sintomas_view.xml',
    ],
    #'demo': ['demo.xml'],
}