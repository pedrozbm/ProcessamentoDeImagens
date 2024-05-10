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

def prewitt_filter(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    horizontal_edges = cv2.filter2D(gray_image, -1, kernel_x)
    
    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])
    vertical_edges = cv2.filter2D(gray_image, -1, kernel_y)
    
    edges = cv2.addWeighted(horizontal_edges, 0.5, vertical_edges, 0.5, 0)
    
    return edges

def canny_edge_detection(image, min_threshold, max_threshold):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray_image, min_threshold, max_threshold)
    
    return edges

def laplacian_edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    
    laplacian = cv2.convertScaleAbs(laplacian)
    
    return laplacian

image = abrir_imagem():

# edges = prewitt_filter(image)
# edges = canny_edge_detection(image, min_threshold, max_threshold)
# edges = laplacian_edge_detection(image)



cv2.imshow('Original', image)
cv2.imshow('Prewitt Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()