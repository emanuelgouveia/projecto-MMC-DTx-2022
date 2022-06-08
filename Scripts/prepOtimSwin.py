import json
import os

#Escolha de Otimizador com Otimizaçao da Ordem de Grandeza do Learning Rate
otimList = ['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adadelta','rmsprop']
lrexpList = [4]

for otim in otimList:
        for lrexp in lrexpList:
            config = '{}_{}'.format(otim,lrexp)
            with open(config,"w") as conf:
                s = """MODEL:\n  TYPE: swin\n  NAME: {}_{}\n  DROP_PATH_RATE: 0.2\n  SWIN:\n    EMBED_DIM: 128\n    DEPTHS: [ 2, 2, 18, 2 ]\n    NUM_HEADS: [ 4, 8, 16, 32 ]\n    WINDOW_SIZE: 7\nTRAIN:\n  EPOCHS: 1\n  WARMUP_EPOCHS: 0\n  WEIGHT_DECAY: 1e-8\n  BASE_LR: 2e-0{}\n  WARMUP_LR: 2e-08\n  MIN_LR: 2e-0{}\n  OPTIMIZER: \n    NAME: {}""" .format(otim,lrexp,lrexp,lrexp+2,otim)      
                conf.write(s)