import cv2
import numpy as np
# lê uma imagem
imagem = cv2.imread('C:\\Users\\smantovani\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade2\\ipe_roxo.jpg')

if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho e o nome do arquivo.")
else:
    #cv2.imshow("Imagem Original", imagem)
    recorte = imagem[100:100+320, 100:100+300]
    
   # cria uma máscara do mesmo tamanho do recorte, inicialmente preta
    mascara = np.zeros(recorte.shape[:2], dtype=np.uint8)

    cv2.circle(mascara,(160,50),40,255,-1)
    cv2.rectangle(mascara,(120,100),(200,180),255,-1)
    cv2.rectangle(mascara,(60,200),(260,280),255,-1)
    
    
    resultado = cv2.bitwise_and(recorte, recorte, mask=mascara)

    espelhamento_vertical = cv2.flip(resultado,0)
    
    cv2.imshow("Recorte da imagem", resultado)
    cv2.imshow("Flip Vertical", espelhamento_vertical)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

