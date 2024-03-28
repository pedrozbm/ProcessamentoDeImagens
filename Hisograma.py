import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Fun��o para abrir uma imagem usando a interface gr�fica do usu�rio
def abrir_imagem():
    filepath = filedialog.askopenfilename()
    imagem = cv2.imread(filepath)
    return imagem

# Fun��o para somar duas imagens
def somar_imagens(imagem1, imagem2):
    if imagem1.shape != imagem2.shape:
        print("As imagens t�m tamanhos diferentes. N�o � poss�vel som�-las.")
        return None
    else:
        return cv2.add(imagem1, imagem2)

# Fun��o para equalizar o histo
# 
# grama de uma imagem
def equalizar_histograma(imagem):
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return equalized

# Fun��o para exibir uma imagem em uma janela separada
def exibir_imagem(imagem, titulo):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Fun��o principal
def main():
    # Criar a janela da GUI
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Abrir a primeira imagem
    print("Selecione a primeira imagem:")
    imagem1 = abrir_imagem()

    # Abrir a segunda imagem
    print("Selecione a segunda imagem:")
    imagem2 = abrir_imagem()

    # Somar as imagens
    imagem_soma = somar_imagens(imagem1, imagem2)

    if imagem_soma is not None:
        # Equalizar o histograma da imagem resultante
        imagem_equalizada = equalizar_histograma(imagem_soma)

        # Exibir as imagens
        exibir_imagem(imagem1, "Imagem 1")
        exibir_imagem(imagem2, "Imagem 2")
        exibir_imagem(imagem_soma, "Imagem Soma")
        exibir_imagem(imagem_equalizada, "Imagem Equalizada")

# Executar a fun��o principal
if __name__ == "__main__":
    main()
