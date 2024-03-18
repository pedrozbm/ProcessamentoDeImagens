import cv2
import tkinter as tk
from tkinter import filedialog

# Abre a janela do explorador de arquivos
print('Selecione a primeira imagem: ')

# Seleciona a primeira imagem
img_path1 = filedialog.askopenfilename()
img1 = cv2.imread(img_path1)
img1 = cv2.resize(img1, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

print("Arquivo selecionado:", img_path1)
cv2.imshow('Imagem 1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Selecione a segunda imagem: ')

# Seleciona a segunda imagem
img_path2 = filedialog.askopenfilename()
img2 = cv2.imread(img_path2)
img2 = cv2.resize(img2, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

print("Arquivo selecionado:", img_path2)
cv2.imshow('Imagem 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

added = cv2.add(img1, img2)
cv2.imshow("added", added)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtraction = cv2.subtract(img1, img2)
cv2.imshow("subtract", subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()


