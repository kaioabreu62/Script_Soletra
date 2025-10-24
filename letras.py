from selenium.webdriver.common.by import By


def capturar_letras_dia(driver):
    try:
        elementos_letras =  driver.find_elements(By.CSS_SELECTOR, ".cell-letter.svelte-1vt3j7k")
        letras = [el.text.strip().upper() for el in elementos_letras if el.text.strip()]
        print(f"[INFO] Letras do dia: {' '.join(letras)}")
        return letras
    except Exception as e:
        print(f"[Erro] Não foi possível capturar as letras do dia:", e)