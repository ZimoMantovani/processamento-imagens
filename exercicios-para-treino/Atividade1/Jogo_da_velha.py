import cv2
import numpy as np



imagem = np.ones((300,300,3), dtype=np.uint8) * 255 # 255 deixa a tela branca

cor_linha = (0,0,0) # preta
cor_x = (255,0,0)
cor_bola = (0,0,255)
espessura = 5

cv2.line(imagem, (100,0),(100,300),cor_linha,espessura)
cv2.line(imagem, (200,0),(200,300),cor_linha,espessura)
cv2.line(imagem, (0,100),(300,100),cor_linha,espessura)
cv2.line(imagem, (0,200),(300,200),cor_linha,espessura)

#X
cv2.line(imagem, (25,25),(75,75),cor_x,espessura)
cv2.line(imagem, (25,75),(75,25),cor_x,espessura)   

cv2.line(imagem, (225,25),(275,75),cor_x,espessura)
cv2.line(imagem, (225,75),(275,25),cor_x,espessura) 

cv2.line(imagem, (25,225),(75,275),cor_x,espessura)
cv2.line(imagem, (25,275),(75,225),cor_x,espessura) 

cv2.line(imagem, (225,275),(275,225),cor_x,espessura)   
cv2.line(imagem, (225,225),(275,275),cor_x,espessura)

#0
cv2.circle(imagem,(150,150),35,cor_bola,espessura)
cv2.circle(imagem,(150,50),35,cor_bola,espessura)
cv2.circle(imagem,(50,150),35,cor_bola,espessura)
cv2.circle(imagem,(250,150),35,cor_bola,espessura)
cv2.circle(imagem,(150,250),35,cor_bola,espessura)



cv2.imshow("Tabuleiro 300x300",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
