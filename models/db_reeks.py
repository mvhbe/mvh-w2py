# -*- coding: utf-8 -*-

def reeks_link(nummer, row):
    return A(nummer, _href=URL('reeks', 'detail',args=row.id))


db.define_table('reeks',
                Field("wedstrijd", "reference wedstrijd", required=True),
                Field('reeksnummer', 'integer'),
                Field('aanvang', 'time', default="13:30"),
                Field('duur', 'time', default="02:00"),
                Field('opmerkingen', 'text'),
                auth.signature)

def valideer_reeksnummer(wedstrijd_id):
    reeksen = db(db.reeks.wedstrijd==wedstrijd_id)
    db.reeks.reeksnummer.requires = IS_NOT_IN_DB(reeksen, db.reeks.reeksnummer)

db.reeks.aanvang.requires = [
    IS_NOT_EMPTY(error_message="Aanvang niet ingevuld !"),
    IS_TIME()
]
db.reeks.duur.requires = [
    IS_NOT_EMPTY(error_message="Duur niet ingevuld !"),
    IS_TIME()
]