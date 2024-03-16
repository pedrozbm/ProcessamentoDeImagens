import cv2
import numpy as np

#abrindo a imagem
imagem_original = cv2.imread('AnzaiLogo.png')


# Imagem original
cv2.imshow('Imagem Original', imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escrevendo o nome
nome = "Pedro"
fonte = cv2.FONT_HERSHEY_SIMPLEX
cor = (0, 0, 0)
espessura = 2
tamanho = 1
posicao = (30, 30)
imagem_com_nome = imagem_original.copy()
cv2.putText(imagem_com_nome, nome, posicao, fonte, tamanho, cor, espessura)
# Mostrando 
cv2.imshow('Imagem com Nome', imagem_com_nome)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Converter para matriz
matriz_imagem = imagem_original.tolist()
print("Matriz da imagem:")
print(matriz_imagem)
# Convertendo a imagem em escala de cinza
imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

# Mostrando a imagem em escala de cinza
cv2.imshow('Imagem em Escala de Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Invertendo a posição da imagem
imagem_invertida = cv2.flip(imagem_original, 1) # 1 para inverter horizontalmente

# Mostrando a imagem invertida
cv2.imshow('Imagem Invertida', imagem_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()
