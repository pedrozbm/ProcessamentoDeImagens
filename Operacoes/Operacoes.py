import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

def load_image():
    root = tk.Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename()
    return cv2.imread(img_path)

def resize_image(image):
    return cv2.resize(image, dsize=(800, 800), interpolation=cv2.INTER_CUBIC)

def show_image(image, title='Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def operations(img1, img2):
    added = cv2.add(img1, img2)
    show_image(added, "Added")

    subtraction = cv2.subtract(img1, img2)
    show_image(subtraction, "Subtraction")

    multiplication = cv2.multiply(img1, img2) 
    show_image(multiplication, "Multiplication")

    division = cv2.divide(img1, img2)
    show_image(division, "Division")

    img_and = cv2.bitwise_and(img1, img2)
    show_image(img_and, "And")

    img_or = cv2.bitwise_or(img1, img2)
    show_image(img_or, "Or")

    img_not = cv2.bitwise_not(img1, img2)
    show_image(img_not, "Not")

    img_xor = cv2.bitwise_xor(img1, img2)
    show_image(img_xor, "Xor")

def detect_faces(img):
    imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    rostos = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    mascara = np.ones(imagem_cinza.shape[:2], dtype=np.uint8) * 255

    for (x, y, w, h) in rostos:
        centro_x = x + w // 2
        centro_y = y + h // 2
        raio = min(w, h) // 2
        raio *= 1.5
        cv2.circle(mascara, (centro_x, centro_y), int(raio), 0, -1)

    mascara = cv2.bitwise_not(mascara)
    imagem_mascarada = cv2.bitwise_and(img, img, mask=mascara)
    return imagem_mascarada

def main():
    print('PROCESSAMENTO DE IMAGENS')
    
    print('Selecione a primeira imagem:')
    img1 = load_image()
    img1 = resize_image(img1)

    print('Selecione a segunda imagem:')
    img2 = load_image()
    img2 = resize_image(img2)

    print('------------------------')
    print('[1] - EXIBIR IMAGENS ORIGINAIS')
    print('[2] - APLICAR OPERACOES:')
    print('[3] - DETECTAR ROSTOS DA PRIMEIRA IMAGEM')
    
    match int(input()):
        case 1:
           show_image(img1, "Image 1")
           show_image(img2, "Image 2")
        case 2:           
            operations(img1, img2)
        case 3: 
            img1_faces_detected = detect_faces(img1)
            show_image(img1_faces_detected, "Faces Detected")
    

if __name__ == "__main__":
    main()
