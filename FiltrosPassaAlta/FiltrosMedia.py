import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

def abrir_imagem():
    filepath = filedialog.askopenfilename()
    imagem = cv2.imread(filepath)
    imagem = resize_image(imagem)
    return imagem
def resize_image(imagem):
    return cv2.resize(imagem, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)
def exibir_imagem(imagem, title='Image'):
    cv2.imshow(title, imagem)
    cv2.waitKey(0)

def filtro_norte(imagem):
    filtro_norte = np.array([[1, 1, 1],
                             [ 1,  -1,  1],
                             [ -1,  -1,  -1]])
    return cv2.filter2D(imagem, -1, filtro_norte)

def filtro_sul(imagem):
    filtro_sul = np.array([[-1, -1, -1],
                           [1, 1,  1],
                           [1, 1, 1]])
    return cv2.filter2D(imagem, -1, filtro_sul)

def main():
    # Criar a janela da GUI
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Abrir a primeira imagem
    print("Selecione a primeira imagem:")
    imagem1 = abrir_imagem()

    exibir_imagem(imagem1, "imagem original")

    # n = int(input("digite a media do filtro"))
    #
    # filter = np.ones((n, n), np.float32) / (n*n)
    # filtered_image = cv2.filter2D(imagem1, -1, filter)
    # cv2.imshow("imagem com filtro", filtered_image)

    imagem_filtroNorte = filtro_sul(imagem1)
    cv2.imshow("imagem filtro norte", imagem_filtroNorte)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()

