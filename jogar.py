import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def digitar_palavras(driver, palavras):
    """
    - Tenta cada palavra da lista 'palavras' (já filtradas).
    - Digita a palavra usando o campo 'input' e (envia com o ENTER).
    - Se for rejeitada, seleciona todas as letras e apaga (com o BACKSPACE) o texto.
    
    """

    inicio = time.perf_counter()  # Início da contagem de execução do robô ao digitar

    # conjunto Set() de palavras aceitas pelo jogo
    palavras_aceitas = set()

    # conjunto Set() de palavras tentadas pelo robô a fim de evitar repetições de palavras
    palavras_tentadas = set()

     # 🔹 Localiza o campo de entrada do jogo (importante para performance)
    try:
        campo_input = driver.find_element(By.ID, "input")
    except Exception:
        print("[ERRO] Campo de entrada não encontrado.")
        return []

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
        palavras_tentadas.add(palavra)

        try:
            # digita palavra e envia ENTER
            campo_input.send_keys(palavra + Keys.ENTER)
            print(f"[TENTANDO] {palavra}")
            time.sleep(0.15)

            # apaga todas as letras digitadas de uma só vez 
            campo_input.send_keys(Keys.CONTROL + 'a') # Seleciona tudo
            campo_input.send_keys(Keys.BACKSPACE) # Apaga tudo
        except:
            print("Não foi possível encontrar o campo 'input'. Fechando o jogo...")
            break    

    fim = time.perf_counter()  # Fim da contagem de execução do robô ao digitar

    # tempo total da execução em segundos
    tempo_total = fim - inicio

    # tempo total da execução em minutos
    tempo_minutos = tempo_total / 60

    print(f"[TEMPO TOTAL] {tempo_total:.2f} segundos ({tempo_minutos:.2f} minutos)")
    return list(palavras_aceitas)
