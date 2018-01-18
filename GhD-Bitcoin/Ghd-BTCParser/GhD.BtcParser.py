# Bloque de exemplo: https://blockchain.info/block-height/502925
# Obter bloque: wget https://blockchain.info/block/0000000000000000002d61c048df6276791d18f92637a4ea94d3035ea8ea18e4?format=hex

import struct
import binascii
import array
from datetime import datetime

block = './blocks/block502925'
f = open(block, "r")

def leer(archivo,num_bytes):
    tam = int(num_bytes)
    bit=[]
    for i in range(0,tam):
        bit.append(f.read(2))
    bit.reverse()
    return ''.join(bit)

def leerCompactSize(archivo, pos):
    archivo.seek(pos)
    bts=leer(archivo,1)
    pos += 2
    if bts == 'fd':
        pos += 6
        return leer(f,2),pos
    if bts == 'fe':
        pos += 10
        return leer(f,4),pos
    if bts == 'ff':
        pos +=18
        return leer(f,8),pos
    return bts, pos

def num_trans(archivo):
    archivo.seek(160)
    numero1,posicionNum =leerCompactSize(archivo,160)
    return int(numero1,16),posicionNum

def coinbase_trans(archivo):
    archivo.seek(160)
    bts=leer(archivo,1)
    pos = 162
    if bts == 'fd':
        pos = 166
    if bts == 'fe':
        pos = 170
    if bts == 'ff':
        pos = 180
    archivo.seek(pos)
    fff=''
    while fff != "ffffffff" :
        pos +=1
        archivo.seek(pos)
        fff = leer(archivo,4)
    pos = archivo.tell() - 72
    archivo.seek(pos)
    coinbaseHas = leer(archivo, 32)
    coinbaseIndex = leer(archivo,4)

    coinbaseNumByts=leer(archivo,1)
    if coinbaseNumByts == 'fd':
        coinbaseNumByts = int(leer(f,2),16)
    if coinbaseNumByts == 'fe':
        coinbaseNumByts = int(leer(f,4),16)
    if coinbaseNumByts == 'ff':
        coinbaseNumByts = int(leer(f,8),16)
    pos =f.tell() + int(coinbaseNumByts) + 8
    print(pos)
    return coinbaseHas,coinbaseIndex, coinbaseNumByts, pos

def transaccion(archivo, posicion):
    archivo.seek(posicion)
    versionTx = leer(archivo,4)
    numInputTx,pos = leerCompactSize(archivo,posicion + 4)

    return int(versionTx,16),int(numInputTx,16),pos

try:
    version = leer(f,4)
    previousBlockHeaderHas = leer(f,32)
    merkleRootHas=leer(f,32)
    tempo=datetime.utcfromtimestamp(int(leer(f,4),16))
    nBits=int(leer(f,4),16)
    nonce = int(leer(f,4),16)
    num=num_trans(f)[0]
    coinHas, coinIndex, coinNum, posicion =coinbase_trans(f)
    vTx,nTx,posNext=transaccion(f,posicion)
finally:
    f.close()

#print()
# print(version)
# print(previousBlockHeaderHas)
# print(merkleRootHas)
# print(tempo)
# print(nBits)
# print(nonce)
# print(num)
# print(coinHas)
# print(coinIndex)
# print(coinNum)
print(posicion)
print(vTx)
print(nTx)


# from blockchain import util
# from blockchain import blockexplorer
# util.TIMEOUT = 5 #time out after 5 seconds
#
# latest_block = blockexplorer.get_latest_block()
# block = blockexplorer.get_block(latest_block.hash)
