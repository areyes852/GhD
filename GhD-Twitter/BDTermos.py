# -*- coding: utf-8 -*-

import sqlite3
import os
db = 'db/dbTermo'

def crearBDTermos():
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()

    curTermo.execute('CREATE TABLE IF NOT EXISTS TermosTwitter (termo_id INTEGER PRIMARY KEY, termo TEXT UNIQUE, peso INTEGER)')

    curTermo.execute('CREATE TABLE IF NOT EXISTS ModificadorTermoTwitter (modificador_id INTEGER PRIMARY KEY, modificador TEXT UNIQUE, peso INTEGER, cariz INTEGER)')

    dbTermo.commit()
    curTermo.close()


def engadirTermo(termo, peso):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('INSERT OR IGNORE INTO TermosTwitter (termo, peso) VALUES(?,?)',(termo, peso))
    dbTermo.commit()
    curTermo.close()

def engadirModificador(modificador, peso, cariz):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('INSERT OR IGNORE INTO ModificadorTermoTwitter (modificador, peso, cariz,modificador_id) VALUES(?,?,?,0)',(modificador, peso, cariz))
    dbTermo.commit()
    curTermo.close()

def modificarPesoBDTermos(termo,peso):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('UPDATE TermosTwitter SET peso=? WHERE termo = ?',(peso,termo))
    dbTermo.commit()
    curTermo.close()

def modificarCarizBDTermos(modificador,cariz):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('UPDATE ModificadorTermoTwitter SET cariz=? WHERE modificador = ?',(modificador,cariz))
    dbTermo.commit()
    curTermo.close()

def engadirRelacionBDTermos(termo, modificador):
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('INSERT OR IGNORE INTO ModificadorTermoTwitter',(modificador,cariz))
    dbTermo.commit()
    curTermo.close()

def obterTermoDBTermos(termo):
    # TODO: Devolver os modificadores asociados a cada termo
    if not os.path.isfile(db):
        print 'Non se pode acceder á base de datos TermosTwitter en: ' + db
    dbTermo = sqlite3.connect(db)
    curTermo = dbTermo.cursor()
    curTermo.execute('SELECT * FROM TermosTwitter WHERE termo = ?',(termo,))
    return curTermo.fetchone()
