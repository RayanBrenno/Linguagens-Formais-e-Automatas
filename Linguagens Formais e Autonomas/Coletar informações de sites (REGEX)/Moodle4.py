import re
import requests
import pandas as pd


def gerarArquivo(dataFrame, nomeArquivo):
    try:
        with open(nomeArquivo, "w", encoding="utf-8", newline='') as arquivo:
            dataFrame.to_csv(arquivo, index=False)
            print(f"Arquivo {nomeArquivo} salvo com sucesso.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")


def obterDadosEmIntervalo(padraoRegex, conteudo):
    dados = re.findall(padraoRegex, conteudo)
    for x in range(len(dados)):
        primeira_divisao = dados[x].split('>')
        segunda_divisao = primeira_divisao[1].split('<')
        dados[x] = segunda_divisao[0]
    return dados


def casoA():
    url = "https://noticias.uol.com.br/blogs-e-colunas/"
    response = requests.get(url)
    conteudo = response.text

    def casoA1():
        padraoTitulo = r'<span class="thumb-kicker kicker-small kicker-lg-large">.*?<\/span>'
        titulo = obterDadosEmIntervalo(padraoTitulo, conteudo)

        padraoTexto = r'<h3 class="thumb-title title-xsmall.*?<\/h3>'
        textos = obterDadosEmIntervalo(padraoTexto, conteudo)

        padraoAutor = r'<p class="author">.*?<\/p>'
        autores = obterDadosEmIntervalo(padraoAutor, conteudo)

        dataCasoA1 = pd.DataFrame({
            'Título': titulo,
            'Texto': textos,
            'Autor': autores
        })

        gerarArquivo(dataCasoA1, "Caso A-1.csv")

    def casoA2():
        padraoNome = r'<h4 class="h-components">.*?</h4>'
        nomes = obterDadosEmIntervalo(padraoNome, conteudo)

        padraoImagem = r'<div class="image mask-circle"><div class="placeholder"><img src=".*?".*?>'
        imagens = re.findall(padraoImagem, conteudo)

        for i in range(len(imagens)):
            primeira_divisao = imagens[i].split('data-src="')
            segunda_divisao = primeira_divisao[1].split('"')
            imagens[i] = segunda_divisao[0]

        dataCasoA2 = pd.DataFrame({
            'Nomes': nomes,
            'Imagem': imagens 
        })

        gerarArquivo(dataCasoA2, "Caso A-2.csv")

    casoA1()
    casoA2()


def casoB():
    url = "https://www.in.gov.br/web/dou/-/edital-n-10/2024-589442586"
    response = requests.get(url)
    conteudo = response.text

    def casoB1():
        padrao = r'<td.*?>(.*?)<\/td>'
        dadosTabela = obterDadosEmIntervalo(padrao, conteudo)

        matricula = []
        nome = []
        orgao = []
        tipo = []

        for i in range(4, len(dadosTabela), 4):
            if dadosTabela[i+3] == 'Beneficiário' or dadosTabela[i+3] == 'Aposentado':
                matricula.append(dadosTabela[i])
                nome.append(dadosTabela[i + 1])
                orgao.append(dadosTabela[i + 2])
                tipo.append(dadosTabela[i + 3])
            else:
                break

        dataCasoB1 = pd.DataFrame({
            "Matrícula": matricula,
            "Nome": nome,
            "Orgão": orgao,
            "Tipo": tipo
        })

        gerarArquivo(dataCasoB1, "Caso B-1.csv")

    def casoB2():
        padrao = r'<td.*?>(?=.*?\b(Gestor|Gestora)\b)(.*?)<\/td>'
        dadosParte2 = re.findall(padrao, conteudo)

        gestor = []
        telefone = []
        cep = []
        cidade = []
        uf = []

        for i in range(len(dadosParte2)):
            html_content = dadosParte2[i][1]
            padraoGestor = r'Gestor[ a-zA-Z]* da CAPE: ([^<]+)'
            padraoTelefone = r'Tel[:.]?\s*\(?\d{2}\)?\s*\d{4,5}-\d{4}'
            padraoCEP = r'CEP: (\d{5}-\d{3}) ([^/]+)/(..)'

            auxGestor = re.search(padraoGestor, html_content).group(1)
            auxTelefone = re.search(padraoTelefone, html_content).group()

            cep_match = re.search(padraoCEP, html_content)
            auxCep = cep_match.group(1).strip() if cep_match else None
            auxCidade = cep_match.group(2).strip() if cep_match else None
            auxUf = cep_match.group(3).strip() if cep_match else None

            if 'Tel' in auxGestor:
                auxGestor = auxGestor.split('-')[0].strip()

            gestor.append(auxGestor)
            telefone.append(auxTelefone)
            cep.append(auxCep)
            cidade.append(auxCidade)
            uf.append(auxUf)

        dataCasoB2 = pd.DataFrame({
            "Gestor/Gestora": gestor,
            "Telefone": telefone,
            "CEP": cep,
            "Cidade": cidade,
            "UF": uf
        })

        gerarArquivo(dataCasoB2, "Caso B-2.csv")

    casoB1()
    casoB2()


if __name__ == "__main__":
    casoA()
    casoB()
