# -*- coding: utf-8 -*-

def reeks_link(nummer, row):
    return A(nummer, _href=URL('reeks', 'detail',args=row.id))


db.define_table('reeks',
                Field("wedstrijd", "reference wedstrijd", required=True),
                Field('reeksnummer', 'integer'),
                Field('aanvang', 'time', requires=IS_TIME(), default="13:30"),
                Field('duur', 'time', requires=IS_TIME(), default="02:00"),
                Field('opmerkingen', 'text'),
                auth.signature)