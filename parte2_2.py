import cv2
import numpy as np
from matplotlib import pyplot as plt

#Ler a imagem
img = cv2.imread('imagem.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Aplicando a remoção
kernel = np.ones((14,14),np.uint8)
remocao = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#Plotando a imagem e comparações
fig, ax = plt.subplots(ncols=2,figsize=(15,5))
ax[0].imshow(img), ax[0].set_title('Imagem Original')
ax[1].imshow(remocao), ax[1].set_title('Remoção dos objetos pretos')

plt.show()