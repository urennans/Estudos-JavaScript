import sys
import os

# Adiciona o diretório raiz ao path do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streams.livro_output_stream import LivroOutputStream
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel

def testar_system_out():
    """Teste com System.out como o professor pede no item 2b-i"""
    print("🧪 TESTANDO SERIALIZAÇÃO COM SYSTEM.OUT")
    
    # Criando alguns livros para teste
    livros = [
        LivroFisico("Dom Casmurro", "Machado de Assis", 45.90, "LIV001", 500, 256, 10),
        LivroDigital("Python Guide", "Ana Silva", 29.90, "DIG001", 15.5, "PDF", "http://download.com/python.pdf"),
        LivroColecionavel("O Senhor dos Anéis", "J.R.R. Tolkien", 199.90, "COL001", 1975, "001/500", "Novo")
    ]
    
    # Usando System.out como OutputStream (stdout em Python)
    output_stream = sys.stdout.buffer  # Stream binário
    
    # Criando o LivroOutputStream como o professor pede
    livro_stream = LivroOutputStream(
        livros_array=livros,
        num_objects=len(livros),
        output_stream=output_stream
    )
    
    # Executando a serialização
    print("📤 Enviando dados dos livros para System.out...")
    livro_stream.enviar_livros()
    print("✅ Teste com System.out concluído!")

if __name__ == "__main__":
    testar_system_out()