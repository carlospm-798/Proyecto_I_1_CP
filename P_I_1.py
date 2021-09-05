#Carlos Paredes Márquez
#Proyecto integrador 1
#04 09 2021

''' Escribir un programa que identifique el tipo de
    exposicxión de una imagen <normal, sub o expuesta>. '''

import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("Travieso_Scott.jpg")
if im.size > 1000 * 600:
    im = cv2.resize(im, None, fx=0.5, fy=0.5)

ig = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
[M,N] = ig.shape[0:2]

hist = cv2.calcHist([ig],[0],None,[5],[0,256]).flatten()/(M*N)

'''Calcular exposición de la imagen'''

maxElement = np.argmax(hist)
if maxElement == 4 and hist[4] > 0.3:
    print('Imagen sobreexpuesta')
    cv2.putText(ig, 'Imagen sobreexpuesta', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 5)
    im_eq = cv2.equalizeHist(ig)
    cv2.putText(im_eq, 'CP', (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 5)
    cv2.imshow("imagen ecualizada", im_eq)
    #
elif maxElement == 0 and hist[0] > 0.3:
    print('Imagen subexpuesta')
    cv2.putText(ig, 'Imagen subexpuesta', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 5)
    im_eq = cv2.equalizeHist(ig)
    cv2.putText(im_eq, 'CP', (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 5)
    cv2.imshow("Imagen ecualizada", im_eq)
    #
else:
    print('Buena exposición')
    cv2.putText(ig, 'expuesta normal', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 5)

cv2.putText(im, 'CP', (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 5)

cv2.imshow('image0',im)

fig= plt.figure()
plt.bar(range(len(hist)),hist)
plt.show()