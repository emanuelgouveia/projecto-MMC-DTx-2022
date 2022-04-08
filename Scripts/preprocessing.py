#Pré Processamento do Dataset

import torch
from PIL import Image 
import torchvision.transforms as T
import json
import os

n = 486  #numero de imagens

for x in range(n):
    #paths de origem e destino das img
    orig = '/home/br99/Desktop/PI/dataset/original/{:06}.jpg'.format(x)    
    dest = '/home/br99/Desktop/PI/dataset/padded/{:06}.jpg'.format(x)   
    print(orig)
    
    orig_img = Image.open(orig)

    w, h = orig_img.size  #width, height da img

    dif = 0
    if(w>h):
        dif = w-h
        if (dif%2==0):
            wh = [0,dif//2]
        else:
            wh = [0,(dif//2)+1,0,dif//2]
        new_img = T.Pad(wh)(orig_img)

    if(h>w):
        dif = h-w
        if (dif%2==0):
            wh = [dif//2,0]
        else:
            wh = [(dif//2)+1,0,(dif//2),0]
        new_img = T.Pad(wh)(orig_img)

    if(h==w): new_img = orig_img
    
    new_img.save(dest)

#!!! Otimização com cor de fundo 