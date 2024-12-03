import numpy as np
from b_and_b import caixeiro_viajante

# Define uma matriz de custo para o teste
cost_matrix = np.array([
    [float('inf'), 10, 15, 20],
    [10, float('inf'), 35, 25],
    [15, 35, float('inf'), 30],
    [20, 25, 30, float('inf')]
])

# Executa o algoritmo
melhor_custo, melhor_caminho = caixeiro_viajante(cost_matrix)

# Exibe os resultados
print("Melhor custo encontrado:", melhor_custo)
print("Melhor caminho encontrado:", melhor_caminho)
