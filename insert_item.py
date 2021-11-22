from Books import book

# Definindo a função para inserir um livro 
def insert_item(list):

    # Solicitando os dados que serão inseridos
    title = input("Digite o titulo do livro\n")
    author = input("Digite o nome do autor do livro\n")
    pages = int(input("Digite a quantidade de páginas do livro\n"))
    price = float(input("Digite o preço do livro\n"))

    # Incrementando na lista utilizando a função append
    list.append(book(title, author, pages, price))

# Defino uma função para testar os casos de uso, recebe a lista desordenada
def test_insert_item(list):
        
    # Exibo uma mensagem em tela para introduzir a lista após a inserção
    print('\n======================= ESTANTE APÓS A INSERÇÃO ============================')

    # Defino uma estrutura de repetição que vai do range 0 até o tamanho da lista
    for current in range(0, len(list)):
        item = list[current]

        # Para cada repetição eu vou exibir o titulo, para confirmar que a lista possui o novo elemento
        print(f'{item.title}, {item.price}, {item.pages}, {item.author}')
