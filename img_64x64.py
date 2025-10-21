from PIL import Image
import os

def processar_imagem(entrada, saida, tamanho=(96, 96), cores=128):
    try:
        # Abrir imagem
        img = Image.open(entrada)

        # Redimensionar
        img = img.resize(tamanho, Image.LANCZOS)

        # Converter para formato indexado com paleta adaptativa
        # img = img.convert("P", palette=Image.ADAPTIVE, colors=cores)

        # Salvar imagem final
        img.save(saida)

        print(f"✅ Imagem processada com sucesso: {saida}")
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {entrada}")
    except Exception as e:
        print(f"⚠️ Erro ao processar imagem: {e}")

if __name__ == "__main__":
    entrada = "Screenshot_117.png"
    saida = "Screenshot_117_64x64_128cores.png"
    print("🔧 Iniciando processamento da imagem...")
    processar_imagem(entrada, saida)