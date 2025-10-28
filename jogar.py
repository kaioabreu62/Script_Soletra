import time
from collections import Counter
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def analisar_padrao(palavras_aceitas):
    """
    Analisa padrões simples das palavras aceitas.
    Retorna um dicionário com as letras e tamanhos mais comuns.
    """
    if not palavras_aceitas:
        return {}

    tamanhos = [len(p) for p in palavras_aceitas]
    letras = Counter("".join(palavras_aceitas))
    prefixos = Counter(p[:2] for p in palavras_aceitas if len(p) >= 2)
    sufixos = Counter(p[-2:] for p in palavras_aceitas if len(p) >= 2)

    return {
        "tam_medio": sum(tamanhos) / len(tamanhos),
        "letras_comuns": [l for l, _ in letras.most_common(5)],
        "prefixos": [p for p, _ in prefixos.most_common(3)],
        "sufixos": [s for s, _ in sufixos.most_common(3)]
    }

def priorizar_palavras(palavras_restantes, padrao):
    """
    Ordena palavras restantes de acordo com o quanto se parecem com o padrão.
    """
    def pontuar(p):
        score = 0
        if abs(len(p) - padrao.get("tam_medio", len(p))) < 2:
            score += 2
        for l in padrao.get("letras_comuns", []):
            if l in p:
                score += 1
        for pref in padrao.get("prefixos", []):
            if p.startswith(pref):
                score += 2
        for suf in padrao.get("sufixos", []):
            if p.endswith(suf):
                score += 2
        return score

    return sorted(palavras_restantes, key=pontuar, reverse=True)

def digitar_palavras(driver, palavras):
    """
    Digita palavras no Soletra (G1) usando ActionChains.
    Aprende com as palavras aceitas e ajusta próximas tentativas.
    """
    palavras_aceitas = set()
    palavras_tentadas = set()

    try:
        placar_elem = driver.find_element(By.CSS_SELECTOR, "span.points")
        total_palavras = int(placar_elem.text.strip().split("/")[1])
        print(f"[INFO] Total de palavras do dia: {total_palavras}")
    except Exception:
        placar_elem = None
        total_palavras = len(palavras)
        print("[AVISO] Não foi possível localizar o placar no site.")

    while palavras:
        # Recalcula padrão e prioriza palavras
        if palavras_aceitas:
            padrao = analisar_padrao(list(palavras_aceitas))
            palavras = priorizar_palavras(palavras, padrao)
            print(f"[ADAPTANDO] Novo padrão: {padrao}")

        palavra = palavras.pop(0).lower().strip()
        if palavra in palavras_tentadas:
            continue
        palavras_tentadas.add(palavra)

        total_antes = 0
        if placar_elem:
            try:
                total_antes = int(driver.find_element(By.CSS_SELECTOR, "span.points").text.strip().split("/")[0])
            except Exception:
                total_antes = 0

        # Digita palavra
        actions = ActionChains(driver)
        actions.send_keys(palavra)
        actions.key_down(Keys.ENTER).key_up(Keys.ENTER)
        actions.perform()
        actions.reset_actions()

        print(f"[TENTANDO] {palavra}")
        time.sleep(0.6)

        aceita = False
        if placar_elem:
            for _ in range(6):
                try:
                    total_depois = int(driver.find_element(By.CSS_SELECTOR, "span.points").text.strip().split("/")[0])
                    if total_depois > total_antes:
                        aceita = True
                        break
                except Exception:
                    pass
                time.sleep(0.25)

        if aceita:
            print(f"[ACEITA ✅] {palavra}")
            palavras_aceitas.add(palavra)
        else:
            print(f"[REJEITADA ❌] {palavra} — apagando...")
            actions = ActionChains(driver)
            for _ in range(len(palavra)):
                actions.send_keys(Keys.BACKSPACE)
            actions.perform()
            actions.reset_actions()
            time.sleep(0.3)

        if placar_elem and len(palavras_aceitas) >= total_palavras:
            print(f"\n🎯 Todas as palavras ({len(palavras_aceitas)}) foram encontradas!")
            break

    print(f"\n[RESUMO] {len(palavras_aceitas)} aceitas de {len(palavras_tentadas)} tentadas.")
    return list(palavras_aceitas)
