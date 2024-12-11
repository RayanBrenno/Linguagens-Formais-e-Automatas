import sys


def q0(charToTrade, morseBase, index):
    dic = {".": q1, "-": q2, "/": q40, "#": q41}
    return dic[morseBase[index]]("", morseBase, index+1)


def trade(charToTrade, morseBase, index):
    morseBase[index-1] = charToTrade
    return q0("", morseBase, index)


def q1(charToTrade, morseBase, index):
    dic = {".": q3, "-": q4, "|": trade}
    return dic[morseBase[index]]("E", morseBase, index+1)


def q2(charToTrade, morseBase, index):
    dic = {".": q5, "-": q6, "|": trade}
    return dic[morseBase[index]]("T", morseBase, index+1)


def q3(charToTrade, morseBase, index):
    dic = {".": q7, "-": q8, "|": trade}
    return dic[morseBase[index]]("I", morseBase, index+1)


def q4(charToTrade, morseBase, index):
    dic = {".": q9, "-": q10, "|": trade}
    return dic[morseBase[index]]("A", morseBase, index+1)


def q5(charToTrade, morseBase, index):
    dic = {".": q11, "-": q12, "|": trade}
    return dic[morseBase[index]]("N", morseBase, index+1)


def q6(charToTrade, morseBase, index):
    dic = {".": q13, "-": q14, "|": trade}
    return dic[morseBase[index]]("M", morseBase, index+1)


def q7(charToTrade, morseBase, index):
    dic = {".": q15, "-": q16, "|": trade}
    return dic[morseBase[index]]("S", morseBase, index+1)


def q8(charToTrade, morseBase, index):
    dic = {".": q17, "-": q32, "|": trade}
    return dic[morseBase[index]]("U", morseBase, index+1)


def q9(charToTrade, morseBase, index):
    dic = {".": q18, "|": trade}
    return dic[morseBase[index]]("R", morseBase, index+1)


def q10(charToTrade, morseBase, index):
    dic = {".": q19, "-": q20, "|": trade}
    return dic[morseBase[index]]("W", morseBase, index+1)


def q11(charToTrade, morseBase, index):
    dic = {".": q21, "-": q22, "|": trade}
    return dic[morseBase[index]]("D", morseBase, index+1)


def q12(charToTrade, morseBase, index):
    dic = {".": q23, "-": q24, "|": trade}
    return dic[morseBase[index]]("K", morseBase, index+1)


def q13(charToTrade, morseBase, index):
    dic = {".": q25, "-": q26, "|": trade}
    return dic[morseBase[index]]("G", morseBase, index+1)


def q14(charToTrade, morseBase, index):
    dic = {".": q27, "-": q28, "|": trade}
    return dic[morseBase[index]]("O", morseBase, index+1)


def q15(charToTrade, morseBase, index):
    dic = {".": q29, "-": q30, "|": trade}
    return dic[morseBase[index]]("H", morseBase, index+1)


def q16(charToTrade, morseBase, index):
    dic = {"-": q31, "|": trade}
    return dic[morseBase[index]]("V", morseBase, index+1)


def q17(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("F", morseBase, index+1)


def q18(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("L", morseBase, index+1)


def q19(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("P", morseBase, index+1)


def q20(charToTrade, morseBase, index):
    dic = {"-": q34, "|": trade}
    return dic[morseBase[index]]("J", morseBase, index+1)


def q21(charToTrade, morseBase, index):
    dic = {".": q35, "|": trade}
    return dic[morseBase[index]]("B", morseBase, index+1)


def q22(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("X", morseBase, index+1)


def q23(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("C", morseBase, index+1)


def q24(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("Y", morseBase, index+1)


def q25(charToTrade, morseBase, index):
    dic = {".": q36, "|": trade}
    return dic[morseBase[index]]("Z", morseBase, index+1)


def q26(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("Q", morseBase, index+1)


def q27(charToTrade, morseBase, index):
    dic = {".": q37}
    return dic[morseBase[index]]("", morseBase, index+1)


def q28(charToTrade, morseBase, index):
    dic = {".": q38, "-": q39}
    return dic[morseBase[index]]("", morseBase, index+1)


def q29(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("5", morseBase, index+1)


def q30(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("4", morseBase, index+1)


def q31(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("3", morseBase, index+1)


def q32(charToTrade, morseBase, index):
    dic = {"-": q33}
    return dic[morseBase[index]]("", morseBase, index+1)


def q33(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("2", morseBase, index+1)


def q34(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("1", morseBase, index+1)


def q35(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("6", morseBase, index+1)


def q36(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("7", morseBase, index+1)


def q37(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("8", morseBase, index+1)


def q38(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("9", morseBase, index+1)


def q39(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]]("0", morseBase, index+1)


def q40(charToTrade, morseBase, index):
    dic = {"|": trade}
    return dic[morseBase[index]](" ", morseBase, index+1)


def q41(charToTrade, morseBase, index):
    """
    text = [x for x in morseBase if x not in ".-/#"]
    return "".join(text)
    """
    return "".join(filter({'.', '-', '/', '#'}.isdisjoint, morseBase))

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo + '#'


nome_arquivo = "fita01.txt"
morseBase = list(ler_arquivo(nome_arquivo))
sys.setrecursionlimit(2*len(morseBase))
print(f'Codigo traduzido de {nome_arquivo} - {q0("", morseBase, 0)}\n')

nome_arquivo = "fita02.txt"
morseBase = list(ler_arquivo(nome_arquivo))
sys.setrecursionlimit(2*len(morseBase))
print(f'Codigo traduzido de {nome_arquivo} - {q0("", morseBase, 0)}\n')

nome_arquivo = "fita03.txt"
morseBase = list(ler_arquivo(nome_arquivo))
sys.setrecursionlimit(2*len(morseBase))
print(f'Codigo traduzido de {nome_arquivo} - {q0("", morseBase, 0)}\n')

nome_arquivo = "fitaNumeros.txt"
morseBase = list(ler_arquivo(nome_arquivo))
sys.setrecursionlimit(2*len(morseBase))
print(f'Codigo traduzido de {nome_arquivo} - {q0("", morseBase, 0)}')