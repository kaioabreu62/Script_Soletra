from selenium.webdriver.common.by import By
import re
import unicodedata
import time

def remover_acentos(txt):
    """Remove acentos só para comparação lógica (mantém 'ç')."""
    return ''.join(
        c for c in unicodedata.normalize("NFD", txt)
        if unicodedata.category(c) != "Mn" or c in "çÇ"
    ).lower()


def carregar_dicionario(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        # Mantém todas as letras, incluindo acentos e ç
        return set(p.strip() for p in file if len(p.strip()) >= 4)

def gerar_palavras_possiveis(driver, dicionario, letras, letra_central):
    """
    Gera as palavras válidas para o Soletra (G1).
    - Detecta automaticamente o tamanho máximo permitido lendo todos os elementos "X letras".
    - Mantém acentos e cedilha.
    - Exige a letra central e só usa letras disponíveis.
    """

    letras_set = set(remover_acentos(l) for l in letras)
    letra_central = remover_acentos(letra_central)
    palavras_validas = []

    # 🔹 Detecta o maior tamanho disponível (ex: 10 letras)
    try:
        spans = driver.find_elements(By.CSS_SELECTOR, "span.length")
        tamanhos = []
        for span in spans:
            texto = span.text.strip()
            match = re.search(r"(\d+)", texto)
            if match:
                tamanhos.append(int(match.group(1)))

        tamanho_maximo = max(tamanhos) if tamanhos else 11
        print(f"[INFO] Tamanho máximo detectado: {tamanho_maximo} letras")
    except Exception as e:
        tamanho_maximo = 11
        print(f"[AVISO] Não foi possível detectar o tamanho máximo ({e}). Usando 11 como padrão.")

    # 🔹 Gera palavras válidas
    for palavra in dicionario:
        palavra_possiveis = remover_acentos(palavra.strip().lower())

        if len(palavra_possiveis) >= 4 and len(palavra_possiveis) <= tamanho_maximo:
            if letra_central in palavra_possiveis:
                if all(l in letras_set for l in palavra_possiveis):
                    palavras_validas.append(palavra_possiveis)
    
    
    print(f"[INFO] {len(palavras_validas)} palavras válidas geradas.")
    return sorted(palavras_validas, key=len)