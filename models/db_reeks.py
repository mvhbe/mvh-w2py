# -*- coding: utf-8 -*-
db.define_table('reeks',
                Field("wedstrijd", "reference wedstrijd", required=True),
                Field('reeksnummer', 'integer'),
                Field('aanvang', 'time', requires=IS_TIME(), default="13:30"),
                Field('duur', 'time', requires=IS_TIME(), default="02:00"),
                Field('opmerkingen', 'text'),
                auth.signature)