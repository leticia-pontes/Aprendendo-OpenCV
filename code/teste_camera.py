import numpy as np
import cv2 as cv

camera = cv.VideoCapture(0)
# camera = cv.VideoCapture("videos/gif.avi")

# se não conseguir abrir a câmera, encerra o programa
if not camera.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

# captura a imagem continuamente
while True:

    # status da leitura e frame 
    reading, frame = camera.read()

    if not reading:
        print("Não foi possível receber o frame. Encerrando...")
        break

    # altera a resolução do frame
    # reading = camera.set(cv.CAP_PROP_FRAME_WIDTH,320)
    # reading = camera.set(cv.CAP_PROP_FRAME_HEIGHT,240)

    # inverte a imagem
    frame = cv.flip(frame, 90)

    # converte para escala cinza
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    colored = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # gera o negativo da imagem
    colored_negative = abs(255-colored)

    # mostra o resultado
    cv.imshow("Captura", abs(255-frame))

    if cv.waitKey(1) == ord("q"):
        break

print(camera.get(cv.CAP_PROP_FRAME_WIDTH), camera.get(cv.CAP_PROP_FRAME_HEIGHT))

camera.release()
cv.destroyAllWindows()
