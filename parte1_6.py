import cv2
import matplotlib.pyplot as plt

#Ler a imagem
img = cv2.imread('lena.png')

#Separando as cores
B, G, R = cv2.split(img)
  
#Canal azul
cv2.imshow('Azul', B)

#Canal verde
cv2.imshow('Verde', G)

#Canal vermelho
cv2.imshow('Vermelho', R)

cv2.waitKey(0)