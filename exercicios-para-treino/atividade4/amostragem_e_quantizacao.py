# 1) Pesquise uma imagem colorida na qual há presença de um câncer de pele.
# a)Transforme a imagem em nível de cinza
# b)Aplique a equalização da imagem em nível de cinza
# c)Mostre as duas imagens para comparação e salve a imagem equalizada
# d)Repita o mesmo processo para uma imagem de placa de carro
# e)Repita o mesmo processo para uma imagem da superfície de marte
# f)Repita o mesmo processo para uma imagem de neve nas montanhas da Groenlândia
# g)Repita o mesmo processo para uma imagem do fundo do mar escuro
# h)Repita o mesmo processo para uma imagem de incêndio florestal em cinzas.

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# =============================================================================
# --- FUNÇÃO DA PARTE 1: Processar várias imagens ---
# =============================================================================
def processar_imagem(caminho_arquivo):

   # Lê uma imagem, converte para cinza, equaliza e exibe a comparação.

    imagem = cv2.imread(caminho_arquivo)
    if imagem is None:
        print(f"Erro: Não encontrei a imagem: {caminho_arquivo}")
        return

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_equalizada = cv2.equalizeHist(imagem_cinza)
    
    comparacao = np.hstack([imagem_cinza, imagem_equalizada])
    titulo_janela = os.path.basename(caminho_arquivo)
    cv2.imshow(f'Cinza vs. Equalizada - {titulo_janela}', comparacao)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =============================================================================
# --- FUNÇÃO DA PARTE 2: Analisar a imagem da catedral ---
# =============================================================================
def analisar_e_segmentar(imagem_cinza, titulo_base):
    
   # Calcula e exibe o histograma, e depois segmenta a imagem em 3 regiões.
    
    # 1. Calcula e mostra o gráfico do histograma
    histograma = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])
    plt.figure()
    plt.title(f"Histograma - {titulo_base}")
    plt.xlabel("Tons de Cinza")
    plt.ylabel("Quantidade de Pixels")
    plt.plot(histograma)
    plt.xlim([0, 256])
    plt.show() 

    # 2. Define os limites para segmentar
    limite_escuro = 85
    limite_claro = 170

    # 3. Cria uma imagem nova para colorir a segmentação
    imagem_segmentada = np.zeros((imagem_cinza.shape[0], imagem_cinza.shape[1], 3), dtype=np.uint8)

    # 4. Pinta cada região de uma cor
    imagem_segmentada[imagem_cinza <= limite_escuro] = [255, 0, 0]  # Azul para escuros
    imagem_segmentada[(imagem_cinza > limite_escuro) & (imagem_cinza <= limite_claro)] = [0, 255, 0] # Verde para médios
    imagem_segmentada[imagem_cinza > limite_claro] = [0, 0, 255]   # Vermelho para claros

    # 5. Mostra o resultado
    cv2.imshow(f'Imagem Cinza - {titulo_base}', imagem_cinza)
    cv2.imshow(f'Segmentada (Escuro=Azul, Medio=Verde, Claro=Vermelho) - {titulo_base}', imagem_segmentada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =============================================================================
# --- EXECUÇÃO PRINCIPAL ---
# =============================================================================

# --- INÍCIO DA PARTE 1 ---
print("--- INICIANDO PARTE 1: PROCESSAMENTO DE VÁRIAS IMAGENS ---")
print("Pressione qualquer tecla para fechar cada imagem e passar para a próxima.")

caminho_base = 'C:\\Users\\smantovani\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade4\\'
lista_de_imagens = [
    'cancer de pele.jpg',
    'placa de carro.jpg',
    'marte.jpg',
    'neve.jpg',
    'mar.jpg',
    'incendio.jpg'
]

for nome_imagem in lista_de_imagens:
    caminho_completo = os.path.join(caminho_base, nome_imagem)
    print(f"\nProcessando: {nome_imagem}...")
    processar_imagem(caminho_completo)

print("\n--- PARTE 1 FINALIZADA ---\n")


# --- INÍCIO DA PARTE 2 ---
print("--- INICIANDO PARTE 2: ANÁLISE DA CATEDRAL ---")
print("Atenção: Uma janela com um gráfico irá aparecer. Feche-a para continuar.")

nome_imagem_catedral = 'catedral.jpg' 
caminho_catedral = os.path.join(caminho_base, nome_imagem_catedral)

catedral_cor = cv2.imread(caminho_catedral)

if catedral_cor is None:
    print(f"Erro: Não foi possível encontrar a imagem da catedral em: {caminho_catedral}")
else:
    catedral_cinza = cv2.cvtColor(catedral_cor, cv2.COLOR_BGR2GRAY)

    print("\nAnalisando a imagem original em cinza...")
    analisar_e_segmentar(catedral_cinza, "Original")

    print("\nAnalisando a imagem equalizada...")
    catedral_equalizada = cv2.equalizeHist(catedral_cinza)
    analisar_e_segmentar(catedral_equalizada, "Equalizada")

print("\n--- PARTE 2 FINALIZADA ---")
print("\nTODOS OS PROCESSOS FORAM CONCLUÍDOS!")