# -*- coding: utf-8 -*-

def deelnemer_string(achternaam, voornaam):
    return achternaam + " " + voornaam

def deelnemer_link(row):
    return A(deelnemer_string(row.achternaam, row.voornaam),
             _href=URL('deelnemer', 'detail',args=row.id))

db.define_table('deelnemer',
                Field("wedstrijd", "reference wedstrijd", required=True),
                Field('deelnemer', 'reference persoon'),
                auth.signature)

def valideer_deelnemer(wedstrijd_id):
    deelnemers = db(db.deelnemer.wedstrijd==wedstrijd_id)
    db.deelnemer.deelnemer.requires = [
        IS_NOT_EMPTY(error_message="Deelnemer niet ingevuld !"),
        IS_IN_DB(db,db.persoon, error_message="Deelnemer bestaat niet !"),
        IS_NOT_IN_DB(deelnemers, db.deelnemer.deelnemer,
                     error_message="Deelnemer bestaat reeds !")
    ]
