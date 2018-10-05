from a_star import *
from planta_ap import *
from priority_queue import *

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
        print("\n" * 5)
        print('Saindo.')
        print("\n" * 3)
        break
    elif opcao != 5 and opcao != 4 and opcao != 3 and opcao != 2 and opcao != 1 and opcao != 0:
        print("\n" * 5)
        print('****OPÇÃO INVÁLIDA!!!****')
        print("\n" * 3)
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