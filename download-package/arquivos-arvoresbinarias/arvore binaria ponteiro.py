class NoBinario:
    """O bloco de construção para uma Árvore Binária."""
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None  # Referência ("ponteiro") para o filho da esquerda
        self.direita = None   # Referência ("ponteiro") para o filho da direita

# --- FUNÇÕES DE PERCURSO (EXTERNAS À CLASSE) ---
def percorrer_pre_ordem(no):
    if no is None:
        return
    print(no.valor, end=' ')  # 1. Visita a raiz
    percorrer_pre_ordem(no.esquerda)  # 2. Visita a subárvore esquerda
    percorrer_pre_ordem(no.direita)  # 3. Visita a subárvore direita

def percorrer_em_ordem(no):
    if no is None:
        return
    percorrer_em_ordem(no.esquerda)  # 1. Visita a subárvore esquerda
    print(no.valor, end=' ')  # 2. Visita a raiz
    percorrer_em_ordem(no.direita)  # 3. Visita a subárvore direita

def percorrer_pós_ordem(no):
    if no is None:
        return
    percorrer_pós_ordem(no.esquerda)  # 1. Visita a subárvore esquerda
    percorrer_pós_ordem(no.direita)  # 2. Visita a subárvore direita
    print(no.valor, end=' ')  # 3. Visita a raiz

def percorrer_por_nivel(raiz):
    if raiz is None:
        print("Árvore vazia.")
        return
    
    # 1. Iniciar a fila (uma lista) com a raiz
    fila = [raiz]
    print("Percorrendo por nível: [", end="")
    
    # 2. Loop principal: continua enquanto a fila não estiver vazia
    while fila:
        # 3. Desenfileirar (Dequeue): Remove e obtém o primeiro elemento
        no_atual = fila.pop(0)
        print(no_atual.valor, end=' ')
        
        # 4. Enfileirar (Enqueue) os filhos
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)
    print("]")

# --- CLASSE ARVOREBINARIABUSCA ---
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Inserção (Recursiva)
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoBinario(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            # Ir para a esquerda
            if no_atual.esquerda is None:
                no_atual.esquerda = NoBinario(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        else:
            # Ir para a direita
            if no_atual.direita is None:
                no_atual.direita = NoBinario(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    # Busca (Recursiva)
    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if no_atual is None:
            return False  # Chegou ao fim de um galho, não encontrou
        
        if valor == no_atual.valor:
            return True  # Encontrou!
        
        if valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        else:
            return self._buscar_recursivo(valor, no_atual.direita)

    # Remoção
    def remover(self, valor):
        """Método público para remover um valor. A raiz é atualizada."""
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        # Passo 1: Buscar o nó
        if no_atual is None:
            return no_atual
        
        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_recursivo(no_atual.direita, valor)
        else:
            # Passo 2: Nó encontrado. Analisar os 3 casos.
            
            # Caso 1: Nó é uma folha (0 filhos)
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
            
            # Caso 2: Nó tem 1 filho
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda

            # Caso 3: Nó tem 2 filhos
            # 1. Encontrar o sucessor em ordem (menor nó da subárvore direita)
            sucessor = self._encontrar_minimo(no_atual.direita)
            # 2. Copiar o valor do sucessor para o nó atual
            no_atual.valor = sucessor.valor
            # 3. Remover o nó sucessor da subárvore direita
            no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.valor)
        
        return no_atual

    def _encontrar_minimo(self, no):
        """Auxiliar necessário para o Caso 3 da remoção."""
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
# --- SCRIPT DE TESTE (Baseado nos exemplos clássicos de Árvore Binária) ---

if __name__ == "__main__":
    # 1. Criar a árvore
    minha_arvore = ArvoreBinariaBusca()

    # 2. Inserir valores (Montando a árvore do slide)
    # Vamos inserir o 50 como raiz para ficar equilibrado
    valores = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserindo valores: {valores}")
    for v in valores:
        minha_arvore.inserir(v)

    print("\n--- TESTANDO OS PERCURSOS (Slides 171-175) ---")
    
    print("Pré-ordem (Raiz-Esq-Dir): ", end="")
    percorrer_pre_ordem(minha_arvore.raiz)
    
    print("\nEm-ordem (Esq-Raiz-Dir):  ", end="")
    percorrer_em_ordem(minha_arvore.raiz) # Deve imprimir em ordem crescente
    
    print("\nPós-ordem (Esq-Dir-Raiz): ", end="")
    percorrer_pós_ordem(minha_arvore.raiz)
    
    print("\n")
    percorrer_por_nivel(minha_arvore.raiz)

    print("\n--- TESTANDO A BUSCA (Slide 181) ---")
    valor_busca = 60
    encontrou = minha_arvore.buscar(valor_busca)
    print(f"O valor {valor_busca} está na árvore? {'Sim' if encontrou else 'Não'}")

    print("\n--- TESTANDO A REMOÇÃO (Slides 187-191) ---")
    # Removendo o 30 (que tem dois filhos: 20 e 40) - Caso 3
    print("Removendo o nó 30 (Caso de 2 filhos)...")
    minha_arvore.remover(30)
    
    print("Árvore após remover 30 (Em-ordem): ", end="")
    percorrer_em_ordem(minha_arvore.raiz)
    print("\n")