import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np



 
# Abre a janela do explorador de arquivos
print('Selecione a primeira imagem: ')

# Seleciona a primeira imagem
img_path1 = filedialog.askopenfilename()
img1 = cv2.imread(img_path1)
img1 = cv2.resize(img1, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

print("Arquivo selecionado:", img_path1)
# cv2.imshow('Imagem 1', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print('Selecione a segunda imagem: ')

# Seleciona a segunda imagem
img_path2 = filedialog.askopenfilename()
img2 = cv2.imread(img_path2)
img2 = cv2.resize(img2, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

print("Arquivo selecionado:", img_path2)
# cv2.imshow('Imagem 2', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

added = cv2.add(img1, img2)
cv2.imshow("added", added)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtraction = cv2.subtract(img1, img2)
cv2.imshow("subtract", subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()

multiplication = cv2.multiply(img1, img2) 
cv2.imshow("Multiplication", multiplication)
cv2.waitKey(0)
cv2.destroyAllWindows()

division = cv2.divide(img1, img2)
cv2.imshow("Division", division)
cv2.waitKey(0)  
cv2.destroyAllWindows()

imgand = cv2.bitwise_and(img1, img2)
cv2.imshow("And", imgand)
cv2.waitKey(0)  
cv2.destroyAllWindows()

imgor = cv2.bitwise_or(img1, img2)
cv2.imshow("Or", imgor)
cv2.waitKey(0)  
cv2.destroyAllWindows()

imnot = cv2.bitwise_not(img1, img2)
cv2.imshow("Not", imnot)
cv2.waitKey(0)  
cv2.destroyAllWindows()

imxor = cv2.bitwise_xor(img1, img2)
cv2.imshow("Xor", imxor)
cv2.waitKey(0)  
cv2.destroyAllWindows()

imagem_cinza = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
rostos = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
mascara = np.ones(imagem_cinza.shape[:2], dtype=np.uint8) * 255

for (x, y, w, h) in rostos:
    # Calcular o centro e o raio do círculo
    centro_x = x + w // 2
    centro_y = y + h // 2
    raio = min(w, h) // 2
    raio *= 1.5
    # Desenhar o círculo ao redor do rosto
    # cv2.circle(img1, (centro_x, centro_y), int(raio), (255, 0, 0), 2)
    
    cv2.circle(mascara, (centro_x, centro_y), int(raio), 0, -1)

# Inverter a máscara para obter uma máscara fora dos círculos dos rostos
mascara = cv2.bitwise_not(mascara)

# Aplicar a máscara para a imagem original
imagem_mascarada = cv2.bitwise_and(img1, img1, mask=mascara)

cv2.imshow('Imagem', imagem_mascarada)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
cv2.imshow('Rostos Detectados', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

