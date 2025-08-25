import cv2
import numpy as np

tamanho_tabuleiro = 400
tamanho_quadrado = 50

tabuleiro = np.zeros((tamanho_tabuleiro, tamanho_tabuleiro,3), dtype=np.uint8)

cor1 = (255,255,255)
cor2 = (150,150,150)

for linha in range(8):
    for coluna in range (8):
        if(linha + coluna) % 2 ==0:
            cor = cor1
        else:
            cor = cor2
        
        x1 = linha * tamanho_quadrado
        y1 = coluna * tamanho_quadrado
        x2 = x1 + tamanho_quadrado
        y2 = y1 + tamanho_quadrado
        
        cv2.rectangle(tabuleiro, (x1,y1),(x2,y2), cor,-1)



cv2.imshow("Tabuleiro 400x400",tabuleiro)
cv2.waitKey(0)
cv2.destroyAllWindows()
