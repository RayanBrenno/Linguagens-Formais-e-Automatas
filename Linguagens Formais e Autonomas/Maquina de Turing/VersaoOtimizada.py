import sys

def start(morseBase):
    sys.setrecursionlimit(2*len(morseBase))
    dicFunctions = {
        ".": read,
        "-": read,
        "/": read,
        "|": trade,
        "$": end
    }
    morseToTrade = ""
    textTranslated = ""
    index = 0
    morseToText = {
        '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D',  '.': 'E',   '..-.': 'F',
        '--.': 'G',  '....': 'H', '..': 'I',   '.---': 'J', '-.-': 'K',  '.-..': 'L',
        '--': 'M',   '-.': 'N',   '---': 'O',  '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S',  '-': 'T',    '..-': 'U',  '...-': 'V', '.--': 'W',  '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
        '/': ' ', '.-.-.-': '.'
    }
    return dicFunctions[morseBase[index]](morseBase, morseToTrade, textTranslated, index, dicFunctions, morseToText)
    
    
def read(morseBase, morseToTrade, textTranslated, index, dicFunctions, morseToText):
    morseToTrade += morseBase[index]
    return dicFunctions[morseBase[index]](morseBase, morseToTrade, textTranslated, index + 1, dicFunctions, morseToText)


def trade(morseBase, morseToTrade, textTranslated, index, dicFunctions, morseToText):
    textTranslated += morseToText[morseToTrade[0:-1]]
    morseToTrade = ""
    return dicFunctions[morseBase[index]](morseBase, morseToTrade, textTranslated, index, dicFunctions, morseToText)


def end(morseBase, morseToTrade, textTranslated, index, dicFunctions, morseToText):
    return textTranslated


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo + '$'

morseBase = "-|.|...|-|.-|-.|-..|---|/|---|/|-.-.|---|-..|..|--.|---|$"
print(f'Translated code - {start(morseBase)}\n')

nome_arquivo = "fita01.txt"
morseBase = ler_arquivo(nome_arquivo)
print(f'Translated code - {start(morseBase)}\n')


nome_arquivo = "fita02.txt"
morseBase = ler_arquivo(nome_arquivo)
print(f'Translated code - {start(morseBase)}\n')

nome_arquivo = "fita03.txt"
morseBase = ler_arquivo(nome_arquivo)
print(f'Translated code - {start(morseBase)}\n')
