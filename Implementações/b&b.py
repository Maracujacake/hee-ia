import numpy as np
import heapq as heap

def calculate_bond(path, matrix, numero_cidades):
    bound = 0
    visited = set(path)

    for i in range(n):
        if i in visited:
            continue
        # define a cidade com menor caminho a partir da cidade que estamos agora (i)
        # explicação: pegue todos os elementos da linha i e, caso nao esteja em visitado, escolha o menor
        #             não pode ser float('inf') pois isso signif. que é da cidade para ela mesma
        min_vertice = min( [matrix[i][j] for j in range n if j not in visited and matrix[i][j] != float('inf')], default = 0)
        bound += min_vertice
    return bound

def caixeiro_viajante(matrix):
    n = len(matrix)
    melhor_custo = float('inf')
    melhor_caminho = []

    fila_prioridade = []

    heap.heappush( fila_prioridade, (0, 0, [0]) )
#[...] tbc