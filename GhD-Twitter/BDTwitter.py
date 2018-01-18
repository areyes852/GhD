# -*- coding: utf-8 -*-

import sqlite3
import os
db = 'db/dbTwitter'

def crearBDTwitter():
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()

    curTwitter.execute('CREATE TABLE IF NOT EXISTS ContasTwitter (conta_id INTEGER PRIMARY KEY, conta TEXT UNIQUE, reputacion INTEGER, seguidores INTEGER, verificado BOOLEAN, rexion TEXT, carizXeral integer)')

    dbTwitter.commit()
    curTwitter.close()


def engadirContaBDTwitter(conta, reputacion, seguidores, verificado, rexion, carizXeral):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('INSERT OR IGNORE INTO ContasTwitter (conta, reputacion, seguidores, verificado, rexion, carizXeral) VALUES(?,?,?,?,?,?)',(conta, reputacion, seguidores, verificado, rexion, carizXeral))
    dbTwitter.commit()
    curTwitter.close()

def obterIDContaBDTwitter(conta):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('SELECT conta_id FROM ContasTwitter WHERE conta = ?',(conta,))
    conta_id=curTwitter.fetchone()[0]
    dbTwitter.commit()
    curTwitter.close()
    return conta_id

def modificarReputacionContaBDTwitter(conta_id, reputacion):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('UPDATE ContasTwitter SET reputacion=? WHERE conta_id = ?',(reputacion,conta_id))
    dbTwitter.commit()
    curTwitter.close()

def modificarSeguidoresContaBDTwitter(conta_id, seguidores):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('UPDATE ContasTwitter SET seguidores=? WHERE conta_id = ?',(seguidores,conta_id))
    dbTwitter.commit()
    curTwitter.close()

def modificarVerificadoContaBDTwitter(conta_id, verificado):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('UPDATE ContasTwitter SET verificado=? WHERE conta_id = ?',(verificado,conta_id))
    dbTwitter.commit()
    curTwitter.close()

def modificarRexionContaBDTwitter(conta_id, rexion):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('UPDATE ContasTwitter SET rexion=? WHERE conta_id = ?',(rexion,conta_id))
    dbTwitter.commit()
    curTwitter.close()

def modificarCarizXeralContaBDTwitter(conta_id, carizXeral):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('UPDATE ContasTwitter SET carizXeral=? WHERE conta_id = ?',(carizXeral,conta_id))
    dbTwitter.commit()
    curTwitter.close()

def obterContaBDTwitter(conta_id):
    # TODO: Devolver os modificadores asociados a cada termo
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos ContasTwitter en: ' + db
    dbTwitter = sqlite3.connect(db)
    curTwitter = dbTwitter.cursor()
    curTwitter.execute('SELECT * FROM ContasTwitter WHERE conta_id = ?',(conta_id,))
    conta = curTwitter.fetchone()
    curTwitter.close()
    return conta
