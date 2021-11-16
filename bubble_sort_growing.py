# Definindo a função que terá o comportamento do bubble sort de forma crescente, recebe a lista como parametro
def bubble_sort_growing(list, by):
    item = ''
    nextItem = ''

    # Defino uma estrutura de repetição para ir da ultima posição da lista até a posição 0,
    # e vai decrementando
    for final in range(len(list), 0, -1):

        # Defino uma variavel que armazenará o "estado" da minha lista,
        # se há ou não elementos para ordenar, iniciando em False
        exchanging = False

        # Faço outra repetição para varrer cada elemento da lista, esta repetição vai
        # até o final do tamanho da lista -1 (por conta da lista iniciar no elemento 0)
        for current in range(0, final - 1):
            if (by == 'title'):
                item = list[current].title
                nextItem = list[current + 1].title
            elif (by == 'price'):
                item = list[current].price
                nextItem = list[current + 1].price
            elif (by == 'pages'):
                item = list[current].pages
                nextItem = list[current + 1].pages
            elif (by == 'author'):
                item = list[current].author
                nextItem = list[current + 1].author
            
            # Se o titulo da lista nessa repetição for maior que o seu sucessor
            if (item > nextItem):

                # Digo então que vou inverter o valor delas, para que a maior fique depois
                list[current], list[current+1] = list[current+1], list[current]
                exchanging = True

        # Se eu não tiver mais elementos para ordenar, paro a execução do bubble_sort
        if not exchanging:
            break

    # Ao finalizar a organização, retorno a lista atual organizada
    return list

# Defino uma função para testar os casos de uso, recebe a lista desordenada
def test_bubble_sort_growing(list, by):
        
    # Exibo uma mensagem em tela para introduzir a lista sem ordenação
    print('\n======================= LISTA DESORDENADA ============================')

    # Defino uma estrutura de repetição que vai do range 0 até o tamanho da lista
    for current in range(0, len(list)):
        if (by == 'title'):
            item = list[current].title
        elif (by == 'price'):
            item = list[current].price
        elif (by == 'pages'):
            item = list[current].pages
        elif (by == 'author'):
            item = list[current].author

        # Para cada repetição eu vou exibir o titulo, para confirmar que a lista está desordenada
        print(item)

    # Chamo a função que organiza minha lista salvando os valores organizados em uma variavel
    test = bubble_sort_growing(list, by)

    # Exibo uma mensagem em tela para introduzir a lista com ordenação
    print('\n======================== LISTA ORDENADA =============================')

    # Defino uma estrutura de repetição que vai do range 0 até o tamanho da lista
    for current in range(0, len(test)):
        if (by == 'title'):
            item = test[current].title
        elif (by == 'price'):
            item = test[current].price
        elif (by == 'pages'):
            item = test[current].pages
        elif (by == 'author'):
            item = test[current].author

        # Para cada repetição eu vou exibir o titulo, para confirmar que a lista está ordenada
        print(item)
