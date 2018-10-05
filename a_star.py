from planta_ap import *
from priority_queue import *
from print_grid import *
import collections

# Calcula a distância estimada até o final, sendo que este é o H do nosso
# F = G + H, sendo que G é o custo para o vizinho apenas, e H é a distância
# do vizinho até o final, sendo que assim, o F resultante (no caso, dentro da função a_star
# ele está chamado de prioridade, para servir como uma forma de adicionar no topo da PriorityQueue
# os objetos de maior prioridade) seja o valor mais confiável para a distância do
# incio até o final. No Dijkstra, ele apenas considera o melhor caminho, sem considerar a
# posição/direção na qual está o final, porém, aqui, a ideia dessa função é levar este fato
# em consideração, portanto, enquanto o Dijkstra irá verificar praticamente todas as possibilidades
# enquanto não encontra o destino, o A* irá focar em ir na direção da posição final
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# Eu recebo a planta na qual estamos trabalhando e as posições iniciais e finais
def a_star(planta, inicio, final):
    fronteira = PriorityQueue()     # Fronteira vem da ideia de que precisamos manter um controle de um anel que se expande em volta do ponto em observação, uma fronteira
    fronteira.put(inicio, 0)        # Adiciono a fronteira com a posição inicial e peso zero
    veio_de = {}                    # Estou criando um dicionário para armazenar as posições da onde vim
    custo_total = {}                # Dicionário para armazenar o custo
    veio_de[inicio] = None          # A posição do inicio é vazio, pois ninguém veio antes
    custo_total[inicio] = 0         # O custo total do início é 0, pois não andei aidna
    
    while not fronteira.empty():    # Enquanto a lista fronteira não estiver vazia, ou seja, enquanto eu ainda tiver vizinhos para analisar, eu continuo no loop
        atual = fronteira.get()     # O objeto que estou analisando agora recebe o item no topo da lista de prioridades fronteira
        
        if atual == final:          # Se ele for a posição final de destino, eu saio do loop
            break
        
        for next in planta.vizinhos(atual):                                 # Para cada possibilidade dentro dos vizinhos adjacentes da minha posição atual
            new_cost = custo_total[atual] + planta.custo(next, final)       # Eu calculo um novo custo, que é o custo total até agora + o custo para esse vizinho
            if next not in custo_total or new_cost < custo_total[next]:     # Se o proximo vizinho não está no custo total ou o novo custo  for menor que o custo para o próximo vizinho
                custo_total[next] = new_cost                                # O custo total vira o novo custo
                prioridade = new_cost + heuristic(final, next)              # Meu F (prioridade) vira o novo custo mais a função heuristica (distancia do vizinho até o destino)
                fronteira.put(next, prioridade)                             # Adiciono na lista de prioridade o meu próximo vizinho e com seu valor F (prioridade)
                veio_de[next] = atual                                       # A próxima posição do meu veio_de vira a posição atual
    
    return veio_de, custo_total     # Quando terminar, devolvo o meu dicionário veio_de (os caminhos) e o dicionário do custo_total (com os custos de cada posição)