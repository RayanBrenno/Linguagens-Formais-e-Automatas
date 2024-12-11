import itertools
import json


def nfaToDFA(arquivo):
    with open(f'ExercicioLaboratorio2/{arquivo}', 'r') as read:

        # Cria conjunto das partes de acordo com as keys em formato de array
        def criarConjuntoDasPartes(arr):
            final = []
            for i in range(len(arr) + 1):
                for aux in itertools.combinations(arr, i):
                    final.append(list(aux))

            return final

        # Remove as linhas que nao estao sendo usados, começa do maior pro menor, pra evitar problemas
        def removerNaoUsados(naoUsado, conjuntoDasPartes, valoresConjunto):
            for x in sorted(naoUsado, reverse=True):
                conjuntoDasPartes.pop(x)
                valoresConjunto.pop(x * 2)
                valoresConjunto.pop(x * 2)

            return conjuntoDasPartes, valoresConjunto

        # Uni os subconjuntos para 0 e 1
        def unirOsSubconjuntos(subconjunto):
            valores_0 = set()
            valores_1 = set()

            for estado in subconjunto:
                valor = transition[estado]
                valores_0.update(valor["0"])
                valores_1.update(valor["1"])

            if "\u03B5" in valores_1 and len(valores_1) != 1:
                valores_1.remove("\u03B5")
            if "\u03B5" in valores_0 and len(valores_0) != 1:
                valores_0.remove("\u03B5")

            return sorted(list(valores_0)), sorted(list(valores_1))

        # Preenche os valoresConjunto com as unioes de acordo com os subconjunto
        def gerarValoresConjunto(conjuntoDasPartes):
            valoresConjunto = []

            for x in conjuntoDasPartes:
                if len(x) == 0:
                    valoresConjunto.append(["\u03B5"])
                    valoresConjunto.append(["\u03B5"])

                if len(x) == 1:
                    estado = x[0]
                    valor = transition[estado]
                    valoresConjunto.append(valor['0'])
                    valoresConjunto.append(valor['1'])

                elif len(x) > 1:
                    valores_0, valores_1 = unirOsSubconjuntos(x)
                    valoresConjunto.append(valores_0)
                    valoresConjunto.append(valores_1)

            return valoresConjunto

        # Gera o dicionario para todas as combinações possiveis
        def gerarDicionario(conjuntoDasPartes):
            alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            dicionario = {}
            for x, y in zip(conjuntoDasPartes, alfabeto):
                dicionario[str(x)] = y

            return dicionario

        dados = json.load(read)
        transition = dados['transition']
        conjuntoDasPartes = criarConjuntoDasPartes(transition.keys())
        valoresConjunto = gerarValoresConjunto(conjuntoDasPartes)
        conjuntoDasPartes[0] = ["\u03B5"]
        dicionario = gerarDicionario(conjuntoDasPartes)

        # Loop que remove oq nao ta sendo usado
        while True:
            naoUsado = []
            mudou = False
            for x in conjuntoDasPartes:
                valor = conjuntoDasPartes.index(x)
                idicesIgnorados = [valor*2, (valor*2)+1]
                if x not in [valoresConjunto[i] for i in range(len(valoresConjunto)) if i not in idicesIgnorados]:
                    naoUsado.append(valor)
                    mudou = True
            if mudou:
                conjuntoDasPartes, valoresConjunto = removerNaoUsados(
                    naoUsado, conjuntoDasPartes, valoresConjunto)
            else:
                break

        for x in range(len(valoresConjunto)):
            valoresConjunto[x] = list(dicionario.get(str(valoresConjunto[x])))

        dicionarioFinal = {}
        contador = 0
        state = []
        inicial_state=[]
        end_state=[]
        for x in conjuntoDasPartes:

            aux1 = False
            for y in dados['end_state']:
                if y in x:
                    aux1 = True
                    
            aux2 = str(dicionario.get(str(x)))
            
            if x == [dados['initial_state']]:
                dicionarioFinal['->' + aux2] = {
                    "0": valoresConjunto[contador], "1": valoresConjunto[contador + 1]}
                inicial_state.append(aux2)

            elif aux1:
                dicionarioFinal['*' + aux2] = {
                    "0": valoresConjunto[contador], "1": valoresConjunto[contador + 1]}
                end_state.append(aux2)

            else:
                dicionarioFinal[aux2] = {
                    "0": valoresConjunto[contador], "1": valoresConjunto[contador + 1]}
                
            state.append(aux2)
            contador += 2


        for chave, valor in dicionarioFinal.items():
            print(f'{chave} : {valor}')
            
        dados = {
            "alpha": dados["alpha"],
            "state": state,
            "initial_state": inicial_state[0],
            "end_state": end_state,
            "transition": dicionarioFinal
        }

        with open(f'ExercicioLaboratorio2/Resposta-{arquivo}', 'w') as json_file:
            json.dump(dados, json_file, indent=4)


nfaToDFA('input.json')
print("------------------------------")
nfaToDFA('input2.json')