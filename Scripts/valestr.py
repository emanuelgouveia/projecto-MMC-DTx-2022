import json
import os

#Estrutura da pasta Val
with open("estruturadataset.txt","w") as o:
    n = 14567 #numero de imagens
    o.write('#! /bin/bash \n')
    dic = json.load(open("/home/alpr/MMC/projecto-MMC-DTx-2022/stanford_train.json"))
    lab = dic["labels"]
    for l in set(lab):
        s = "mkdir /home/alpr/MMC/Datasets/padded/val/{:06} \n".format(l)
        o.write(s)


    for x in range(n):
        sourc = x          
        dest = lab[x]       
        cont = 0 
        past = 0

        if(cont<8):
            s = "mv /home/alpr/MMC/Datasets/padded/train/{:06}/{:06}.jpg /home/alpr/MMC/Datasets/padded/val/{:06} \n".format(dest,sourc,dest)
            s = s+1
            o.write(s)

        cont = cont+1

        if(dest>past):
            cont = 0
            past = dest