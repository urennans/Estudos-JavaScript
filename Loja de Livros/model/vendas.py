from abc import ABC, abstractmethod

class Vendas(ABC):
    @abstractmethod
    def realizar_venda(self, produto, quantidade):
        pass
    
    @abstractmethod
    def listar_produtos(self):
        pass
    
    @abstractmethod
    def buscar_produto(self, id_produto):
        pass