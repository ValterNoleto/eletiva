import cv2
import numpy as np
from matplotlib import pyplot as plt

#Ler a imagem
img = cv2.imread('imagem.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Aplicando o preenchimento
kernel = np.ones((10,10),np.uint8)
preenchimento = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#Plotando a imagem e comparações
fig, ax = plt.subplots(ncols=2,figsize=(15,5))
ax[0].imshow(img), ax[0].set_title('Imagem Original')
ax[1].imshow(preenchimento), ax[1].set_title('Pontos preenchidos')

plt.show()