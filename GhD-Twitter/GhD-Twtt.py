# -*- coding: utf-8 -*-

##  Análisis de datos de Twitter.
##  TODO:
##      · Migrar a Python 3?
##      · Integración con Jane
##      · Escribir resultados a archivos.
##
import sys
import os
import twitter
import sqlite3
from BDConfiguracion import *
from BDTermos import *
from BDTwitter import *

## Ficheiros de configuración.
## TODO:
##      · Definir resultados.
##      · Definir forma de gardar os datos.

[consumerKey,consumerSecret,accessTokenKey,accessTokenSecret, incT] =leerBDConfiguracion()
print consumerKey
print consumerSecret
print accessTokenKey
print accessTokenSecret
print incT

twtt = twitter.Api(
    consumer_key=consumerKey,
    consumer_secret=consumerSecret,
    access_token_key=accessTokenKey,
    access_token_secret=accessTokenSecret)

## Busqueda por un termo
twtt.GetSearch(
    term='bitcoin',
    raw_query=None,
    geocode=None,
    since_id=None,
    max_id=None,
    until=None,
    count=15,
    lang=None,
    locale=None,
    result_type='mixed',
    include_entities=None)

## Usuarios con tweets que conteñen algún dos termos.
twtt.GetUsersSearch(
    term=None,
    page=1,
    count=20,
    include_entities=None
)

## Información dun Usuario.
twtt.GetUser(
    user_id=None,
    screen_name=None,
    include_entities=True,
    return_json=False
)

## Devolve o historial dun Usuario
twtt.GetUserTimeline(
    user_id=None,
    screen_name=None,
    since_id=None,
    max_id=None,
    count=None,
    include_rts=True,
    trim_user=False,
    exclude_replies=False
)




print '     #-*-#'
