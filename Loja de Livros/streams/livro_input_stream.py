import struct
import io

class LivroInputStream:
    def __init__(self, input_stream):
        """
        Construtor como o professor pede no item 3a:
        - input_stream: stream de origem (System.in, FileInputStream, etc)
        """
        self.input_stream = input_stream
    
    def ler_livros(self):
        """Lê os dados serializados e retorna lista de livros"""
        try:
            # 1. Lê o número de objetos
            num_objects = self._ler_int()
            livros = []
            
            print(f"📖 Lendo {num_objects} livros serializados...")
            
            # 2. Para cada objeto, lê os dados
            for i in range(num_objects):
                livro = self._desserializar_livro()
                if livro:
                    livros.append(livro)
            
            print(f"✅ {len(livros)} livros desserializados com sucesso!")
            return livros
            
        except Exception as e:
            print(f"❌ Erro na desserialização: {e}")
            return []
    
    def _desserializar_livro(self):
        """Desserializa um livro a partir dos bytes"""
        # Lê o tipo do livro
        tipo = self._ler_string()
        
        # Lê os 3 atributos base
        titulo = self._ler_string()
        autor = self._ler_string()
        preco = self._ler_float()
        
        # Importa as classes aqui para evitar circular imports
        from model.livro_fisico import LivroFisico
        from model.livro_digital import LivroDigital
        from model.livro_colecionavel import LivroColecionavel
        
        # Cria o objeto específico baseado no tipo
        if tipo == "FISICO":
            peso = self._ler_float()
            num_paginas = self._ler_int()
            estoque = self._ler_int()
            return LivroFisico(titulo, autor, preco, f"LIV_{len(titulo)}", peso, num_paginas, estoque)
        
        elif tipo == "DIGITAL":
            tamanho_mb = self._ler_float()
            formato = self._ler_string()
            url_download = self._ler_string()
            return LivroDigital(titulo, autor, preco, f"DIG_{len(titulo)}", tamanho_mb, formato, url_download)
        
        elif tipo == "COLECIONAVEL":
            ano_edicao = self._ler_int()
            numero_serie = self._ler_string()
            estado = self._ler_string()
            return LivroColecionavel(titulo, autor, preco, f"COL_{len(titulo)}", ano_edicao, numero_serie, estado)
        
        else:
            print(f"⚠️ Tipo de livro desconhecido: {tipo}")
            return None
    
    # Métodos auxiliares para ler tipos primitivos
    def _ler_int(self):
        data = self.input_stream.read(4)  # 4 bytes para int
        return struct.unpack('>i', data)[0]
    
    def _ler_float(self):
        data = self.input_stream.read(4)  # 4 bytes para float
        return struct.unpack('>f', data)[0]
    
    def _ler_string(self):
        tamanho = self._ler_int()  # Tamanho da string
        data = self.input_stream.read(tamanho)  # Dados da string
        return data.decode('utf-8')
    
    def close(self):
        """Fecha o stream"""
        if hasattr(self.input_stream, 'close'):
            self.input_stream.close()