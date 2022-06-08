import json
import os

#Escolha de Otimizador com Otimizaçao da Ordem de Grandeza do Learning Rate

fich = input('Nome Ficheiro de Output:')

with open(fich,"w") as o:
    o.write('#! /bin/bash \n')

    n = int(input('Nº de Epocas:'))
    otimList = ['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adadelta','rmsprop']
    lrexpList = [4]
    
    for otim in otimList:
        for lrexp in lrexpList:
            o.write("mkdir {}_{}\n".format(otim,lrexp))
            comd = "python -m torch.distributed.launch --nproc_per_node 1 --master_port 12345 main.py --cfg configs/{}_{}.yaml --pretrained ../Checkpoints/swin_base_patch4_window7_224_22k.pth --data-path ../Datasets/padded --batch-size 32 --accumulation-steps 2\n\n".format(otim,lrexp)
            o.write(comd)
        
