from model.vendas import Vendas
from model.produto import Produto
# Adicionar os imports das classes específicas
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel

class LojaVirtual(Vendas):
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []  # Agregação - "tem-um" produtos
        self.vendas_realizadas = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto adicionado: {produto.titulo}")
    
    def realizar_venda(self, produto, quantidade):
        if isinstance(produto, LivroFisico):
            if produto.estoque >= quantidade:
                produto.estoque -= quantidade
                venda = {
                    'produto': produto.titulo,
                    'quantidade': quantidade,
                    'total': produto.preco * quantidade
                }
                self.vendas_realizadas.append(venda)
                print(f"Venda realizada: {quantidade}x {produto.titulo}")
                return True
            else:
                print("Estoque insuficiente!")
                return False
        else:
            # Digital ou colecionável - venda direta
            venda = {
                'produto': produto.titulo,
                'quantidade': quantidade,
                'total': produto.preco * quantidade
            }
            self.vendas_realizadas.append(venda)
            print(f"Venda realizada: {quantidade}x {produto.titulo}")
            return True
    
    def listar_produtos(self):
        print(f"\n--- Produtos na {self.nome} ---")
        for produto in self.produtos:
            print(f"  {produto}")
        return self.produtos
    
    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto.id_produto == id_produto:
                return produto
        return None
    
    def __str__(self):
        return f"LojaVirtual: {self.nome} - {len(self.produtos)} produtos"