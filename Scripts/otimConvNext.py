import json
import os

#Escolha de Otimizador com Otimizaçao da Ordem de Grandeza do Learning Rate

fich = input('Nome Ficheiro de Output:')

with open(fich,"w") as o:
    o.write('#! /bin/bash \n')

    n = int(input('Nº de Epocas:'))
    otimList = ['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adamp', 'sgdp','adadelta','adafactor','adahessian','rmsprop','rmsproptf','novograd','nvnovograd']
    lrexpList = [4,5,6]
    #lrbase = 5
    
    for otim in otimList:
        for lrexp in lrexpList:
            comd = "python main.py --model convnext_base --drop_path 0.8 --input_size 224 --batch_size 32 --opt {} --lr 5e-{} --update_freq 2 --warmup_epochs 0 --epochs {} --weight_decay 1e-8  --layer_decay 0.7 --head_init_scale 0.001 --cutmix 0 --mixup 0 --finetune ../Checkpoints/convnext_base_22k_224.pth --data_path ../Datasets/padded --output_dir ../Results\n\n\n".format(otim,lrexp,n)
            o.write(comd)
        
