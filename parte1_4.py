import cv2
import matplotlib.pyplot as plt

#Ler a imagem
img = cv2.imread('lena.png')
#Convertendo em tons de cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Calculando histograma
histograma = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

#Plotando a imagem e comparações
plt.title('Histograma escala de cinza'), plt.plot(histograma), plt.xlim([0, 256])

plt.show()