def normalizar(texto):
    """Mantém acentos e cedilha, apenas converte para minúsculo e remove espaços extras."""
    return texto.strip().lower()

def carregar_dicionario(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        # Mantém todas as letras, incluindo acentos e ç
        return set(p.strip() for p in file if len(p.strip()) >= 4)

def gerar_palavras_possiveis(dicionario, letras, letra_central):
    letras_set = set(normalizar(l) for l in letras)
    letra_central = normalizar(letra_central)
    palavras_validas = []

    for palavra in dicionario:
        palavra_min = normalizar(palavra)
        if (
            4 <= len(palavra_min) <= 11
            and letra_central in palavra_min
            and all(l in letras_set for l in palavra_min)
        ):
            palavras_validas.append(palavra)

    return sorted(palavras_validas, key=len)
