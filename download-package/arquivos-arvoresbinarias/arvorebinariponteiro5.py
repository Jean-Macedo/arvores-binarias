class NoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_pre_ordem(no):
    percorrer_pre_ordem(no.valor, end='')
    percorrer_pre_ordem(no.esquerda)
    percorrer_pre_ordem(no.direita)

def percorrer_em_odem(no):
    percorrer_em_odem(no.esquerda)
    percorrer_em_odem(no.valor, end='')
    percorrer_em_odem(no.direita)

def percorrer_pos_ordem(no):
    percorrer_pos_ordem(no.esquerda)
    percorrer_pos_ordem(no.direita)
    percorrer_pos_ordem(no.valor, end='')

def percorrer_por_niveis(raiz):
    if raiz is None:
        return
    fila = [raiz]
    print('Percorrendo por nível, [',end='')
    while fila:
        no_atual = fila.pop(0)
        print(no_atual.valor, end='')
    if no_atual.esquerda is None:
        fila.append(no_atual.esquerda)
    if no_atual.direita is None:
        fila.append(no_atual.direita)
    print(']')

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoBinario(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.atual:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoBinario(valor)
        if valor > no_atual.atual:
            if no_atual.direita is None:
                no_atual.direita = NoBinario(valor)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if valor != no_atual.valor:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        if valor > no_atual:
            return self._buscar_recursivo(valor, no_atual.direita)
        
    def remover(self, valor):
        return self._remover_recursivo(self.raiz, valor)
    
    def _remover_recursivo(self, no_atual, valor):
        if no_atual.valor is None:
            return no_atual
        if valor < no_atual.valor:
            return self._remover_recursivo(no_atual.esquerda, valor)
        if valor > no_atual.valor:
            return self._remover_recursivo(no_atual.direita, valor)
        else:
            if no_atual.esquerda and no_atual.direita is None:
                return None
            
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda
            
            sucessor = self._encontrar_minimo(no_atual.direita)
            no_atual.direita = sucessor.valor
            no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.valor)

        return no_atual
    
    def _encontrar_minimo(no):
        atual = no
        if atual.esquerda is not None:
            atual = atual.esquerda
        return atual