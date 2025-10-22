from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TEMPO_ESPERA

def iniciar_jogo(driver):
    """
    Aguarda o botão 'Iniciar' aparecer e clica nele.
    """
    try:
        # Ajuste o seletor para o botão de início do seu jogo
        botao_iniciar = WebDriverWait(driver, TEMPO_ESPERA).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.button--game-white.intro-button.svelte-1t84pcu'))  # <- ajuste aqui
        )
        botao_iniciar.click()
        print("[INFO] Jogo iniciado com sucesso.")
    except Exception as e:
        print("[ERRO] Não foi possível clicar no botão de iniciar:", e)