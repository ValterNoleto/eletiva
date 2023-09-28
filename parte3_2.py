import cv2
import numpy as np

#Ler a imagem em escala de cinza
imagem = cv2.imread('coins.png', cv2.IMREAD_GRAYSCALE)

#Aplicando o filtro Sobel
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)

#Combinando as respostas dos filtros Sobel
bordas = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

#Exibindo a imagem das bordas
cv2.imshow('Bordas Sobel', bordas)

#Definindo os kernels do filtro Prewitt
kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

#Aplicando kernels
prewitt_x = cv2.filter2D(imagem, -1, kernel_prewitt_x)
prewitt_y = cv2.filter2D(imagem, -1, kernel_prewitt_y)

#Combinando as respostas dos filtros Prewitt
bordas = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

#Plotando a imagem
cv2.imshow('Bordas Prewitt', bordas)

cv2.waitKey(0)