import cv2

#Ler a imagem
img = cv2.imread('lena.png')
#Conversão HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Plotando a imagem e comparações
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem HSV', hsv_img)

cv2.waitKey(0)