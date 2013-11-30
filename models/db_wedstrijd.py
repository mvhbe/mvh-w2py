# -*- coding: utf-8 -*-

def wedstrijd_string(datum):
    return datum

def wedstrijd_link(datum, row):
    return A(datum, _href=URL('wedstrijd', 'detail',args=row.id))

db.define_table('wedstrijd',
                Field("kalender", "reference kalender"),
                Field('datum', 'date', unique=True, notnull=True,
                      requires=IS_DATE(format='%d/%m/%Y')),
                Field('omschrijving', 'string', length=100),
                Field('inleg', 'string', length=100,
                      default="3,00 euro/deelnemer"),
                Field('vooruit', 'string', default="0,50 euro/deelnemer"),
                Field('opmerkingen', 'text'),
                auth.signature)
