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
    if no is None:
        return
    percorrer_pos_ordem(no.esquerda)
    percorrer_pos_ordem(no.direita)
    percorrer_pos_ordem(no.valor, end='')

def percorrer_por_nivel(raiz):
    if raiz is None:
        return
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