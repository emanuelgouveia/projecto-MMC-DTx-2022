import json
import os

with open("estruturadataset.txt","w") as o:
    n = 4 #numero de imagens
    o.write('#! /bin/bash \n')
    dic = json.load(open("/home/br99/Desktop/teste/jsonteste.json"))
    lab = dic["labels"]
    for l in set(lab):
        s = "mkdir /home/br99/Desktop/teste/{:06} \n".format(l)
        o.write(s)
    for x in range(n):

        sourc = x
        dest = lab[x]
        s = "mv /home/br99/Desktop/teste/{:06}.JPEG /home/br99/Desktop/teste/{} \n".format(sourc,dest)
        o.write(s)