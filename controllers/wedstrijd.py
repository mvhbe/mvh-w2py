# -*- coding: utf-8 -*-

@auth.requires_login()
def detail():
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    kalender = db.kalender(db.kalender.id==wedstrijd.kalender)
    db.wedstrijd.kalender.readable = False
    db.wedstrijd.kalender.writable = False
    form = crud.update(db.wedstrijd, wedstrijd,
                       next=URL("kalender", "wedstrijden", args=kalender.id))
    return dict(form=form, kalender=kalender)


@auth.requires_login()
def nieuw():
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    db.wedstrijd.kalender.readable = False
    db.wedstrijd.kalender.writable = False
    db.wedstrijd.kalender.default = kalender.id
    form = crud.create(db.wedstrijd,
                       next=URL("kalender", "wedstrijden", args=kalender_id))
    return dict(form=form, kalender=kalender)


@auth.requires_login()
def reeksen():
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    print "wedstrijd :" , wedstrijd
    db.wedstrijd.datum.represent = wedstrijd_link
    reeksen = (
        db(db.reeks.wedstrijd==wedstrijd.id).select(orderby=db.reeks.reeksnummer))
    return dict(wedstrijd=wedstrijd, reeksen=reeksen)