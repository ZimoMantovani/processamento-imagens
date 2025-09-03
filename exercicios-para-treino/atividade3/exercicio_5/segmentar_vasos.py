# 5) Segmentar apenas os vasos na figura 5 usando a técnica de
# conectividade-8 em cada canal R, G e B:
import cv2
import numpy as np
# lê uma imagem
imagem = cv2.imread('C:\\Users\\smantovani\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade3\\exercicio_5\\imagem 5.jpg')

if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho e o nome do arquivo.")
else:
    azul, verde, vermelho = cv2.split(imagem)
    
    _, mascara_azul = cv2.threshold(azul, 150, 255, cv2.THRESH_BINARY_INV)
    _, mascara_verde = cv2.threshold(verde, 150, 255, cv2.THRESH_BINARY_INV)
    _, mascara_vermelho = cv2.threshold(vermelho, 150, 255, cv2.THRESH_BINARY_INV)

    mascara_final = cv2.bitwise_or(mascara_azul, mascara_verde)
    mascara_final = cv2.bitwise_or(mascara_final, mascara_vermelho)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mascara_final, 8, cv2.CV_32S)

    vasos_segmentados = np.zeros_like(imagem)

    for i in range(1, num_labels):
        cor = np.random.randint(0, 255, size=3).tolist()
        vasos_segmentados[labels == i] = cor


    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Vasos Segmentados', vasos_segmentados)

    cv2.waitKey(0)
    cv2.destroyAllWindows()