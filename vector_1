#Пропорцианальное сжатие картинки в пространство поля для полета // не импользуется как основное
import cv2
from glob import glob
import numpy as np
from numpy import *
def pp():
    image = cv2.imread('kek.jpg', cv2.IMREAD_COLOR)
    mas = image.shape
    n = mas[1]/mas[0]
    h = 30
    w = h*n
    resize_img = cv2.resize(image, (int(w), int(h)))
    print(w, h)
    image_new = []
    mas = resize_img.shape
    for i in range(mas[0]):
        image_new.append([])
        for n in range(mas[1]):
            if np.sum(resize_img[i][n]) >= 255:
                image_new[i].append(0)
            else:
                image_new[i].append(1)
    for i in range(len(image_new)):
        for j in range(len(image_new[i])):
            print(image_new[i][j], end = ' ')
        print('\n')
    return(image_new)
