import socket
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streams.livro_output_stream import LivroOutputStream
from streams.livro_input_stream import LivroInputStream
from streams.socket_stream import SocketStreamWrapper
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel

class ClienteLivros:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
    
    def enviar_livros_servidor(self, livros):
        """Envia livros para o servidor e recebe a lista atualizada"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                print(f"🔗 Conectando ao servidor {self.host}:{self.port}...")
                client_socket.connect((self.host, self.port))
                print("✅ Conectado ao servidor!")
                
                # Cria wrapper para o socket
                socket_stream = SocketStreamWrapper(client_socket)
                
                # 1. Envia livros para o servidor
                print("📤 Enviando livros para o servidor...")
                livro_output = LivroOutputStream(
                    livros_array=livros,
                    num_objects=len(livros),
                    output_stream=socket_stream
                )
                livro_output.enviar_livros()
                
                # 2. Recebe a resposta do servidor
                print("📥 Recebendo resposta do servidor...")
                livro_input = LivroInputStream(socket_stream)
                livros_servidor = livro_input.ler_livros()
                
                # 3. Mostra os livros recebidos do servidor
                print("\n🏪 LIVROS DISPONÍVEIS NO SERVIDOR:")
                for i, livro in enumerate(livros_servidor, 1):
                    print(f"  {i}. {livro}")
                
                return livros_servidor
                
        except Exception as e:
            print(f"❌ Erro na comunicação com o servidor: {e}")
            return []

def testar_cliente_servidor():
    """Teste completo de comunicação TCP"""
    print("🧪 TESTANDO COMUNICAÇÃO TCP CLIENTE-SERVIDOR")
    
    # Livros que o cliente vai enviar
    livros_cliente = [
        LivroFisico("Arquitetura Limpa", "Robert Martin", 99.90, "LIV003", 550, 350, 8),
        LivroDigital("Design Patterns", "Erich Gamma", 69.90, "DIG002", 18.2, "EPUB", "http://download.com/patterns.epub")
    ]
    
    cliente = ClienteLivros()
    livros_recebidos = cliente.enviar_livros_servidor(livros_cliente)
    
    print(f"\n✅ Teste TCP concluído! Recebidos {len(livros_recebidos)} livros do servidor")

if __name__ == "__main__":
    testar_cliente_servidor()