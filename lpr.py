#pip install opencv-python

import cv2
import pytesseract

# Cargar la imagen
img = cv2.imread('placa3.jpg')


# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Aplicar filtros (ajusta los valores según la imagen)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)[1]

# Detectar contornos
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Filtrar contornos (ajusta los valores según el tamaño de la placa)
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)

    if w > 50 and h > 20:
        # Aislar la región de la placa
        plate = gray[y:y+8*h, x+10:x+w]
        print(x,y,w,h)
        cv2.imshow('Placa', plate)
     
      
        # Aplicar OCR
        #text = pytesseract.image_to_string(plate, config='--psm 7')
        #pytesseract.pytesseract.tesseract_cmd = 'C:\Archivos de Programa\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(plate, config='--psm 7')
        print("Placa:", text)

        # Dibujar un rectángulo alrededor de la placa
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) 

# Mostrar la imagen resultante
cv2.imshow('Placa', img)
cv2.waitKey(0)
cv2.destroyAllWindows()