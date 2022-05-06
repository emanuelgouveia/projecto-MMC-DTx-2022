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
            o.write("mkdir {}_{}".format(otim,lrexp))
            comd = "python main.py --model convnext_base --drop_path 0.8 --input_size 224 --batch_size 32 --opt {} --lr 5e-{} --min_lr 1e-{} --update_freq 2 --warmup_epochs 0 --epochs {} --weight_decay 1e-8  --layer_decay 0.7 --head_init_scale 0.001 --cutmix 0 --mixup 0 --finetune ../Checkpoints/convnext_base_22k_224.pth --data_path ../Datasets/padded --nb_classes 196 --output_dir ../Results/OtimConvNext/{}_{}\n\n\n".format(otim,lrexp,lrexp+1,n,otim,lrexp)
            o.write(comd)
        
