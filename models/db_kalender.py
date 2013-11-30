# -*- coding: utf-8 -*-

def jaar_string(jaar, row):
    return "Wedstrijdkalender " + jaar

def jaar_link(jaar, row):
    return A(jaar_string(jaar, row), _href=URL('kalender', 'detail', args=row.id))

def wedstrijden_link(row):
    return A("wedstrijden", _href=URL("kalender", "wedstrijden", args=row.id))

db.define_table('kalender',
                Field('jaar', 'string', length=4, unique=True, notnull=True),
                Field('opmerkingen', 'text'),
                auth.signature)

db.kalender.jaar.represent = jaar_string

