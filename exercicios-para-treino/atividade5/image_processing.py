import cv2
import numpy as np
import os

def apply_filters_and_display(image_path):
    """
    Aplica vários filtros em uma imagem e mostra todos em uma única janela.
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return


    max_dim = 250
    h, w = img.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)

    images_to_display = [("Original", img)]

    images_to_display.append(("Media 3x3", cv2.blur(img, (3, 3))))
    images_to_display.append(("Media 5x5", cv2.blur(img, (5, 5))))
    images_to_display.append(("Gaussiana 3x3", cv2.GaussianBlur(img, (3, 3), 0)))
    images_to_display.append(("Gaussiana 5x5", cv2.GaussianBlur(img, (5, 5), 0)))
    images_to_display.append(("Mediana 3x3", cv2.medianBlur(img, 3)))
    images_to_display.append(("Mediana 5x5", cv2.medianBlur(img, 5)))
    images_to_display.append(("Bilateral 75", cv2.bilateralFilter(img, 9, 75, 75)))
    images_to_display.append(("Bilateral 150", cv2.bilateralFilter(img, 9, 150, 150)))

    # Criar uma grade 3x3 para exibir as 9 imagens (original + 8 filtros)
    rows = 3
    cols = 3
    
    # Obter a altura e largura máximas para redimensionar as imagens para exibição
    max_h = max([i[1].shape[0] for i in images_to_display])
    max_w = max([i[1].shape[1] for i in images_to_display])

    # Adicionar texto e redimensionar imagens para a mesma dimensão para a grade
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5 
    font_thickness = 1
    text_color = (255, 255, 255) # Branco
    
    processed_images = []
    for label, image in images_to_display:
        # Redimensionar para a dimensão máxima
        resized_image = cv2.resize(image, (max_w, max_h), interpolation=cv2.INTER_AREA)
        
        # Adicionar borda preta no topo para o texto
        border_size = 30
        bordered_image = cv2.copyMakeBorder(resized_image, border_size, 0, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        
        # Adicionar texto
        cv2.putText(bordered_image, label, (10, 20), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
        processed_images.append(bordered_image)

    # Organiza as imagens em uma grade
    grid_rows = []
    for i in range(rows):
        row_images = processed_images[i*cols : (i+1)*cols]
        grid_rows.append(np.hstack(row_images))
    
    final_grid = np.vstack(grid_rows)
    
    titulo_janela = os.path.basename(image_path)
    cv2.imshow(f'Filtros Aplicados - {titulo_janela}', final_grid)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == '__main__':
    pasta_das_imagens = 'C:\\Users\\symon\\Documents\\GitHub\\processamento-imagens\\exercicios-para-treino\\atividade5'
    
    lista_de_arquivos = [
        "lenna com ruido.jpg",
        "menina com ruido.jpg",
        "chuva.jpg",
        "nevoeiro.jpg",
        "tempestade.jpg",
        "tubos.jpg"
    ]
    
    print("Iniciando processamento. Pressione qualquer tecla para passar para a próxima imagem.")

    for nome_do_arquivo in lista_de_arquivos:
        caminho_completo = os.path.join(pasta_das_imagens, nome_do_arquivo)
        
        print(f"\nProcessando a imagem: {caminho_completo}")
        apply_filters_and_display(caminho_completo)

    print("\nTodas as imagens foram processadas.")