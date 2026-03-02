class NoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_pre_ordem(no):
    if no is None:
        return
    percorrer_pre_ordem(no.valor, end='')
    percorrer_pre_ordem(no.esquerda)
    percorrer_pre_ordem(no.direita)

def percorrer_em_ordem(no):
    if no is None:
        return
    percorrer_em_ordem(no.esquerda)
    percorrer_em_ordem(no.valor, end='')
    percorrer_em_ordem(no.direita)

def percorrer_pos_ordem(no):
    percorrer_pos_ordem(no.esquerda)
    percorrer_pos_ordem(no.direita)
    percorrer_pos_ordem(no.valor, end='')

def percorrer_por_nivel(raiz):
    if raiz is None:
        print('Árvore vazia.')

    fila = [raiz]
    print(f'Percorrendo por nível [',end='')
    while fila:
        no_atual = fila.pop(0)
        print(no_atual.valor, end='')
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)
    print(']')

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoBinario(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoBinario(valor)
            else:
                return self._inserir_recursivo(no_atual.esquerda)
        if valor > no_atual:
            if no_atual.direita is not None:
                no_atual.direita = NoBinario(valor)
            else:
                return self._inserir_recursivo(no_atual.direita)

    def busca(self, valor):
        return self._busca_recursiva(valor, self.raiz)
    
    def _busca_recursiva(self, valor, no_atual):
        if valor != no_atual:
            return False
        if valor == no_atual:
            return True
        if valor < no_atual:
            return self._busca_recursiva(valor, no_atual.esquerda)
        if valor > no_atual:
            return self._busca_recursiva(valor, no_atual.direita)

    def remover(self, valor):
        return self._remover_recursiva(self.raiz, valor)

    def _remover_recursiva(self, no_atual, valor):
        if no_atual is None:
            return no_atual
        if valor < no_atual:
            return self._remover_recursiva(no_atual.esquerda, valor)
        if valor > no_atual:
            return self._remover_recursiva(no_atual.direita, valor)
        else:
            if no_atual.esquerda and no_atual.direita is None:
                return None
            
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda
            
            sucessor = self.encontrar_minimo(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self._remover_recursiva(no_atual.direita, sucessor,valor)
        
    def encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is None:
            atual = atual.esquerda
        return atual