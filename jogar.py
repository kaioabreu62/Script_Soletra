import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def digitar_palavras(driver, palavras):
    """
    - Tenta cada palavra da lista `palavras` (já filtradas).
    - Digita a palavra usando ActionChains e (envia com o ENTER).
    - Se for rejeitada, apaga (com o BACKSPACE) o texto.
    - Evita repetir palavras já tentadas.
    - Interrompe a digitação quando atingir o total do placar (se encontrado).
    """

    inicio = time.perf_counter()  # Início da contagem de execução do robô ao digitar

    # conjunto Set() de palavras aceitas pelo jogo
    palavras_aceitas = set()

    # conjunto Set() de palavras tentadas pelo robô a fim de evitar repetições de palavras
    palavras_tentadas = set()

    # tenta obter o total de palavras do placar (formato "X/Y", sendo "X" quantidade de palavras encontradas e o "Y" de palavras no total)
    try:
        # robô tenta achar o placar do jogo se caso não encontrar assume o tamanho da lista de palavras como limite máximo
        placar_elem = driver.find_element(By.CSS_SELECTOR, "span.points")
        total_palavras = int(placar_elem.text.strip().split("/")[1])
        print(f"[INFO] Total de palavras do dia: {total_palavras}")
    except Exception:
        placar_elem = None
        total_palavras = len(palavras)
        print("[AVISO] Não foi possível localizar o placar no site. Usando tamanho da lista como limite.")

    # copia da lista de palavras válidas possíveis para iterar (mantém original fora intacta)
    fila = [p.lower().strip() for p in palavras if p and p.strip()]

    # percorre cada palavra da lista 'fila' e tenta digitar
    for palavra in fila:
        if palavra in palavras_tentadas:
            continue
        palavras_tentadas.add(palavra)

        # lê placar atual antes de tentar
        total_antes = 0
        if placar_elem:
            try:
                total_antes = int(driver.find_element(By.CSS_SELECTOR, "span.points").text.strip().split("/")[0])
            except Exception:
                total_antes = 0

        # digita palavra e envia ENTER
        actions = ActionChains(driver)
        actions.send_keys(palavra + Keys.ENTER).perform()
        actions.reset_actions()

        print(f"[TENTANDO] {palavra}")
        time.sleep(0.5) 

        # verifica se foi aceita comparando o placar (se disponível)
        aceita = False
        if placar_elem:
            for _ in range(8):  # tenta ler o placar por ciclos de 8 tentativas a cada 0,05s
                try:
                    # se o número de palavras encontradas aumentou, ele sabe que a palavra foi aceita
                    total_depois = int(driver.find_element(By.CSS_SELECTOR, "span.points").text.strip().split("/")[0])
                    if total_depois > total_antes:
                        aceita = True
                        break
                except Exception:
                    pass
                time.sleep(0.05)

        if aceita:
            palavras_aceitas.add(palavra)
            print(f"[ACEITA] {palavra} (aceitas: {len(palavras_aceitas)})")
        else:
            # apaga a palavra rejeitada (envia backspaces várias vezes uma para cada letra)
            actions = ActionChains(driver)
            for _ in range(len(palavra)):
                actions.send_keys(Keys.BACKSPACE)
            actions.perform()
            actions.reset_actions()
            print(f"[REJEITADA] {palavra} — apagada")
            time.sleep(0.05)

        # condição de parada: se atingiu total do placar para de digitar
        if placar_elem and len(palavras_aceitas) >= total_palavras:
            print(f"\nTodas as palavras ({len(palavras_aceitas)}) foram encontradas! Encerrando.")
            break

    fim = time.perf_counter()  # Fim da contagem de execução do robô ao digitar

    # tempo total da execução em segundos
    tempo_total = fim - inicio

    # tempo total da execução em minutos
    tempo_minutos = tempo_total / 60

    print(f"\n[RESUMO] {len(palavras_aceitas)} aceitas de {len(palavras_tentadas)} tentadas.")
    print(f"[TEMPO TOTAL] {tempo_total:.2f} segundos ({tempo_minutos:.2f} minutos)")
    return list(palavras_aceitas)
