class NoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoBinario(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if self.esquerda is None:
                no_atual.esquerda = NoBinario(valor)
        if valor > no_atual.valor:
            if self.direita is None:
                no_atual.direita = NoBinario(valor)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if valor != no_atual:
            return False
        if valor == no_atual:
            return True
        if valor < no_atual:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        if valor > no_atual:
            return self._buscar_recursivo(valor, no_atual.direita)
        
    def remover(self, valor):
        return self._remover_recursivo(self.raiz, valor)
    
    def _remover_recursivo(self, no_atual, valor):
        if no_atual is None:
            return no_atual
        if valor < no_atual.esquerda:
            return self._remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.direita:
            return self._remover_recursivo(no_atual.direita, valor)
        else:
            if no_atual.equerda and no_atual.direita is None:
                return None
            
            if no_atual.esquerda is None:
                return no_atual.direita
            if no_atual.direita is None:
                return no_atual.esquerda
            
            sucessor = self._encontrar_minimo(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.valor)
            
        return no_atual

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual