# -*- coding: utf-8 -*-

@auth.requires_login()
def overzicht():
    T.force("nl")
    db.kalender.jaar.represent = jaar_link
    kalenders = db(db.kalender).select(orderby=~db.kalender.jaar)
    return dict(kalenders=kalenders)


@auth.requires_login()
def detail():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    form = crud.update(db.kalender, kalender, next=URL("overzicht"))
    return dict(form=form)


@auth.requires_login()
def nieuw():
    T.force("nl")
    form = crud.create(db.kalender, next="overzicht")
    return dict(form=form)


@auth.requires_login()
def wedstrijden():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    db.wedstrijd.datum.represent = wedstrijd_link
    wedstrijden = (
        db(db.wedstrijd.kalender==kalender.id).select(db.wedstrijd.id,
                                                      db.wedstrijd.datum,
                                                      db.wedstrijd.omschrijving,
                                                      orderby=db.wedstrijd.datum))
    return dict(kalender=kalender, wedstrijden=wedstrijden)