from a_star import *
from planta_ap import *
from priority_queue import *

# Na função print_grid, estamos utilizando a biblioteca Colorama, para imprimir cores nos textos
# dos objetos na planta, para ficar melhor a visualização. Não sei dizer exatamente em qual versão
# do Python ela passou a ser introduzida por padrão. Sei que em algumas ela não está presente (antes
# da versão 3 é certeza absoluta) porém, não sei dizer em qual ver da 3 ela foi introduzida. Então,
# dê algum erro por não estar introduzida, caso seu Python não esteja na versão mais atual. Estamos
# utilizando o Python 3.7, e nela o Colorama já vem introduzido por padrão, então, caso dê erro,
# por favor, verifique se seu Python está na versão mais atual, caso não esteja, é bom atualizá-lo.
# Há meios de instalar apenas aquela biblioteca específica, mas, uma vez que a linguagem possui um 
# update disponível e a linguagem passa a ser introduzida por padrão (tirando que é muito mais chato
# e complicado instalar ela sozinha), torna-se mais interessante apenas atualizar a linguagem.
# Não sei também como irá rodar no windows, pois utilizei apenas no Linux (Ubuntu 18.04 LTS), mas
# parece que há algum problema no windows com essa biblioteca.

####################################################################################################

# Esse é o pedaço mais simples do programa. Aqui só está sendo chamado as funções e classes dos
# outros arquivos. A ideia aqui é: como não temos um sensor implementado, então há uma entrada
# manual de dados para indicar onde o sensor disparou. Há um menu, onde se escolhe o local onde
# o sensor disparou e que possui uma opção, ou a opção 5 para se sair. O código todo está dentro
# de um laço while, ou seja, irá se repetir enquanto a opção 5 (sair) não for escolhida.
# Há uma opção escondida, a opção de número 0, onde nela se é possível escolher qualquer ponto 
# da planta, porém, isso pode gerar erros, pois caso seja escolhido uma parede, será impossível
# se chegar ao destino, então, o programa irá dar um erro e fechar. Isso poderia ser tratado
# se verificando na hora que os pontos são inseridos se a tupla está na lista de paredes, se
# estiver, não é chamado o mostrar_grid dela, logo, não é traçado o melhor caminho.
# No fim, só é chamado todos os mostrar_grid's para apresentar o resultado de todas as formas.

def main(): #{
    opcao = 0
    
    while opcao != 5:
        print('1 - Quarto')
        print('2 - Banheiro')
        print('3 - Sala')
        print('4 - Cozinha')
        print('5 - Sair')
        print()
        opcao = int(input('Opção: '))

        if opcao == 1:
            a, b = 36, 11
        elif opcao == 2:
            a, b = 42, 26
        elif opcao == 3:
            a, b = 10, 22
        elif opcao == 4:
            a, b = 13, 6
        elif opcao == 0:
            a = int(input('a = '))
            b = int(input('b = '))
        elif opcao == 5:
            print("\n" * 2)
            print('Saindo.')
            print("\n" * 2)
            break
        elif opcao != 5 and opcao != 4 and opcao != 3 and opcao != 2 and opcao != 1 and opcao != 0:
            print("\n")
            print('****OPÇÃO INVÁLIDA!!!****')
            print("\n")
            continue

        start, end = (0, 24), (a, b)
        veio_de, custo_total = a_star(planta, start, end)
        print("\n" * 3)
        mostrar_grid(planta)
        print("\n" * 3)
        mostrar_grid(planta, largura = 2, aponta_para = veio_de, inicio = start, final = end)        
        print("\n" * 3)
        mostrar_grid(planta, largura = 3, numero = custo_total, inicio = start, final = end)
        print("\n" * 3)
        mostrar_grid(planta, largura = 2, caminho = reconstruir_caminho(veio_de, inicio = start, final = end))
        print()
#}

if(__name__ == "__main__"): #{
    main();
#}

