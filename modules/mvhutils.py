# -*- coding: utf-8 -*-

import calendar
import copy
import datetime


def huidige_datum():
    return datetime.datetime.now()


def huidig_jaar():
    return datetime.datetime.now().year


def begin_einde_huidige_maand():
    vandaag = huidige_datum()
    eerste_dag = 1
    laatste_dag = calendar.monthrange(vandaag.year, vandaag.month)[1]
    begin_maand = datetime.date(vandaag.year, vandaag.month, eerste_dag)
    einde_maand = datetime.date(vandaag.year, vandaag.month, laatste_dag)
    return begin_maand, einde_maand