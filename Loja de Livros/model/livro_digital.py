from model.produto import Produto

class LivroDigital(Produto):
    def __init__(self, titulo, autor, preco, id_produto, tamanho_mb, formato, url_download):
        super().__init__(titulo, autor, preco, id_produto)
        self.tamanho_mb = tamanho_mb
        self.formato = formato  # PDF, EPUB, etc
        self.url_download = url_download
    
    def calcular_frete(self):
        return 0.0  # Digital não tem frete
    
    def __str__(self):
        return f"[DIGITAL] {super().__str__()} - {self.formato} - {self.tamanho_mb}MB"