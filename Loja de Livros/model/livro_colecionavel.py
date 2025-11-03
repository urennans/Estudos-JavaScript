from model.produto import Produto

class LivroColecionavel(Produto):
    def __init__(self, titulo, autor, preco, id_produto, ano_edicao, numero_serie, estado):
        super().__init__(titulo, autor, preco, id_produto)
        self.ano_edicao = ano_edicao
        self.numero_serie = numero_serie
        self.estado = estado  # "Novo", "Usado", etc
    
    def calcular_frete(self):
        # Frete mais caro para itens colecionáveis
        return 25.0
    
    def __str__(self):
        return f"[COLECIONÁVEL] {super().__str__()} - Ed. {self.ano_edicao} - {self.estado}"