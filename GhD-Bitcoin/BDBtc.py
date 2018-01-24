# -*- coding: utf-8 -*-

import sqlite3
import os

db = '/mnt/hdd/db/dbBtc'
def crearBDBtc():
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()

    #Só para a primeira creación da base de datos.
    curBtc.execute('CREATE TABLE IF NOT EXISTS ContaCoinbase (clave TEXT,valor TEXT)')
    curBtc.execute('INSERT INTO ContaCoinbase (clave, valor) VALUES(?,?)',('api_key','KcD6KbiczVpLS2Z2'))
    curBtc.execute('INSERT INTO ContaCoinbase (clave, valor) VALUES(?,?)',('api_secret','COLyP3pPPfksDe7Wx3Z6hwnmYmUMsV1Q'))


    curBtc.execute('CREATE TABLE IF NOT EXISTS Prezos (prezoCompra MONEY, prezoVenta MONEY, prezoSpot MONEY, tempo TIME)')

    dbBtc.commit()
    curBtc.close()

def obterCredenciales():
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('SELECT valor FROM ContaCoinbase WHERE clave =?',('api_key',))
    apiKey=curBtc.fetchone()[0]
    curBtc.execute('SELECT valor FROM ContaCoinbase WHERE clave =?',('api_secret',))
    apiSecret=curBtc.fetchone()[0]
    curBtc.close()
    return [apiKey,apiSecret]

def actualizarPrecios(prezoCompra, prezoVenta, prezoSpot, tempo):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('INSERT OR IGNORE INTO Prezos (prezoCompra, prezoVenta, prezoSpot, tempo) VALUES(?,?,?,?)',(prezoCompra, prezoVenta, prezoSpot, tempo,))
    dbBtc.commit()
    curBtc.close()

def obterPrezoCompra(tempo):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('SELECT prezoCompra FROM Prezos WHERE tempo = ?',(tempo,))
    prezoCompra=curBtc.fetchone()[0]
    curBtc.close()
    return prezoCompra

def obterPrezoVenta(tempo):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('SELECT prezoVenta FROM Prezos WHERE tempo = ?',(tempo,))
    prezoVenta=curBtc.fetchone()[0]
    curBtc.close()
    return prezoVenta

def obterPrezoSpot(tempo):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('SELECT prezoSpot FROM Prezos WHERE tempo = ?',(tempo,))
    prezoSpot=curBtc.fetchone()[0]
    curBtc.close()
    return prezoSpot

def obterPrezos(tempo):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos dbBtc en: ' + db
    dbBtc = sqlite3.connect(db)
    curBtc = dbBtc.cursor()
    curBtc.execute('SELECT * FROM Prezos WHERE tempo = ?',(tempo,))
    prezos=curBtc.fetchone()
    curBtc.close()
    return prezos
