# -*- coding: utf-8 -*-

@auth.requires_login()
def overzicht():
    db.kalender.jaar.represent = jaar_link
    kalenders = db(db.kalender).select(orderby=~db.kalender.jaar)
    return dict(kalenders=kalenders)

@auth.requires_login()
def overzicht_old():
    db.kalender.jaar.represent = jaar_link
    grid = SQLFORM.grid(db.kalender, editable=False, deletable=False,
                        create=False, details=False, csv=False,
                        fields=[db.kalender.jaar],
                        field_id=db.kalender.id,
                        sortable=False,
                        searchable=False,
                        links=[wedstrijden_link],
                        orderby=~db.kalender.jaar)
    return dict(grid=grid)

@auth.requires_login()
def detail():
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    form = crud.update(db.kalender, kalender, next=URL("overzicht"))
    return dict(form=form)

@auth.requires_login()
def nieuw():
    form = crud.create(db.kalender, next="overzicht")
    return dict(form=form)


@auth.requires_login()
def wedstrijden():
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    wedstrijden = (
        db(db.wedstrijd.kalender==kalender.id).select(db.wedstrijd.datum,
                                                   db.wedstrijd.omschrijving,
                                                   orderby=db.wedstrijd.datum))
    return dict(kalender=kalender, wedstrijden=wedstrijden)