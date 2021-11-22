def remove_item(list, title):
    # Defino uma estrutura de repetição que vai do range 0 até o tamanho da lista
    for current in range(0, len(list)):

        # Itero pelos titulos
        item = list[current].title

        # Se o titulo (da estante) for igual ao titulo digitado
        if (item == title):

            # Busca o índice do item
            index = list.index(list[current])

            # Remove o item baseado no index utilizando a função POP
            list.pop(index)

            # Retorna a nova lista para parar a iteração
            return list

# Defino uma função para testar os casos de uso, recebe a lista desordenada
def test_remove_item(list):

    # Exibo uma mensagem em tela para introduzir a lista sem ordenação
    print('\n======================= ESTANTE APÓS A DELEÇÃO ============================')

    # Defino uma estrutura de repetição que vai do range 0 até o tamanho da lista
    for current in range(0, len(list)):
        item = list[current]

        # Para cada repetição eu vou exibir o titulo, para confirmar que a lista está desordenada
        print(f'{item.title}, {item.price}, {item.pages}, {item.author}')
