import heapq
import collections

# Funciona como uma lista, porém, ele irá adicionar as posições dependendo de sua prioridade
# Portanto, em vez de adicionar na ordem de adição, como uma pilha normal, ele irá organizar
# em relação aos valores de prioridade.

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]