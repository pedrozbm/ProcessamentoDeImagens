import cv2
import tkinter as tk
from tkinter import filedialog

def abrir_imagem():
    filepath = filedialog.askopenfilename()
    imagem = cv2.imread(filepath)
    return imagem

def somar_imagens(imagem1, imagem2):
    if imagem1.shape != imagem2.shape:
        print("As imagens tem tamanhos diferentes. Nao eh possivel soma-las.")
        return None
    else:
        return cv2.add(imagem1, imagem2)


def equalizar_histograma(imagem):
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return equalized

def exibir_imagem(imagem, titulo):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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

if __name__ == "__main__":
    main()
