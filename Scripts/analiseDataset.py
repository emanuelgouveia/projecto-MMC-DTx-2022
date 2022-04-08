import json
import os
import matplotlib.pyplot as plt


dic = json.load(open("/home/br99/Desktop/stanford_train.json"))
lab = dic["labels"]
val = []
    #[0,0,0,0,0,....,0,0,0,0,1,1,1,1,1,1,....]
i = 0
for l in lab:
    val.append(l)
    i = i+1
print(val)


#Tamanho do DataSet
tamanho = len(val)
print(tamanho)

#Numero de Classes
classes = [] #[0,1,2,3,4...,195]
for c in set(lab):
    classes.append(c)
numClas = len(classes)
print(numClas)



#Distribuição do Dataset
dist = [] #[67,65,...]
cnt = 0
cont = 0
for x in val:
    if(x>cnt):
        cnt = cnt + 1
        dist.append(cont)
        cont = 0
    cont = cont + 1 
print(dist)


plt.plot(dist)
plt.show()

dist.sort()
print(dist)

plt.bar(dist,width=0.4)
plt.show()

dist.sort(reverse=True)
print(dist)

plt.bar(dist)
plt.show()
