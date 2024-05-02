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
                           [1, -1,  1],
                           [1, 1, 1]])
    return cv2.filter2D(imagem, -1, filtro_sul)


def filtro_leste(imagem):
    filtro_leste = np.array([[-1, 1, 1],
                             [-1, -1, 1],
                             [-1, 1, 1]])
    return cv2.filter2D(imagem, -1, filtro_leste)


def filtro_oeste(imagem):
    filtro_oeste = np.array([[1, 1, -1],
                             [1, -1, -1],
                             [1, 1, -1]])
    return cv2.filter2D(imagem, -1, filtro_oeste)

def filtro_roberts(imagem):
    filtro_roberts_horizontal = np.array([[1, 0],
                                          [0, -1]], dtype=np.float32)
    filtro_roberts_vertical = np.array([[0, 1],
                                        [-1, 0]], dtype=np.float32)
    img_horizontal = cv2.filter2D(imagem, -1, filtro_roberts_horizontal)
    img_vertical = cv2.filter2D(imagem, -1, filtro_roberts_vertical)

    imagem_final = np.sqrt(np.square(img_horizontal)+np.square(img_vertical))
    imagem_final = np.clip(imagem_final, 0, 255).astype(np.uint8)
    return imagem_final

def filtro_sobel(imagem):
    filtro_sobel_x = np.array([[1, 2, 1],
                               [0, 0, 0],
                               [-1, -2, -1]], dtype=np.float32)

    filtro_sobel_y = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]], dtype=np.float32)

    img_filtrada_x = cv2.filter2D(imagem, -1, filtro_sobel_x)
    img_filtrada_y = cv2.filter2D(imagem, -1, filtro_sobel_y)
    imagem_bordas = np.sqrt(np.square(img_filtrada_x) + np.square(img_filtrada_y))
    imagem_bordas = np.clip(imagem_bordas, 0, 255).astype(np.uint8)
    return imagem_bordas

def filtro_passa_altas_agucamento(imagem, alpha=1.5, beta=-0.5):
    filtro_passa_altas = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]], dtype=np.float32)

    imagem_filtrada = cv2.filter2D(imagem, -1, filtro_passa_altas)

    imagem_agucada = cv2.addWeighted(imagem, alpha, imagem_filtrada, beta, 0)

    imagem_agucada = np.clip(imagem_agucada, 0, 255).astype(np.uint8)

    return imagem_agucada

def aplicar_filtro(imagem, filtro):
    if filtro == "Norte":
        return filtro_norte(imagem)
    elif filtro == "Sul":
        return filtro_sul(imagem)
    elif filtro == "Leste":
        return filtro_leste(imagem)
    elif filtro == "Oeste":
        return filtro_oeste(imagem)
    elif filtro == "Roberts":
        return filtro_roberts(imagem)
    elif filtro == "Sobel":
        return filtro_sobel(imagem)
    elif filtro == "Passa-altas agucamento":
        return filtro_passa_altas_agucamento(imagem)
    else:
        return imagem


def selecionar_filtro(imagem, filtro):
    imagem_processada = aplicar_filtro(imagem, filtro)
    exibir_imagem(imagem_processada, filtro)

def main():
    root = tk.Tk()
    root.title("Selecionar Filtro")

    botao_abrir = tk.Button(root, text="Abrir Imagem",
                            command=lambda: selecionar_filtro(abrir_imagem(), filtro_combobox.get()))
    botao_abrir.pack()

    filtros = ["Norte", "Sul", "Leste", "Oeste", "Roberts", "Sobel", "Passa-altas agucamento"]
    filtro_combobox = tk.StringVar()
    filtro_combobox.set(filtros[0])
    combobox = tk.OptionMenu(root, filtro_combobox, *filtros)
    combobox.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

