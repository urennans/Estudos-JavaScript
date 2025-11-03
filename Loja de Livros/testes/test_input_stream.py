import sys
import os
sys.path.insert(0, r'C:\Faculdade\Repositório GitHub\Loja de Livros')

from streams.livro_input_stream import LivroInputStream

def testar_input_stream_arquivo():
    """Teste do InputStream com arquivo - item 3c"""
    print("🧪 TESTANDO INPUTSTREAM COM ARQUIVO")
    
    # Lê o arquivo que criamos anteriormente
    with open('livros_serializados.bin', 'rb') as arquivo:
        # Criando o LivroInputStream
        livro_input = LivroInputStream(arquivo)
        
        # Executando a desserialização
        print("📖 Lendo dados dos livros do arquivo...")
        livros_desserializados = livro_input.ler_livros()
        
        # Mostrando os livros recuperados
        print("\n📚 LIVROS DESSERIALIZADOS:")
        for i, livro in enumerate(livros_desserializados, 1):
            print(f"  {i}. {livro}")
            if hasattr(livro, 'calcular_frete'):
                print(f"     Frete: R$ {livro.calcular_frete():.2f}")
    
    print("✅ Teste do InputStream com arquivo concluído!")

if __name__ == "__main__":
    testar_input_stream_arquivo()