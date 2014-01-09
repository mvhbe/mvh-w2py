# -*- coding: utf-8 -*-

@auth.requires_login()
def overzicht():
    T.force("nl")
    #db.persoon..represent = persoon_link
    personen = db(db.persoon).select(orderby=db.persoon.nummer)
    return dict(personen=personen)


@auth.requires_login()
def detail():
    T.force("nl")
    persoon_id = request.args(0)
    persoon = db.persoon(persoon_id)
    form = crud.update(db.persoon, persoon, next=URL("overzicht"))
    return dict(form=form)


@auth.requires_login()
def nieuw():
    T.force("nl")
    form = crud.create(db.persoon, next=URL("overzicht"))
    return dict(form=form)
