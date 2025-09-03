#  4-a) Criar uma imagem na cor preta de 301 x 301 de dimensão utilizando os três canais R, G e B.
#  a) encontre o ponto central da imagem
#  b) calcule a partir do centro na cor verde a 𝐷଼ ≤ 150
#  c) calcule a partir do centro na cor amarela a 𝐷ସ ≤ 150
#  D) calcule a partir do centro na cor azul a 𝐷௘ ≤ 100

import cv2
import numpy as np

tamanho = 301
espessura = 5

imagem = np.zeros((tamanho,tamanho,3), dtype=np.uint8)

meio = tamanho // 2
centro_x, centro_y = meio, meio

cv2.circle(imagem,(meio,meio),1,(0,0,255),espessura)
y_indices, x_indices = np.indices((tamanho, tamanho))

# Desenha um quadrado amarelo (usando a distância D8)
dist_8 = np.maximum(np.abs(x_indices - centro_x), np.abs(y_indices - centro_y))
imagem[dist_8 <= 150] = [0, 255, 255] # Amarelo

# Desenha um losango verde (usando a distância D4)
dist_4 = np.abs(x_indices - centro_x) + np.abs(y_indices - centro_y)
imagem[dist_4 <= 150] = [0, 255, 0] # Verde

# Desenha um círculo azul (usando a distância Euclidiana)
dist_e = np.sqrt((x_indices - centro_x)**2 + (y_indices - centro_y)**2)
imagem[dist_e <= 100] = [255, 0, 0] # Azul

# Mostra a imagem na tela
cv2.imshow("Formas Coloridas", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

