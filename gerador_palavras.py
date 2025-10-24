from itertools import permutations

def carregar_dicionario(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        return set(p.strip().lower() for p in file.readlines())
    

def gerar_palavras_possiveis(letras, dicionario, tam_minimo=4, tam_maximo=11):
    letras = [l.lower() for l in letras]
    palavras_validas = set()

    for tam in range(tam_minimo, min(len(letras), tam_maximo)+ 1):
        for p in permutations(letras, tam):
            palavra = ''.join(p)
            if palavra in dicionario:
                palavras_validas.add(palavra)

    return sorted(palavras_validas)
