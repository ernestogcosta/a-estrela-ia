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

planta = GridComPesos(50, 30)
planta.paredes = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), 
                  (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0),
                  (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0), (30, 0),
                  (31, 0), (32, 0), (33, 0), (34, 0), (35, 0), (36, 0), (38, 0), (39, 0), (40, 0), (37, 0),
                  (41, 0), (42, 0), (43, 0), (44, 0), (45, 0), (46, 0), (47, 0), (48, 0), (49, 0), 
                  (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
                  (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21),
                  (0, 22), (0, 26), (0, 27), (0, 28), (0, 29),
                  (49, 0), (49, 1), (49, 2), (49, 3), (49, 4), (49, 5), (49, 6), (49, 7), (49, 8), (49, 9),
                  (49, 10), (49, 11), (49, 12), (49,13), (49, 14), (49, 15), (49, 16), (49, 17), (49, 18),
                  (49, 19), (49, 20), (49, 21), (49,22), (49, 23), (49, 24), (49, 25), (49, 26), (49, 27),
                  (49, 28), (49, 29),
                  (0, 29), (1, 29), (2, 29), (3, 29), (4, 29), (5, 29), (6, 29), (7, 29), (8, 29), (9, 29),
                  (10, 29), (11, 29), (12, 29), (13, 29), (14, 29), (15, 29), (16, 29), (17, 29), (18, 29),
                  (19, 29), (20, 29), (21, 29), (22, 29), (23, 29), (24, 29), (25, 29), (26, 29), (27, 29),
                  (28, 29), (29, 29), (30, 29), (31, 29), (32, 29), (33, 29), (34, 29), (35, 29), (36, 29), 
                  (37, 29), (38, 29), (39, 29), (40, 29), (41, 29), (42, 29), (43, 29), (44, 29), (45, 29),
                  (46, 29), (47, 29), (48, 29), (49, 29),
                  (36, 20), (36, 21),(36, 22), (36, 23), (36, 24), (36, 28), (36, 29),
                  (36, 20), (37, 20), (38, 20), (39, 20), (40, 20), (41,20), (42, 20), (43, 20), (44, 20), (45, 20), (46, 20), (47, 20), (48, 20),
                  (35, 20), (34, 20), (33, 20), (29, 20), (28, 20), (27, 20), (26, 20), (25, 20), (24, 20),
                  (24, 19), (24, 18), (24, 17), (24, 16), (24, 15), (24, 14), (24, 13), (24, 12), (24, 11), (24, 10),
                  (24, 9), (24, 8), (24, 7), (24, 6), (24, 6), (24, 5), (24, 4), (24, 3), (24, 2), (24, 1),
                  (1, 13), (2, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13), (11, 13), (12, 13), (13, 13), (14, 13),
                  (15, 13), (16, 13), (17, 13), (18, 13), (19, 13), (20, 13), (21, 13), (22, 13), (23, 13)]