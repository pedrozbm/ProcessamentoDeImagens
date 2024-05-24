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
    

