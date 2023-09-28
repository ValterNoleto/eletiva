import cv2
from matplotlib import pyplot as plt

#Ler a imagem
img = cv2.imread('lena_ruido.png')

#Aplicando filtro Mediana
mediana = cv2.medianBlur(img, 5)

#Plotando a imagem e comparações
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(mediana), plt.title('Mediana')

plt.show()