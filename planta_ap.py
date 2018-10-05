# Gera uma grid quadrada, um grafo, utilizando tuplas para guardar as posições
# Não é guardado as bordas, e sim, calcula-se os vizinhos pela função "vizinhos"
class GridQuadrada:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.paredes = []
    
    def limites(self, id):				# Separa os limites, para dar apenas os vizinhos adjacentes
        (x, y) = id						# Assim, ele não vai retornar um vizinha que esteja 2 quadrados de distância
        return 0 <= x < self.largura and 0 <= y < self.altura # retornando apenas o vizinho exatamente ao lado do atual
    
    def passavel(self, id):				# Simplesmente verifica se o vizinho não é uma parede
        return id not in self.paredes 	# Ele retorna verdadeiro de o id fornecido não estiver na lista de paredes
    
    def vizinhos(self, id): 			# Separa os vizinhos adjacentes ao atual, filtrando paredes
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        #if (x + y) % 2 == 0: results.reverse() # apenas estética, muda praticamente nada
        results = filter(self.limites, results) # filtra para separar apenas os adjacentes
        results = filter(self.passavel, results) # filtra para mostrar só os que não são paredes
        return results

# Classe que herda da classe GridQuadrada e adiciona
# pesos para os movimentos
class GridComPesos(GridQuadrada):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.pesos = {}
    
    def custo(self, from_node, to_node):
        return self.pesos.get(to_node, 1)

planta = GridComPesos(10, 10)
planta.paredes = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
planta.pesos = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6), 
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6), 
                                       (5, 7), (5, 8), (6, 2), (6, 3), 
                                       (6, 4), (6, 5), (6, 6), (6, 7), 
                                       (7, 3), (7, 4), (7, 5)]}