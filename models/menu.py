# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = "Visclub Moed & Volharding"
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Kalender'), False, URL('default', 'kalender'), []),
    #(T('Uitslagen'), False, URL('default', 'uitslagen'), []),
]

if auth.user:
    response.menu.append((T('Kalenders'), False, URL('kalender', 'overzicht'), []))
    response.menu.append((T('Personen'), False, URL('persoon', 'overzicht'), []))

DEVELOPMENT_MENU = True


if "auth" in locals(): auth.wikimenu() 
