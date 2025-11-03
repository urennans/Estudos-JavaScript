from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, titulo, autor, preco, id_produto):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.id_produto = id_produto
    
    @abstractmethod
    def calcular_frete(self):
        pass
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} - R$ {self.preco:.2f}"