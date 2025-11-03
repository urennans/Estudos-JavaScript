import io
import struct
import json
from datetime import datetime

class LivroOutputStream:
    def __init__(self, livros_array, num_objects, output_stream):
        """
        Construtor como o professor pede no item 2a:
        - livros_array: array de objetos Livro
        - num_objects: número de objetos a serem enviados
        - output_stream: stream de destino (System.out, FileOutputStream, etc)
        """
        self.livros_array = livros_array
        self.num_objects = num_objects
        self.output_stream = output_stream
    
    def enviar_livros(self):
        """Envia os dados dos livros seguindo as regras do professor"""
        try:
            # 1. Envia o número de objetos (item 2a-ii)
            self._escrever_int(self.num_objects)
            
            # 2. Para cada objeto, envia os dados (item 2a-iii)
            for i in range(self.num_objects):
                if i < len(self.livros_array) and self.livros_array[i] is not None:
                    livro = self.livros_array[i]
                    self._serializar_livro(livro)
            
            if hasattr(self.output_stream, 'flush'):
                self.output_stream.flush()
            print(f"✅ {self.num_objects} livros serializados com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro na serialização: {e}")
    
    def _serializar_livro(self, livro):
        """Serializa pelo menos 3 atributos de cada livro"""
        # Envia o tipo do livro
        tipo = self._obter_tipo_livro(livro)
        self._escrever_string(tipo)
        
        # Serializa 3 atributos base (como o professor pede)
        self._escrever_string(livro.titulo)      # Atributo 1
        self._escrever_string(livro.autor)       # Atributo 2  
        self._escrever_float(livro.preco)        # Atributo 3
        
        # Atributos específicos por tipo
        if tipo == "FISICO":
            self._escrever_float(livro.peso)
            self._escrever_int(livro.num_paginas)
            self._escrever_int(livro.estoque)
        elif tipo == "DIGITAL":
            self._escrever_float(livro.tamanho_mb)
            self._escrever_string(livro.formato)
            self._escrever_string(livro.url_download)
        elif tipo == "COLECIONAVEL":
            self._escrever_int(livro.ano_edicao)
            self._escrever_string(livro.numero_serie)
            self._escrever_string(livro.estado)
    
    def _obter_tipo_livro(self, livro):
        """Identifica o tipo do livro para serialização"""
        if hasattr(livro, 'peso') and hasattr(livro, 'estoque'):
            return "FISICO"
        elif hasattr(livro, 'tamanho_mb') and hasattr(livro, 'formato'):
            return "DIGITAL"
        elif hasattr(livro, 'ano_edicao') and hasattr(livro, 'numero_serie'):
            return "COLECIONAVEL"
        else:
            return "DESCONHECIDO"
    
    # Métodos auxiliares para escrever tipos primitivos
    def _escrever_int(self, valor):
        data = struct.pack('>i', valor)  # Big-endian 4 bytes
        self.output_stream.write(data)
    
    def _escrever_float(self, valor):
        data = struct.pack('>f', valor)  # Big-endian 4 bytes
        self.output_stream.write(data)
    
    def _escrever_string(self, valor):
        if valor is None:
            valor = ""
        bytes_data = valor.encode('utf-8')
        self._escrever_int(len(bytes_data))  # Tamanho da string
        self.output_stream.write(bytes_data) # Dados da string
    
    def close(self):
        """Fecha o stream"""
        if hasattr(self.output_stream, 'close'):
            self.output_stream.close()