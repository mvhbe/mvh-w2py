@auth.requires_login()
def detail():
    reeks_id = request.args(0)
    reeks = db.reeks(reeks_id)
    wedstrijd = db.wedstrijd(db.wedstrijd.id==reeks.wedstrijd)
    db.reeks.wedstrijd.readable = False
    db.reeks.wedstrijd.writable = False
    validate_reeksnummer(reeks.wedstrijd)
    form = crud.update(db.reeks, reeks,
                       next=URL("wedstrijd", "reeksen", args=wedstrijd.id))
    return dict(form=form, wedstrijd=wedstrijd)


@auth.requires_login()
def nieuw():
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    db.reeks.wedstrijd.readable = False
    db.reeks.wedstrijd.writable = False
    db.reeks.wedstrijd.default = wedstrijd.id
    validate_reeksnummer(wedstrijd_id)
    form = crud.create(db.reeks,
                       next=URL("wedstrijd", "reeksen", args=wedstrijd.id))
    return dict(form=form, wedstrijd=wedstrijd)
