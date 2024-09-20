# bibliotecas: opencv, sys (system)
import cv2 as cv
import sys

# abre uma imagem
img = cv.imread(cv.samples.findFile("images/papao.jpg"))

# verifica se a imagem está vazia e mostra a mensagem de erro
if img is None:
    print("Não foi possível abrir a imagem")

# mostra a imagem
cv.imshow("Display", img)

# aguarda uma ação de uma tecla e armazena o valor da tecla
k = cv.waitKey(1) # 0 significa indefinidamente; outros valores representam um "timer"

# se a tecla pressionada for s, salva a imagem como .png
if k == ord("s"):
    cv.imwrite("images/papao.png", img)
