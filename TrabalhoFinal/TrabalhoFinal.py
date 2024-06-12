import cv2
import numpy as np
from scipy.signal import wiener
import tkinter as tk
from tkinter import filedialog

# Funções de filtro
def aplicar_filtro_passa_baixa(imagem):
    imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)
    return imagem_suavizada

def aplicar_filtro_passa_alta(imagem):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    imagem_passa_alta = cv2.filter2D(imagem, -1, kernel)
    return imagem_passa_alta

def aplicar_filtro_mediana(imagem):
    imagem_mediana = cv2.medianBlur(imagem, 5)
    return imagem_mediana

def aplicar_filtro_sobel(imagem):
    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    sobel = cv2.convertScaleAbs(magnitude)
    return sobel

def aplicar_filtro_wiener(imagem):
    imagem_wiener = wiener(imagem)
    return imagem_wiener

def aplicar_transformada_fourier(imagem):
    dft = cv2.dft(np.float32(imagem), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    return np.uint8(magnitude_spectrum)

# Função para abrir e redimensionar imagem
def abrir_imagem():
    root = tk.Tk()
    root.withdraw()  # Fechar a janela principal do Tkinter
    filepath = filedialog.askopenfilename()
    imagem = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if imagem is not None:
        imagem = resize_image(imagem)
    return imagem

def resize_image(imagem):
    return cv2.resize(imagem, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

# Função para exibir imagem
def exibir_imagem(imagem, title='Image'):
    cv2.imshow(title, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função principal
def main():
    # Abrir imagem usando o explorador de arquivos
    imagem_original = abrir_imagem()
    
    if imagem_original is None:
        print("Nenhuma imagem foi carregada.")
        return

    # Aplicar filtros
    imagem_suavizada = aplicar_filtro_passa_baixa(imagem_original)
    imagem_passa_alta = aplicar_filtro_passa_alta(imagem_suavizada)
    imagem_mediana = aplicar_filtro_mediana(imagem_passa_alta)
    imagem_sobel = aplicar_filtro_sobel(imagem_mediana)
    imagem_wiener = aplicar_filtro_wiener(imagem_mediana)
    imagem_fourier = aplicar_transformada_fourier(imagem_wiener)

    # Exibir resultados
    exibir_imagem(imagem_original, title='Imagem Original')
    exibir_imagem(imagem_suavizada, title='Imagem com Filtro Passa-Baixa')
    exibir_imagem(imagem_passa_alta, title='Imagem com Filtro Passa-Alta')
    exibir_imagem(imagem_mediana, title='Imagem com Filtro de Mediana')
    exibir_imagem(imagem_sobel, title='Imagem com Filtro de Sobel')
    exibir_imagem(imagem_wiener, title='Imagem com Filtro de Wiener')
    exibir_imagem(imagem_fourier, title='Imagem com Transformada de Fourier')

if __name__ == "__main__":
    main()
5
