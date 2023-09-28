import cv2
from matplotlib import pyplot as plt

#Ler a imagem
img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Redimensionamento
img_metade = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
img_maior = cv2.resize(img, (1500, 1500))
#Criação das legendas
Titles = ['Original', 'Metade', 'Maior']
images = [img, img_metade, img_maior]
count = 3

#Plotando a imagem e comparações
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()