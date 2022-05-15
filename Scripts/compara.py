import json
import os

#Comparação de Otim ConvNext


fich = input('Nome Ficheiro de Output:')

with open(fich,"w") as o:
    o.write('#! /bin/bash \n')

    otimList = ['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adamp', 'sgdp','adadelta','adafactor','rmsprop','rmsproptf','novograd','nvnovograd']
    lrexpList = [4,5,6]
    o.write('mkdir logs \n')
    for otim in otimList:
        for lrexp in lrexpList:
            o.write('mv {}_{}/log.txt {}_{}.txt\n'.format(otim,lrexp,otim,lrexp))
            o.write('cp {}_{}/{}_{}.txt logs\n'.format(otim,lrexp,otim,lrexp))