# -*- coding: utf-8 -*-

import sys
import os
import twitter
import sqlite3
from BDConfiguracion import *
from BDTermos import *
from BDTwitter import *
twtt = twitter.Api()#

# crearBDTermos()
# engadirTermo('bitcoin',1)
# engadirTermo('bitcoins',1)
# engadirTermo('precio',1)
# engadirTermo('prizes',1)
# engadirTermo('cost',1)
# engadirModificador('subir',2,1)
# engadirModificador('rise',2,1)
# engadirModificador('up',2,1)
# engadirModificador('bajar',3,-1)
# engadirModificador('down',2,-1)
#
# crearBDTwitter()
# engadirContaBDTwitter('@proba1',1,10,'FALSE','EUROPE',1)
# engadirContaBDTwitter('@proba2',2,20,'TRUE','EUROPE',-1)
# id1 = obterIDContaBDTwitter('@proba1')
# id2 = obterIDContaBDTwitter('@proba2')
# print "Conta 1:" + str(id1)
#
# modificarReputacionContaBDTwitter(id1,3)
# modificarSeguidoresContaBDTwitter(id1,4)
# modificarVerificadoContaBDTwitter(id1,'TRUE')
# modificarRexionContaBDTwitter(id1,'CHINA')
# modificarCarizXeralContaBDTwitter(id1,1)
#
# print obterContaBDTwitter(id1)
# print '*****************************'
# print obterContaBDTwitter('@proba2')
# print '*****************************'
