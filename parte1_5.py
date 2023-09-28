import cv2
from matplotlib import pyplot as plt

#Ler imagem
img = cv2.imread('lena.png')

#Fazendo a equalização
canais = cv2.split(img)
canais_equalizados = []

for canal in canais:
    canal_equalizado = cv2.equalizeHist(canal)
    canais_equalizados.append(canal_equalizado)

img_equalizada = cv2.merge(canais_equalizados)

#Plotando a imagem
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1), plt.title('Imagem Original'), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2), plt.title('Imagem Equalizada'), plt.imshow(cv2.cvtColor(img_equalizada, cv2.COLOR_BGR2RGB))

plt.show()