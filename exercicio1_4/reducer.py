#!/usr/bin/python3

import sys

memo = {}
lista=[]
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue


    thisKey, Precio = data_mapped
    if oldKey == None:
        oldKey = thisKey
    if oldKey==thisKey:
        lista.append(Precio)
    if oldKey != thisKey:
        memo.update({oldKey : lista})
        lista=[]
        oldKey= thisKey

memo.update({oldKey : lista})
max = 0

for tarjetas, valores in memo.items():

    for i in range(len(valores)):
        valores[i]=float(valores[i])
        if valores[i]>max:
            max=valores[i]
    memo.update({tarjetas : max})
    max = 0
maximo = 0

maxiTar=None
for maxTar, maxVal in memo.items():
    maxVal=float(maxVal)
    if maxVal>maximo:
        maximo=maxVal
        maxiTar=maxTar
print(maxiTar, "\t", maximo)
