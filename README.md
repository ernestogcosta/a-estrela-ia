# Algoritmo de A*

O algoritmo de A* é uma versão melhorada do algoritmo de Dijkstra. Enquanto no Dijkstra ele busca o menor caminho dentre todas as possibilidades, o algoritmo de A* faz uma busca dando preferência por um caminho que, em relação ao destino, terá a menor distância. No Dijkstra, ele pode acabar seguindo para mais longe, caso o vizinho tenha o menor caminho em relação a ele mesmo. No A*, caso o vizinho que tenha o menor caminho em realação ao ponto atual esteja se distanciando do destino, o algoritmo irá preferir outro vizinho, mesmo que em relação ao atual esse vizinho tenha uma distância maior mas que possua a menor distância entre ele e o destino dentre as dadas possibilidades.

Nesse trabalho, desenvolveu-se um algoritmo utilizando A* para se traçar caminhos da porta da frente de uma casa inteligente até o comodo no qual um alarme de emergência foi disparado. Na fase inicial, não são utilizados sensores de fato, utilizando-se assim um menu com as opções de cada recinto, assim, quando se escolhe um recinto, o código é tratado como se um sensor tivesse sido disparado naquele cômodo, assim traçando o melhor caminho até ele.

#### Referências

[Red Blob Games - Implementação](https://www.redblobgames.com/pathfinding/a-star/implementation.html). 

 [Red Blob Games - Introdução](https://www.redblobgames.com/pathfinding/a-star/introduction.html). 

 [Geeks For Geeks](https://www.geeksforgeeks.org/a-search-algorithm). 

 [Let's Learn Python #20 - A* Algorithm](https://www.youtube.com/watch?v=ob4faIum4kQ).

 [A* (A Star) Search Algorithm - Computerphile](https://www.youtube.com/watch?v=ySN5Wnu88nE). 

 [A* Pathfinding (E01: algorithm explanation)](https://www.youtube.com/watch?v=-L-WgKMFuhE).

 [StackOverflow - Change Color Print](https://stackoverflow.com/questions/5890437/change-color-of-individual-print-line-in-python-3-2#5890967).