from Books import book
from bubble_sort_growing import test_bubble_sort_growing
from bubble_sort_decreasing import test_bubble_sort_decreasing
from insert_item import insert_item, test_insert_item
from remove_item import remove_item, test_remove_item

# Iniciando uma lista vazia de livros
books = []

# Adicionando objetos à minha lista de livros
books.append(book("Dom Quixote", "Miguel de Cervantes", 120, 75))
books.append(book("Guerra e Paz", "Liev Tolstói", 250, 55))
books.append(book("A Montanha Mágica", "Thomas Mann", 175, 99))
books.append(book("Cem Anos de Solidão",
             "Gabriel García Márquez", 345, 79.50))
books.append(book("O Processo", "Franz Kafka", 99, 37))
books.append(book("O Som e a Fúria", "William Faulkner", 279, 120))
books.append(book("A Morte de Virgílio", "Hermann Broch", 79, 89))
books.append(book("Rumo ao Farol", "Virginia Woolf", 89, 56))
books.append(book("O Lobo da Estepe", "Herman Hesse", 55, 99))
books.append(book("O Grande Gatsby", "Scott Fitzgerald", 88, 78))

# Chamo a função que vai iniciar meus testes e ordenação de titulo,
# passando a lista de livros como parâmetro
print("\n================================ LISTA ORDENADA EM ORDEM CRESCENTE =================================")
print("\n============ De acordo com Número de páginas")
test_bubble_sort_growing(books, "pages")
print("\n============ De acordo com Preço")
test_bubble_sort_growing(books, "price")
print("\n============ De acordo com Titulo")
test_bubble_sort_growing(books, "title")
print("\n============ De acordo com Nome do autor")
test_bubble_sort_growing(books, "author")

print("\n================================ LISTA ORDENADA EM ORDEM DECRESCENTE =================================")
print("\n============ De acordo com Número de páginas")
test_bubble_sort_decreasing(books, "pages")
print("\n============ De acordo com Preço")
test_bubble_sort_decreasing(books, "price")
print("\n============ De acordo com Titulo")
test_bubble_sort_decreasing(books, "title")
print("\n============ De acordo com Nome do autor")
test_bubble_sort_decreasing(books, "author")

print("\n============================= INSERINDO LIVROS NA PRATELEIRA ELETRONICA =============================")
insert_item(books)
test_insert_item(books)

print("\n============================= REMOVENDO LIVROS NA PRATELEIRA ELETRONICA =============================")
remove_item(books, "A Montanha Mágica")
test_remove_item(books)