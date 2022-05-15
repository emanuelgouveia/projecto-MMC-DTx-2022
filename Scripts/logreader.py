import json
import os
import numpy as np

#Leitura de Logs

otimList = ['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adamp', 'sgdp','adadelta','adafactor','rmsprop','rmsproptf','novograd','nvnovograd']
lrexpList = [4,5,6]

accuracy = []
trainlosses = []
testlosses = []
maxacu = []

for otim in otimList:
        for lrexp in lrexpList:
            log = open("{}_{}.txt".format(otim,lrexp))
            epcs = log.readlines()
            list = []
            for epc  in epcs:
                list.append(json.loads(epc))
            accur = []
            trainloss = []
            testloss = []

            for dic in list:
                accur.append(dic['test_acc1'])
                trainloss.append(dic['train_loss'])
                testloss.append(dic['test_loss'])

            accuracy.append(accur)
            trainlosses.append(trainloss)
            testlosses.append(testloss)
            maxacu.append(argmax(accur))

print('Accuracy:\n')
print(accuracy)
print('\nLoss (treino):\n')
print(trainlosses)
print('\nLoss (teste):\n')
print(testlosses)
print('\nMelhor Resultado:\n')
print(maxacu)