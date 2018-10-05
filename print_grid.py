import collections
from colorama import *

# A função desenhar recebe a planta na qual a busca está sendo feita
# recebe o id do grafo, um "style", que funciona como a forma como se
# deseja printar todo o grafo com os caminhos, além de receber a largura
# das "colunas" (na verdade, das linhas, mas, como forma de melhorar a visão,
# a matriz é invertida (com a fun~ção .reverse), então as linhas viram colunas
# e as colunas viram linhas)
# É possível se printar de 3 formas: numeros (custos), sentido e o melhor caminho gerado
# isso é feito através do style, explicado melhor na função mostrar_grid
def desenhar(planta, id, style, largura):
    r = "."
    if 'numero' in style and id in style['numero']:     # Se na tupla recebida tiver nela 'numero', e tiver um id,
        r = "%d" % style['numero'][id]                  # nesse style, então, o r receberá o valor contido no id
        
    if 'aponta_para' in style and style['aponta_para'].get(id, None) is not None:
        (x1, y1) = id                                   # A ideia é a mesma do if anterior, porém, em vez de verificar
        (x2, y2) = style['aponta_para'][id]             # se 'numero' está dentro de style, ele vê se 'aponta_para' está
        if x2 == x1 + 1: r = ">"                        # então, é atribuído "setas" na direção da onde a busca veio
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    
    if 'caminho' in style and id in style['caminho']:   # Mesmo esquema, porém com o melhor caminho encontrado
        r = "@"                                         # só será printado o caminho, diferente das outras oções

    if 'inicio' in style and id == style['inicio']:       # Marca a posição inicial com um A
        r = "A"

    if 'final' in style and id == style['final']:         # Marca a posição final com um Z
        r = "Z"

    if id in planta.paredes:                            # Marca as paredes com #
        r = "#" * largura

    return r

# É a função que de fato printa o grafo. Nela, se recebe a planta na qual se está trabalhando,
# a largura, que caso não seja especificada, será 2, e um kwargs (KeyWord ARGuments), que funciona
# de forma similar a uma tupla, sendo que com isso, é possível se passar 2 ou mais informações dentro
# de style, dependendo do caso. 
# Então, utiliza-se um for duplo para se percorrer toda a matriz, primeiro o y, uma vez que, como
# explicado anteriormente, a matriz é invertida, depois o x, percorrendo até as dimensões máximas da matriz,
# e a cada iteração se chama a função desenhar para printar da forma escolhida.
def mostrar_grid(planta, largura=2, **style):
    colorama.init()
    for y in range(planta.altura):
        for x in range(planta.largura):
            a = desenhar(planta, (x, y), style, largura)
            if a == '@':
               print(Fore.CYAN + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            elif a == '#' * largura:
                print(Fore.GREEN + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            elif a == 'A' or a == 'Z':
                print(Fore.RED + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            elif a == '>' or a == '<' or a == '^' or a == 'v':
                print(Fore.YELLOW + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            elif a == '.':
                print(Fore.WHITE + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            elif a.isnumeric:
                print(Fore.MAGENTA + "%%-%ds" % largura % a, end="" + Style.RESET_ALL)
            else:
                print("%%-%ds" % largura % a, end="")
            #print("%%-%ds" % largura % desenhar(planta, (x, y), style, largura), end="")
                                  
        print()

# Serve para retraçar o melhor caminho encontrado, ele recebe como parâmetros a lista
# veio_de e as posições incio e final. O código começa na posição final, e retraça o 
# melho caminho até a posição incial.
def reconstruir_caminho(veio_de, inicio, final):
    atual = final               # inicia-se com o final
    caminho = []                # lista na qual o melhor caminho será armazenado
    while atual != inicio:      # enquanto a posição que estou analisando não for a posição inicial:
        caminho.append(atual)   # adiciono na minha lista do caminho a posição atual
        atual = veio_de[atual]  # a posição atual passa a ser recebe a posição seguinte da lista veio_de 
    caminho.append(inicio)      # caso seja o início, eu saio do while, adiciono inicio ao meu caminho
    return caminho              # devolvo então o meu caminho para ser printado  