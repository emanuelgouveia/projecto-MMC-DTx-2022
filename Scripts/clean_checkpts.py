import os

#Remoção dos checkpoints extras

with open('clean_checkpoints.sh',"w") as o:
    o.write('#! /bin/bash \n')
    otimList = ['sgd', 'adam']
    #['sgd', 'adam', 'adamw', 'nadam', 'radam', 'adadelta','rmsprop']
    lrexpList = [4,5]
    for otim in otimList:
        for lrexp in lrexpList:
            model = "{}_{}".format(otim,lrexp)
            comd = "cd {}/\n".format(model)
            o.write(comd)
            o.write("cd default/\n")
            for x in range(99):
                comd = " rm ckpt_epoch_{}.pth\n".format(x)
                o.write(comd)
            o.write("cd ../../../output/\n")
