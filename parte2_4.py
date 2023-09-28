import cv2

#Ler a imagem em escala de cinza
img = cv2.imread('imagem.png', cv2.IMREAD_GRAYSCALE)

#Aplicando Canny para detectar bordas
bordas = cv2.Canny(img, threshold1=30, threshold2=100)  # Ajuste esses valores conforme necessário

#Plotando a imagem e comparação
cv2.imshow('Original', img)
cv2.imshow('Bordas', bordas)

cv2.waitKey(0)