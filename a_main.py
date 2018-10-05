from a_star import *
from planta_ap import *
from priority_queue import *

start, end = (1, 4), (7, 8)
veio_de, custo_total = a_star(planta, start, end)
mostrar_grid(planta, largura=3, aponta_para=veio_de, inicio=start, final =end)
print()
mostrar_grid(planta, largura=3, numero=custo_total, inicio=start, final=end)
print()
mostrar_grid(planta, largura=3, caminho=reconstruir_caminho(veio_de, inicio=(1, 4), final=(7, 8)))