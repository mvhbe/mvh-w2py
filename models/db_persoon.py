# -*- coding: utf-8 -*-

def persoon_string(achternaam, voornaam):
    return achternaam + " " + voornaam

def persoon_link(achternaam, voornaam, row):
    return A(persoon_string(achternaam, voornaam),
             _href=URL('persoon', 'detail',args=row.id))

db.define_table('persoon',
                Field('nummer', 'integer', unique=True, notnull=True,
                      required=True),
                Field("achternaam", "string", length=50, notnull=True,
                      required=True),
                Field('voornaam', 'string', length=50, notnull=True,
                      required=True),
                auth.signature)

db.persoon.nummer.requires = [
    IS_NOT_EMPTY(error_message="Nummer niet ingevuld !"),
    IS_NOT_IN_DB(db, db.persoon.nummer,
                 error_message="Nummer bestaat reeds !")
]
db.persoon.achternaam.requires = [
    IS_NOT_EMPTY(error_message="Achternaam niet ingevuld !")
]
db.persoon.voornaam.requires = [
    IS_NOT_EMPTY(error_message="Voornaam niet ingevuld !")
]