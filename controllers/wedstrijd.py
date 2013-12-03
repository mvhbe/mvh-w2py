# -*- coding: utf-8 -*-

@auth.requires_login()
def detail():
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    kalender = db.kalender(db.kalender==wedstrijd.kalender)
    form = crud.update(db.wedstrijd, wedstrijd, next=URL("overzicht"))
    return dict(form=form, kalender=kalender)

@auth.requires_login()
def nieuw():
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    db.wedstrijd.kalender.readable = False
    db.wedstrijd.kalender.writable = False
    db.wedstrijd.kalender.default = kalender.id
    form = crud.create(db.wedstrijd, next="overzicht")
    return dict(form=form)
