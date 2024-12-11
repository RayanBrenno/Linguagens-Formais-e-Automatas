"""
Desenvolva um programa que receba como entrada dois conjuntos A e B e um conjunto universo U. O programa deverá calcular a união, intersecção, diferença, complemento, conjunto das partes e produto cartesiano entre os conjuntos A e B. Imprima o resultado de cada conjunto. 
"""

import itertools


def uniao(a, b):
    final = []
    for x in a+b:
        if x not in final:
            final.append(x)
    return sorted(final)


def intersecacao(a, b):
    final = []
    for x in a:
        if x in b and x not in final:
            final.append(x)
    return sorted(final)


def diferenca(a, b):
    final = []
    for x in a:
        if x not in b and x not in final:
            final.append(x)
    return sorted(final)


def conjuntoDasPartes(a):
    final = []
    for i in range(len(a) + 1):
        for aux in itertools.combinations(a, i):
            if list(aux) not in final:
                final.append(list(aux))
    return final


def produtoCartesiano(a, b):
    final = []
    for x in a:
        for y in b:
            final.append([x, y])
    return sorted(final)


a = [2, 4]
b = [4, 5, 6]
u = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Uniao-> {uniao(a, b)}")
print(list(set(a) | set(b)))
print(f"Interseção-> {intersecacao(a, b)}")
print(list(set(a) & set(b)))
print(f"Diferença-> {diferenca(a, b)}")
print(list(set(a)-set(b)))
print(f"Diferença-> {diferenca(u, a)}")
print(list(set(u)-set(a)))
print(f"Conjunto das partes-> {conjuntoDasPartes(a)}")
print(f"Produto cartersiano-> {produtoCartesiano(a, b)}")