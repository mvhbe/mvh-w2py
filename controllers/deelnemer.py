# -*- coding: utf-8 -*-

@auth.requires_login()
def detail():
    T.force("nl")
    deelnemer_id = request.args(0)
    deelnemer = db.deelnemer(deelnemer_id)
    wedstrijd = db.wedstrijd(db.wedstrijd.id==deelnemer.wedstrijd)
    db.deelnemer.wedstrijd.readable = False
    db.deelnemer.wedstrijd.writable = False
    valideer_deelnemer(wedstrijd.id)
    form = crud.update(db.deelnemer, deelnemer,
                       next=URL("wedstrijd", "deelnemers", args=wedstrijd.id))
    return dict(form=form, wedstrijd=wedstrijd)

@auth.requires_login()
def nieuw():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    db.deelnemer.wedstrijd.readable = False
    db.deelnemer.wedstrijd.writable = False
    db.deelnemer.wedstrijd.default = wedstrijd_id
    valideer_deelnemer(wedstrijd.id)
    form = crud.create(db.deelnemer,
                       next=URL("wedstrijd", "deelnemers", args=wedstrijd_id))
    return dict(form=form, wedstrijd=wedstrijd)
