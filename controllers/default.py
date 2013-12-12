# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
#from mvhutils import begin_einde_huidige_maand
import mvhutils

TODO = "Under construction ! Available soon."


def index():
    begin_maand, einde_maand = mvhutils.begin_einde_huidige_maand()
    query = ((db.wedstrijd.id==db.reeks.wedstrijd)&
             (db.reeks.reeksnummer==1)&
             (db.wedstrijd.datum >= begin_maand)&
             (db.wedstrijd.datum <= einde_maand))
    wedstrijden = db(query).select(db.wedstrijd.datum,
                                   db.wedstrijd.omschrijving,
                                   db.reeks.aanvang)
    #wedstrijden = SQLFORM.grid(query,
    #                    create=False, details=False, csv=False,
    #                    editable=False, deletable=False,
    #                    fields=[db.wedstrijd.datum, db.wedstrijd.omschrijving],
    #                    field_id=db.wedstrijd.id,
    #                    sortable=False,
    #                    searchable=False,
    #                    orderby=db.wedstrijd.datum
    #                    )
    return dict(wedstrijden=wedstrijden)


def kalender():
    jaar = str(mvhutils.huidig_jaar())
    kalender = db.kalender(db.kalender.jaar==jaar)
    query = ((db.wedstrijd.kalender==kalender)&
             (db.wedstrijd.id==db.reeks.wedstrijd)&
             (db.reeks.reeksnummer==1))
    wedstrijden = db(query).select(db.wedstrijd.datum,
                                   db.wedstrijd.omschrijving,
                                   db.reeks.aanvang,
                                   orderby=db.wedstrijd.datum)
    return dict(wedstrijden=wedstrijden, huidig_jaar=jaar)


def uitslagen():
    return dict(message=TODO)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
