import socket
import threading
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streams.livro_input_stream import LivroInputStream
from streams.livro_output_stream import LivroOutputStream
from streams.socket_stream import SocketStreamWrapper
from model.loja_virtual import LojaVirtual
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel

class ServidorLivros:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.loja = LojaVirtual("Livraria Distribuída TCP")
        self._inicializar_loja()
    
    def _inicializar_loja(self):
        """Adiciona alguns livros de exemplo à loja"""
        livros_exemplo = [
            LivroFisico("Dom Casmurro", "Machado de Assis", 45.90, "LIV001", 500, 256, 10),
            LivroDigital("Python Avançado", "Carlos Silva", 79.90, "DIG001", 25.0, "PDF", "http://download.com/python_avancado.pdf"),
            LivroColecionavel("1984 - Edição Especial", "George Orwell", 299.90, "COL001", 1949, "001/1000", "Novo"),
            LivroFisico("Clean Code", "Robert Martin", 89.90, "LIV002", 600, 320, 5)
        ]
        
        for livro in livros_exemplo:
            self.loja.adicionar_produto(livro)
        
        print(f"🏪 Loja inicializada com {len(livros_exemplo)} livros")
    
    def iniciar_servidor(self):
        """Inicia o servidor TCP multi-threaded"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            
            print(f"🚀 Servidor de Livros iniciado em {self.host}:{self.port}")
            print("📡 Aguardando conexões de clientes...")
            
            try:
                while True:
                    client_socket, client_address = server_socket.accept()
                    print(f"🔗 Cliente conectado: {client_address}")
                    
                    # Cria uma thread para cada cliente
                    client_thread = threading.Thread(
                        target=self._tratar_cliente,
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
            except KeyboardInterrupt:
                print("\n🛑 Servidor encerrado pelo usuário")
    
    def _tratar_cliente(self, client_socket, client_address):
        """Trata a comunicação com um cliente específico"""
        try:
            with client_socket:
                # Cria wrapper para o socket
                socket_stream = SocketStreamWrapper(client_socket)
                
                # 1. Recebe dados do cliente (livros serializados)
                print(f"📥 Recebendo dados do cliente {client_address}...")
                
                # Usa LivroInputStream para ler os dados
                livro_input = LivroInputStream(socket_stream)
                livros_recebidos = livro_input.ler_livros()
                
                print(f"📚 {len(livros_recebidos)} livros recebidos do cliente")
                
                # 2. Processa os livros recebidos (adiciona à loja)
                for livro in livros_recebidos:
                    if livro:
                        self.loja.adicionar_produto(livro)
                
                # 3. Envia confirmação + lista atualizada de volta ao cliente
                print(f"📤 Enviando resposta para {client_address}...")
                
                # Prepara dados para enviar (todos os livros da loja)
                todos_livros = self.loja.listar_produtos()
                
                # Usa LivroOutputStream para enviar os dados
                livro_output = LivroOutputStream(
                    livros_array=todos_livros,
                    num_objects=len(todos_livros),
                    output_stream=socket_stream
                )
                livro_output.enviar_livros()
                
                print(f"✅ Comunicação com {client_address} concluída")
                
        except Exception as e:
            print(f"❌ Erro com cliente {client_address}: {e}")

if __name__ == "__main__":
    servidor = ServidorLivros()
    servidor.iniciar_servidor()