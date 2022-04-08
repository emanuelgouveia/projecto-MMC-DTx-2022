#resize de imagens

import torch
from PIL import Image 
import torchvision.transforms as T

orig_img = Image.open('/home/br99/Desktop/teste/000000.JPEG')

resized_img = T.Resize(size=(224,224))(orig_img) 

resized_img.save('/home/br99/Desktop/teste/nova.JPEG')


#opçao cortar -> maior resoluçao perda de informaçao
#opçao acrescentar -> menor resoluçao preserva informaçao
