# Buscas em Inteligência Artificial

 A busca é uma das técnicas fundamentais na Inteligência Artificial (IA) para resolução de problemas. Ela permite encontrar soluções em espaços de estados, que podem ser representados como grafos ou árvores. Os algoritmos de busca são divididos em buscas não informadas e buscas informadas, de acordo com a quantidade de informação adicional usada durante o processo de exploração. Vamos explorar os principais conceitos e algoritmos.


## 1. Espaço de estados

O espaço de estados é uma representação abstrata de **todos os estados possíveis** de um problema e as transições entre eles. Ele é frequentemente representado como um grafo:

Cada **nó** representa um **estado**.
Cada **aresta** representa uma **ação ou transição entre estados**.


Exemplo:
No problema de um labirinto:


<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Graph_based_maze_animation.gif">

*no gif em questão não há direção entre as arestas, mas vamos fingir que essa direção existe*

Um nó pode representar uma posição no labirinto.
Uma aresta pode representar um movimento (esquerda, direita, cima ou baixo).


## 2. Tipos de Busca

### 2.1 Busca Não Informada

Também chamada de **busca cega**, não utiliza nenhuma informação específica sobre o problema além do próprio grafo. Exemplos incluem:


- Busca em Largura (BFS).
<a href="https://github.com/Maracujacake/hee-ia/blob/main/Implementa%C3%A7%C3%B5es/BuscaLargura/javab/BuscaLargura.java">Implementações em java</a>

- Busca em Profundidade (DFS).

- Busca com Custo Uniforme.


### 2.2 Busca Informada

Utiliza informações heurísticas* para guiar a exploração do espaço de estados, geralmente tornando a busca mais eficiente. Exemplos incluem:

 *como heurística, entenda

- Busca Gulosa.

- Algoritmo A*.




## 3. Busca Não Informada

### 3.1 Busca em Largura (BFS)

A BFS (*Breadth-First Search*) **explora todos os nós em um nível** antes de passar para o próximo. Ela é implementada usando uma **fila** (FIFO) e garante encontrar o caminho mais curto em um grafo não ponderado.

V = numero de vértices

E = numero de arestas ("E" por causa do "edges" em ingles)

Complexidade de tempo: *O (V + E)*

Complexidade de espaço: Alto, deve ter todos os nós do nível atual armazenados numa fila, assim como os nós seguintes

Exemplo:

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif">


### 3.2 Busca em Profundidade (DFS)

A DFS **segue um ramo até o final** antes de voltar e explorar outro. Ela é implementada com uma **pilha** (LIFO) ou recursão.

Complexidade de tempo: *O (V + E)*

Complexidade de espaço: Levemente menor que a BFS em alguns casos, pois não precisa salvar todos os V de um nível e do próximo (no entanto, cuidado com os grafos "linguiça");

Exemplo: 

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif">


### 3.3 Busca com Custo Uniforme

A busca com custo uniforme **expande o nó com o menor custo acumulado**. É ideal para problemas onde cada transição tem um custo associado.

Exemplo:

*Encontrar o caminho mais barato em um grafo rodoviário com pedágios*

Tempo: 𝑂(𝑉 + 𝐸 log⁡𝑉)*

*Visita todos os vértices uma vez e, pra cada aresta com custo, pode-se mudar a prioridade no heap (estrutura utilizando comumente nesses algoritmos) e cada operação leva logV (log de vértices) para ser realizada.

Espaço: Proporcional ao tamanho do grafo.

https://youtu.be/XyoucHYKYSE - visualização do algoritmo