# -*- coding: utf-8 -*-

import sqlite3
import os

db = 'db/dbConfig'
def crearBDConfiguracion():
    dbConfig = sqlite3.connect(db)
    curConfig = dbConfig.cursor()

    #Só para a primeira creación da base de datos.
    curConfig.execute('CREATE TABLE IF NOT EXISTS CuentaTwitter (clave TEXT,valor TEXT)')
    curConfig.execute('INSERT INTO CuentaTwitter (clave, valor) VALUES(?,?)',('consumerKey','consKey'))
    curConfig.execute('INSERT INTO CuentaTwitter (clave, valor) VALUES(?,?)',('consumerSecret','consSecret'))
    curConfig.execute('INSERT INTO CuentaTwitter (clave, valor) VALUES(?,?)',('accessTokenKey','accTokenKey'))
    curConfig.execute('INSERT INTO CuentaTwitter (clave, valor) VALUES(?,?)',('accessTokenSecret','accTokenSecret'))
    curConfig.execute('INSERT INTO CuentaTwitter (clave, valor) VALUES(?,?)',('intervaloTempo','90'))
    dbConfig.commit()

def modificarBDConfiguracion(consumerKey,consumerSecret,accessTokenKey,accessTokenSecret,incT):
    if not os.path.isfile(db):
        crearBDConfiguracion()
    dbConfig = sqlite3.connect(db)
    curConfig = dbConfig.cursor()

    curConfig.execute('UPDATE CuentaTwitter SET valor=? WHERE clave = ?',(consumerKey,'consumerKey'))
    curConfig.execute('UPDATE CuentaTwitter SET valor=? WHERE clave = ?',(consumerSecret,'consumerSecret'))
    curConfig.execute('UPDATE CuentaTwitter SET valor=? WHERE clave = ?',(accessTokenKey,'accessTokenKey'))
    curConfig.execute('UPDATE CuentaTwitter SET valor=? WHERE clave = ?',(accessTokenSecret,'accessTokenSecret'))
    curConfig.execute('UPDATE CuentaTwitter SET valor=? WHERE clave = ?',(incT,'incT'))
    dbConfig.commit()
    curConfig.close()

def leerBDConfiguracion():
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos Configuración en: ' + db
    dbConfig = sqlite3.connect(db)
    curConfig = dbConfig.cursor()

    curConfig.execute('SELECT valor FROM CuentaTwitter WHERE clave = ?',('consumerKey',))
    consumerKey=curConfig.fetchone()[0]
    curConfig.execute('SELECT valor FROM CuentaTwitter WHERE clave = ?',('consumerSecret',))
    consumerSecret=curConfig.fetchone()[0]
    curConfig.execute('SELECT valor FROM CuentaTwitter WHERE clave = ?',('accessTokenKey',))
    accessTokenKey=curConfig.fetchone()[0]
    curConfig.execute('SELECT valor FROM CuentaTwitter WHERE clave = ?',('accessTokenSecret',))
    accessTokenSecret=curConfig.fetchone()[0]
    curConfig.execute('SELECT valor FROM CuentaTwitter WHERE clave = ?',('intervaloTempo',))
    incT=int(curConfig.fetchone()[0])
    curConfig.close()

    return [consumerKey,consumerSecret,accessTokenKey,accessTokenSecret,incT]
