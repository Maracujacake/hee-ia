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


## 4. Busca Informada 

### 4.1 Branch and Bound

Branch and Bound (b&B), também conhecido como alg. de "força bruta" (não exatamente) inteligente, é um algoritmo que explora o espaço de soluções de maneira sistemática e evita considerar subespaços inviáveis, economizando tempo. Ele funciona como uma busca em árvore, onde cada nó representa uma subsolução parcial ou um estado do problema.

**Branch** (Ramifica, faz a árvore de estados a partir do estado atual) and **Bound** (Define um limite e poda o que for pior do que aquele limite ou, pelo menos, não o considera atualmente)

A partir de uma solução viável, ignoramos aquelas que pareçam mais custosas ou inviáveis, focando apenas no que for menor ou igual ao custo já obtido

[>> vídeo explicativo (créditos ao prof. Mário 😎) <<](https://youtu.be/1UPNxELq8Uw)

[>> leitura explicativa com exemplos <<](https://www.javatpoint.com/branch-and-bound)

[>> implementação do caixeiro viajante (python) <<]()

Tempo: 
 - Difícil de mensurar sem um problema
 - Para o problema do caixeiro viajante: No pior caso e com pode ineficaz ... O(n!) 😨
 - - Pois deve explorar todas as permutações de cidades possíveis e, como a poda se mostra ineficaz, continua testando exaustivamente
 - Caso a poda seja extremamente eficiente, pode-se chegar em soluções de O(n^2) ou até O(n log n) 👀

Traduzindo, depende do problema, dos dados do problema e depende também da função que define o bound


### 4.2 Best-First

O Best-First Search (Busca pelo Melhor Primeiro) é um algoritmo de busca informada, no qual a exploração do grafo é guiada por uma função de avaliação (heurística) que prioriza os nós que parecem ser mais promissores em relação ao objetivo.

O algoritmo vai ordernar e priorizar os valores dados pela heurística e não (somente) os pesos das arestas entre os nós, sendo assim, *dependendo da implementação*, pode não achar o resultado ótimo.

[>> vídeo de explicação com exemplo <<](https://youtu.be/i4MA_hFkKDg)

[>> implementação em python utilizando heap <<]()

[>> explicando o greedy-best-first <<](https://youtu.be/dv1m3L6QXWs)

*perceba que no vídeo, outra abordagem é utilizada, lançando mão de duas listas que salvam os nós e verificam constantemente os valores das heurísticas desses nós

### 4.3 Busca Gulosa

É um algoritmo relativamente simples, que apesar de rápido, infelizmente **não garante a solução ótima**. Ele funciona sempre **priorizando o caminho cuja heurística é menor**. MUITO parecido com o anterior, não é? Bom, algumas implementações do best-first costumam se parecer com o próximo algoritmo (A*), *onde além de levar em consideração o valor da heurística, ele leva também em consid. o custo entre os nós*, **já aqui isso não acontece**.

O termo "guloso" **não se refere a um tipo de busca específico** e sim a uma técnica de programação que também pode ser vista em programação dinâmica ou em outros algoritmos. Inclusive, na implementação em python do algoritmo anterior, a ideia geral utilizada é chamada de *"greedy-best-first"* pois combina as duas ideias. É interessante, né? *Não são classificações rígidas, mas sim um conjunto de ideias unificadas pra tentar otimizar algo tão comum quanto a busca de um elemento.*

### 4.4 Busca A*

