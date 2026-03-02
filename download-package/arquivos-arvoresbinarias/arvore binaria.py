class NoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # --- INSERÇÃO ---
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoBinario(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoBinario(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = NoBinario(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    # --- BUSCA ---
    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        return self._buscar_recursivo(valor, no_atual.direita)

    # --- REMOÇÃO ---
    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_recursivo(no_atual.direita, valor)
        else:
            # Caso 1: Nó folha
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
            
            # Caso 2: Um filho
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda

            # Caso 3: Dois filhos (Sucessor em ordem)
            sucessor = self._encontrar_minimo(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.valor)
        
        return no_atual

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

# --- MÉTODOS DE TRAVESSIA (FORA DA CLASSE OU DENTRO) ---
def percorrer_em_ordem(no):
    if no:
        percorrer_em_ordem(no.esquerda)
        print(no.valor, end=' ')
        percorrer_em_ordem(no.direita)

def percorrer_por_nivel(raiz):
    if raiz is None:
        return
    fila = [raiz]
    while fila:
        no_atual = fila.pop(0)
        print(no_atual.valor, end=' ')
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)

# Exemplo de Uso:
arvore = ArvoreBinariaBusca()
valores = [50, 30, 70, 20, 40, 60, 80]
for v in valores:
    arvore.inserir(v)

print("Em-ordem (Crescente):")
percorrer_em_ordem(arvore.raiz) # Saída: 20 30 40 50 60 70 80