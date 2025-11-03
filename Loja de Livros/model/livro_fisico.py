from model.produto import Produto

class LivroFisico(Produto):
    def __init__(self, titulo, autor, preco, id_produto, peso, num_paginas, estoque):
        super().__init__(titulo, autor, preco, id_produto)
        self.peso = peso  # em gramas
        self.num_paginas = num_paginas
        self.estoque = estoque
    
    def calcular_frete(self):
        # Frete base + peso
        return 10.0 + (self.peso * 0.02)
    
    def __str__(self):
        return f"[FÍSICO] {super().__str__()} - {self.peso}g - {self.estoque} em estoque"