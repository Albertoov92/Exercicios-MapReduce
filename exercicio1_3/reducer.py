#!/usr/bin/python3

import sys

memo = 0
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
    
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey == None:
       oldKey = thisKey 
    if float(memo)<float(Precio):
        memo=float(Precio)
    if oldKey != thisKey:
        print(oldKey,"\t", memo)
        memo = 0
        oldKey = thisKey


# Escribe o último par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey,"\t", memo)