package javab;
import javab.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class BuscaLargura {


    /*
     * Um grafo pode ser representado implicitamente como um vetor, 
     * onde (2*i+1) e (2*i+2) representam filho ESQUERDO e DIREITO respectivamente
     * 
     * vetor = [10, 15, 20, 30, 25, 35, 40]
     * 
     * 10 -> 15 e 20, 15 -> 30 e 25, 20 -> 35 e 40
     */
     
    // utilizando árvore implicita como vetor
    public boolean achouElemento(int[] grafo, int objetivo){
        List<Integer> fila = new ArrayList<>(); // a fila faz o controle para que acessemos os nós do mesmo nível
        fila.add(0);

        while(!fila.isEmpty()){
            int indiceAtual = fila.remove(0); // pegamos o indice na posicao 0 da fila, a mais antiga

            if(indiceAtual < 0 || indiceAtual >= grafo.length) continue; // caso, ao adicionar os filhos, coloquemos um num maior que o tamanho do grafo

            if(grafo[indiceAtual] == objetivo) return true;

            int filhoEsquerdo = 2 * indiceAtual + 1;
            int filhoDireito = 2 * indiceAtual + 2;
            
            if(filhoEsquerdo < grafo.length ) fila.add(filhoEsquerdo);
            if(filhoDireito < grafo.length) fila.add(filhoDireito);
        }
        return false; // passou por todos os nós e não achou o objetivo
    }



    // utilizando uma estrutura de árvore
    public boolean achouElemento(TreeNode raiz, int objetivo){
        List<TreeNode> fila = new ArrayList<>(); // java tem uma estrutura de fila e pilha já prontas, optei por arraylist apenas para facilitar explicação
        if(raiz == null) return false;
        fila.add(raiz);

        while(!fila.isEmpty()){
            TreeNode atual = fila.remove(0);

            if(atual.val == objetivo) return true;

            if(atual.esq != null) fila.add(atual.esq);
            if(atual.dir != null) fila.add(atual.dir);
        }
        
        return false;
    }



    // versão recursiva
        // utilizando uma estrutura de árvore
        public boolean achouElementoR(TreeNode raiz, int objetivo){
            if(raiz == null) return false;    
            if(raiz.val == objetivo) return true;


            boolean esq = false;
            esq = achouElementoR(raiz.esq, objetivo); 
            boolean dir = false;
            dir = achouElementoR(raiz.dir, objetivo);
            
            return esq || dir;
        }











    // Função principal para testar
    public static void main(String[] args) {
        BuscaLargura busca = new BuscaLargura();

        // Representação como vetor (árvore implícita)
        int[] grafo = {10, 15, 20};

        System.out.println("Teste com vetor (árvore implícita):");
        System.out.println(busca.achouElemento(grafo, 25)); // true
        System.out.println(busca.achouElemento(grafo, 50)); // false

        // Representação como TreeNode (árvore explícita)
        TreeNode raiz = new TreeNode(10);
        raiz.esq = new TreeNode(15);
        raiz.dir = new TreeNode(20);
        raiz.esq.esq = new TreeNode(30);
        raiz.esq.dir = new TreeNode(25);
        raiz.dir.esq = new TreeNode(35);
        raiz.dir.dir = new TreeNode(40);

        System.out.println("\nTeste com TreeNode (busca iterativa):");
        System.out.println(busca.achouElemento(raiz, 25)); // true
        System.out.println(busca.achouElemento(raiz, 50)); // false

        System.out.println("\nTeste com TreeNode (busca recursiva):");
        System.out.println(busca.achouElementoR(raiz, 25)); // true
        System.out.println(busca.achouElementoR(raiz, 50)); // false
    }
}