import numpy as np
import heapq as heap

# verifica o custo expandindo os nós (soma até a distancia de tds os outros nós)
# path[A] -> vai verificar a distância de nó por nó e ir somando em bound
def calculate_bound(path, matrix, numero_cidades):
    bound = 0
    visited = set(path)

    for i in range(numero_cidades):
        # se já tiver visitado a cidade, não calculamos o bound para ela
        if i in visited:
            continue

        # soma o custo da cidade atual até a j-ésima cidade NÃO VISITADA
        min_vertice = min([matrix[i][j] for j in range(numero_cidades) if j not in visited and matrix[i][j] != float('inf') ], default = 0)
        bound += min_vertice
    return bound


# O problema do caixeiro viajante aqui é definido por: percorrer todas as cidades e retornar à inicial
# com o menor custo possível.
def caixeiro_viajante(matrix):
    n = len(matrix) # numero de cidades (numero de colunas da matriz)
    melhor_custo = float('inf') # vamos definir "infinito" como: não tem caminho até essa cidade ou é ela mesma
    melhor_caminho = []

    fila_prioridade = []

    # a estrutura principal aqui, diferente da BFS e DFS, é o heap, pois ordena-se a cada inserção
    heap.heappush( fila_prioridade, (0, 0, [0]) )

    while(fila_prioridade):
        bound, custo_atual, path = heap.heappop( fila_prioridade ) 

        # não avaliamos caminhos que não sejam promissores, isto é, caminhos que não apresentam melhor resultado
        if(bound >= melhor_custo):
            continue

        # quando já verificamos todas as cidades, fazemos uma ultima verificação adicionando a primeira cidade na conta 
        if( len(path) == n ):
            custo_total = custo_atual + matrix[path[-1]][path[0]] # path[-1] se refere ao ultimo elemento da lista path
            if(custo_total < melhor_custo):
                melhor_custo = custo_total + matrix[path[-1]][path[0]]
                melhor_caminho = [path] + [path[0]]
            continue

        # isto é, dada  uma linha da matriz, pegue todas as cidades dessa linha (todas as cdds que a cidade em questão tem conexão)
        # verificamos isso pegando a ultima cidade visitada presente no path
        for prox_cidade in range (n):
            if(prox_cidade not in path and matrix[path[-1]] [prox_cidade] != float('inf')):
                novo_custo = custo_atual + matrix[path[-1]] [prox_cidade]
                # calculamos a fronteira dessa cidade
                novo_bound = novo_custo + calculate_bound( path + [prox_cidade], matrix, n )
                # adicionamos no heap, caso a fronteira seja maior do que o que temos agora, será adicionado no final do heap
                heap.heappush(fila_prioridade, (novo_bound, novo_custo, path + [prox_cidade]) )

    return melhor_custo, melhor_caminho