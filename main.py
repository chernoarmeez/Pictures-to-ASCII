import cv2
import os
folder = 'pic'
file = open('sas.txt','w')
symbols = ['.',':','=','<','c','z','T','J','F','C','I','t','n','x',']','E','q','6','d','O','U','H','8','$','M','@']
for i in os.listdir(folder):
    cb_img = cv2.imread(folder+'/'+i, 0)
    weight = cb_img.shape[0]
    height = cb_img.shape[1]
    for i in range(weight):
        for j in range (height):
            file.write(symbols[int(cb_img[i,j]/10)]*3)
        file.write('\n')
file.close()