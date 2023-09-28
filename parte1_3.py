import cv2
from matplotlib import pyplot as plt

#Ler imagem
img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Calculando histograma
cores  = ('b', 'g', 'r')
for i, color in enumerate(cores):
    histograma = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histograma, color = color)
    plt.xlim([0, 256])

plt.title('Histograma colorido')

plt.show()