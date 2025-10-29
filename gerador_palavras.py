from selenium.webdriver.common.by import By
import re
import unicodedata

def remover_acentos(txt):
    """
    Separa e remove acentos das palavras para fazer a comparação correta dos caracteres entre o dicionário e o jogo. 
    Preserva somente o cedilha das palavras.
    Converte todas as palavras para minúsculas. 
    """
    return ''.join(
        c for c in unicodedata.normalize("NFD", txt)
        if unicodedata.category(c) != "Mn" or c in "çÇ"
    ).lower()


def carregar_dicionario(caminho):
    """
    Abre o arquivo 'palavras.txt' para leitura.
    Percorre o arquivo linha por linha.
    Remove espaços em branco e quebras de linha.
    Só aceita palavras de 4 letras ou mais, descartando o resto.
    Coloca todas as palavras aceitas dentro de um conjunto Set() que elimina duplicadas automaticamente. 
    """
    with open(caminho, "r", encoding="utf-8") as file:
        return set(p.strip() for p in file if len(p.strip()) >= 4)

def gerar_palavras_possiveis(driver, dicionario, letras, letra_central):
    """
    Gera todas as palavras válidas possíveis para o Soletra (G1) por meio da filtragem do dicionário seguindo as regras do jogo:
     - A palavra de conter entre 4 letras e o tamanho máximo do dia (detectado automaticamente);
     - Deve conter obrigatoriamente a letra central;
     - Só pode usar as letras que estão disponíveis no dia;
     - Mantém suporte total a acentos e cedilhas.

    Parâmetros:
     - driver -> instância ativa do Selenium WebDriver;
     - dicionario -> conjunto de palavras do arquivo local (palavras.txt);
     - letras -> lista das letras disponíveis no dia.

     Retorna:
     - Uma lista ordenada de palavras válidas possíveis (da menor quantidade até a maior). 
    
    """

    # Normaliza letras (sem acento apenas para comparação)
    letras_set = set(remover_acentos(l) for l in letras)
    letra_central = remover_acentos(letra_central)
    palavras_validas = []

    # Detecta o maior tamanho disponível de letras no dia (ex: 10 letras)
    try:
        spans = driver.find_elements(By.CSS_SELECTOR, "span.length")
        tamanhos = []
        for span in spans:
            texto = span.text.strip()
            match = re.search(r"(\d+)", texto)
            if match:
                tamanhos.append(int(match.group(1)))

        # Caso não encontre o tamanho máximo do dia, assume 11 como padrão (acredito ser a maior quantidade de letras que o jogo gere)
        tamanho_maximo = max(tamanhos) if tamanhos else 11
        print(f"[INFO] Tamanho máximo detectado: {tamanho_maximo} letras")
    except Exception as e:
        tamanho_maximo = 11
        print(f"[AVISO] Não foi possível detectar o tamanho máximo ({e}). Usando 11 como padrão.")

    # Filtra o dicionário e gera apenas as palavras válidas possíveis
    for palavra in dicionario:
        palavras_possiveis = remover_acentos(palavra.strip().lower())

        if len(palavras_possiveis) >= 4 and len(palavras_possiveis) <= tamanho_maximo: # Respeita o limite de tamanho das palavras
            if letra_central in palavras_possiveis:                                    # Verifica se contém a letra central
                if all(l in letras_set for l in palavras_possiveis):                   # Mantém palavras que contém as letras disponíveis
                    palavras_validas.append(palavras_possiveis)                        # Coloca essas palavras filtradas dentro de uma lista
    
    
    print(f"[INFO] {len(palavras_validas)} palavras válidas geradas.")
    return sorted(palavras_validas, key=len)