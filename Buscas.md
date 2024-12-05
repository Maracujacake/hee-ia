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

Como apontado em algumas explicações anteriores, a diferença agora é que consideraremos sempre o valor da **heurística somado com o custo entre os nós**

f(n) = g(n) + h(n) -> entenda como: custo_total_de_vdd = ( custo_entre_nós + heuristica_do_nó )

[>> video explicativo com exemplo <<](https://youtu.be/PzEWHH2v3TE)

Visualização do algoritmo em diversos cenários:

<img src="https://miro.medium.com/v2/resize:fit:1400/1*l0IkrbNLnkCB1VzDq2Qy7A.gif">

<br>

[>> implementação em python <<]()

**Qual a complexidade do algoritmo?** Bom, quando se trata de **algoritmos que dependem da heurística** pra alguma coisa, é natural pensar que **sua complexidade TAMBÉM vá depender dela**, mas em casos gerais:

tempo: O(b^d)

espaço: O(b^d)

onde b é o **tamanho do menor caminho** e d é o **número de ligações possíveis a cada nó** do menor caminho, afinal, temos que fazer a verificação de nó em nó enquanto construímos a solução ótima.

## 5. Busca Local (e por que ela é diferente das anteriores)

#### Ao contrário das buscas anteriores em que usávamos para, por exemplo, encontrar um caminho que levasse a melhor solução, aqui estamos falando de ferramentas que não são feitas para achar um caminho e sim uma solução única e satisfatória. Essa solução nem tem a obrigação de ser ótima, apenas satisfatória para o limite que lhe foi imposta.

#### Na maioria das vezes, os algoritmos anteriores (A*, Branch and Bound, Greedy-Best-First) usávamos uma fila de prioridade (heap) como estrutura de dados principal que ditava o comportamento do algoritmo, aqui a coisa muda de figura. Como não precisamos de um caminho e sim apenas uma solução, podemos implementar utilizando somente um estado (uma variável qualquer) e ir alterando o valor da mesma conforme formos encotrando melhores soluções.

### 5.1 Hill Climbing

*O Algoritmo Subida da Encosta do inglês Hill Climbing (HC) é **baseado na ideia de subida do Monte Everest em meio de um nevoeiro denso durante uma crise de amnésia**, onde o objetivo é **chegar no pico mais alto** apenas **examinando os locais mais próximos** (vizinhos) **esquecendo os caminhos anteriores** e **termina quando alcança um pico em que nenhum vizinho tenha o valor mais alto*** - Professor Alan 👨‍🏫

(por incrivel que pareça, é uma descrição MUITO precisa do que o algoritmo faz)

[>> *video com exemplos <<](https://youtu.be/VoUotaCmDk4)

*Como explicado, o algoritmo pode chegar a um platô por conta de valores iguais de heurísticas e ficar perdido, no entanto, isso não o faz menos útil. Acaba dependendo muito mais das informações/dados que você tem sobre o problema.

### 5.2 Simulate Annealing


### 5.3 Local Beam


### 5.4 Algoritmos Genéticos