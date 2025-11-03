import sys
import os
sys.path.insert(0, r'C:\Faculdade\Repositório GitHub\Loja de Livros')

from streams.livro_output_stream import LivroOutputStream
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel

def testar_arquivo():
    """Teste com FileOutputStream como o professor pede no item 2b-ii"""
    print("🧪 TESTANDO SERIALIZAÇÃO COM ARQUIVO")
    
    # Criando alguns livros para teste
    livros = [
        LivroFisico("Dom Casmurro", "Machado de Assis", 45.90, "LIV001", 500, 256, 10),
        LivroDigital("Python Guide", "Ana Silva", 29.90, "DIG001", 15.5, "PDF", "http://download.com/python.pdf"),
        LivroColecionavel("O Senhor dos Anéis", "J.R.R. Tolkien", 199.90, "COL001", 1975, "001/500", "Novo")
    ]
    
    # Usando FileOutputStream (arquivo em Python)
    with open('livros_serializados.bin', 'wb') as arquivo:
        # Criando o LivroOutputStream
        livro_stream = LivroOutputStream(
            livros_array=livros,
            num_objects=len(livros),
            output_stream=arquivo
        )
        
        # Executando a serialização
        print("📤 Salvando dados dos livros em arquivo...")
        livro_stream.enviar_livros()
    
    # Verificar tamanho do arquivo
    tamanho = os.path.getsize('livros_serializados.bin')
    print(f"✅ Arquivo criado: livros_serializados.bin ({tamanho} bytes)")
    print("✅ Teste com arquivo concluído!")

if __name__ == "__main__":
    testar_arquivo()