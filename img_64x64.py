from PIL import Image
import os

# --- Função Principal de Processamento (Mantida como a sua) ---
def processar_imagem(entrada, saida, tamanho=(64, 64)):
    """Redimensiona uma imagem e a salva no caminho de saída."""
    try:
        # Abrir imagem
        img = Image.open(entrada)

        # Redimensionar com alta qualidade (LANCZOS)
        img = img.resize(tamanho, Image.LANCZOS) # Image.LANCZOS é bom para redução

        # Salvar imagem final
        img.save(saida)

        print(f"✅ Imagem processada: {saida}")
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {entrada}")
    except Exception as e:
        print(f"⚠️ Erro ao processar '{os.path.basename(entrada)}': {e}")

# --- Novo Bloco Principal para Processar a Pasta ---
if __name__ == "__main__":
    # --- Configuração ---
    # Defina a pasta de entrada (onde estão suas imagens originais)
    # '.' significa a pasta atual onde o script está
    pasta_entrada = "." 
    
    # Defina a pasta de saída (onde as imagens redimensionadas serão salvas)
    pasta_saida = "output_64x64"
    
    # Crie a pasta de saída se ela não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"📁 Pasta de saída criada: {pasta_saida}")

    # Tipos de arquivos de imagem que queremos processar
    tipos_imagem = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

    print("\n🔧 Iniciando processamento em lote...")

    # --- Loop pelos arquivos na pasta de entrada ---
    for nome_arquivo in os.listdir(pasta_entrada):
        # Checa se o arquivo tem uma extensão de imagem válida (ignorando maiúsculas/minúsculas)
        if nome_arquivo.lower().endswith(tipos_imagem):
            # Monta o caminho completo para o arquivo de entrada
            caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
            
            # Cria o nome do arquivo de saída
            # Ex: "minha_imagem.png" -> "minha_imagem_64x64.png"
            nome_base, extensao = os.path.splitext(nome_arquivo)
            nome_saida = f"{nome_base}_64x64{extensao}"
            
            # Monta o caminho completo para o arquivo de saída
            caminho_saida = os.path.join(pasta_saida, nome_saida)

            # Chama a função para processar a imagem atual
            processar_imagem(caminho_entrada, caminho_saida)
        else:
            # Informa se um arquivo foi ignorado (não era imagem)
            # Para evitar poluir, você pode comentar a linha abaixo se não quiser ver isso
            # print(f"⚪ Arquivo ignorado (não é imagem suportada): {nome_arquivo}")
            pass # Apenas ignora arquivos que não são imagens

    print("\n🎉 Processamento em lote concluído!")