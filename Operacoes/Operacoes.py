
import numpy as np
import cv2
import tkinter as tk
from PIL import ImageOps
from tkinter import filedialog


# Abre a janela do explorador de arquivos
img = filedialog.askopenfilename()
print("Arquivo selecionado:", img)

# testando
for i in (1, 2, 3, 8):
    Bitsimg = ImageOps(img, bits =i)
    Bitsimg.show()
    


