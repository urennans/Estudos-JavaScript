from model.produto import Produto
from model.livro_fisico import LivroFisico
from model.livro_digital import LivroDigital
from model.livro_colecionavel import LivroColecionavel
from model.loja_virtual import LojaVirtual

def testar_classes():
    print("🔍 TESTANDO CLASSES DA LIVRARIA...")
    
    # 1. Criando alguns produtos
    livro1 = LivroFisico(
        "Dom Casmurro", 
        "Machado de Assis", 
        45.90, 
        "LIV001", 
        500,  # 500g
        256,  # páginas
        10    # estoque
    )
    
    livro2 = LivroDigital(
        "Python para Iniciantes",
        "John Doe",
        29.90,
        "DIG001",
        15.5,  # MB
        "PDF",
        "http://download.com/python.pdf"
    )
    
    livro3 = LivroColecionavel(
        "O Senhor dos Anéis - Edição Especial",
        "J.R.R. Tolkien",
        199.90,
        "COL001",
        1975,  # ano
        "001/500",  # num série
        "Novo"
    )
    
    # 2. Testando métodos
    print("\n📚 PRODUTOS CRIADOS:")
    print(f"Livro 1: {livro1}")
    print(f"  Frete: R$ {livro1.calcular_frete():.2f}")
    
    print(f"Livro 2: {livro2}")
    print(f"  Frete: R$ {livro2.calcular_frete():.2f}")
    
    print(f"Livro 3: {livro3}")
    print(f"  Frete: R$ {livro3.calcular_frete():.2f}")
    
    # 3. Testando a loja virtual
    print("\n🏪 TESTANDO LOJA VIRTUAL:")
    loja = LojaVirtual("Livraria Distribuída")
    
    # Adicionando produtos (agregação)
    loja.adicionar_produto(livro1)
    loja.adicionar_produto(livro2)
    loja.adicionar_produto(livro3)
    
    # Listando produtos
    loja.listar_produtos()
    
    # Testando vendas
    print("\n💰 TESTANDO VENDAS:")
    loja.realizar_venda(livro1, 2)  # Vende 2 unidades
    loja.realizar_venda(livro2, 1)  # Vende 1 unidade digital
    
    # Buscando produto
    print("\n🔎 BUSCANDO PRODUTO:")
    produto_encontrado = loja.buscar_produto("LIV001")
    if produto_encontrado:
        print(f"Produto encontrado: {produto_encontrado}")
    
    print(f"\n✅ Loja: {loja}")
    print(f"✅ Vendas realizadas: {len(loja.vendas_realizadas)}")

if __name__ == "__main__":
    testar_classes()