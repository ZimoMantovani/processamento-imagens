import cv2
import numpy as np
import os

# --- FUNÇÃO AUXILIAR PARA LIMPEZA ---
def limpar_ruido_conectividade(mascara_binaria):
    """
    Remove todos os pequenos objetos brancos de uma máscara, mantendo apenas o maior.
    Isso é útil para limpar ruídos depois da binarização.
    """
    # Encontra todos os componentes (objetos brancos) na imagem
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mascara_binaria, 4, cv2.CV_32S)

    # Se não houver nada além do fundo, retorna a máscara original
    if num_labels < 2:
        return mascara_binaria

    # Encontra o índice (label) do maior componente, ignorando o fundo (label 0)
    maior_componente_idx = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1

    # Cria uma nova imagem preta com o mesmo tamanho
    resultado_limpo = np.zeros_like(mascara_binaria)
    
    # Pinta de branco apenas os pixels que pertencem ao maior componente
    resultado_limpo[labels == maior_componente_idx] = 255

    return resultado_limpo

# --- FUNÇÕES DE SEGMENTAÇÃO PARA CADA IMAGEM ---

def segmentar_cachoeira(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # cachoeira que é muito brilhante, limiar alto
    _, mascara = cv2.threshold(imagem_cinza, 200, 255, cv2.THRESH_BINARY)
    mascara_limpa = limpar_ruido_conectividade(mascara)
    return mascara_limpa

def segmentar_plantacao(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Equalização para aumentar o contraste entre céu e plantação
    img_equalizada = cv2.equalizeHist(imagem_cinza)
    # Pega o céu que ficou branco
    _, mascara_ceu = cv2.threshold(img_equalizada, 210, 255, cv2.THRESH_BINARY)
    # Inverte a máscara para destacar a plantação
    mascara_plantacao = cv2.bitwise_not(mascara_ceu)
    return mascara_plantacao

def segmentar_predios(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Equalização para ajudar a separar o céu dos prédios
    img_equalizada = cv2.equalizeHist(imagem_cinza)
    # Pega o céu brilhante
    _, mascara_ceu = cv2.threshold(img_equalizada, 215, 255, cv2.THRESH_BINARY)
    # Inverte para destacar os prédios e árvores
    mascara_predios = cv2.bitwise_not(mascara_ceu)
    return mascara_predios

def segmentar_macas(imagem):
    # Separa os canais de cor BGR (Azul, Verde, Vermelho)
    _, _, canal_vermelho = cv2.split(imagem)
    # No canal vermelho, as maçãs são muito mais claras que as folhas
    _, mascara = cv2.threshold(canal_vermelho, 160, 255, cv2.THRESH_BINARY)
    mascara_limpa = limpar_ruido_conectividade(mascara)
    return mascara_limpa

def segmentar_orquidea(imagem):
    _, _, canal_vermelho = cv2.split(imagem)
    # As flores rosas/vermelhas se destacam no canal vermelho
    _, mascara = cv2.threshold(canal_vermelho, 180, 255, cv2.THRESH_BINARY)
    mascara_limpa = limpar_ruido_conectividade(mascara)
    return mascara_limpa

def segmentar_desmatamento(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Equalização para aumentar o contraste entre a terra e a floresta
    img_equalizada = cv2.equalizeHist(imagem_cinza)
    # A área desmatada fica bem clara após a equalização
    _, mascara = cv2.threshold(img_equalizada, 150, 255, cv2.THRESH_BINARY)
    mascara_limpa = limpar_ruido_conectividade(mascara)
    return mascara_limpa


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    pasta_entrada = 'C:\\Users\\symon\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade6'
    pasta_saida = 'C:\\Users\\symon\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade6\\resultados'

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    tarefas = {
        "cachoeira.jfif": segmentar_cachoeira,
        "plantacao.jfif": segmentar_plantacao,
        "predios.jfif": segmentar_predios,
        "maca.jfif": segmentar_macas,
        "orquidea.jfif": segmentar_orquidea,
        "desmatamento.jfif": segmentar_desmatamento
    }

    print("Iniciando a segmentação de imagens...")

    for nome_arquivo, funcao in tarefas.items():
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        
        # Lê a magem
        imagem_original = cv2.imread(caminho_entrada)
        
        if imagem_original is None:
            print(f"ERRO: Não foi possível ler a imagem: {nome_arquivo}. Verifique o nome e a pasta.")
            continue 

        print(f"Processando: {nome_arquivo}...")
        
        resultado_final = funcao(imagem_original)
        
        # Salva o resultado
        novo_nome = f"segmentado_{os.path.splitext(nome_arquivo)[0]}.png"
        caminho_saida = os.path.join(pasta_saida, novo_nome)
        cv2.imwrite(caminho_saida, resultado_final)

    print(f"\nProcesso finalizado! Os resultados foram salvos na pasta '{pasta_saida}'.")