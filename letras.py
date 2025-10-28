from selenium.webdriver.common.by import By

def capturar_letras_dia(driver):
    try:
        elementos_letras = driver.find_elements(By.CSS_SELECTOR, "text.cell-letter")
        letras = [el.text.strip().lower() for el in elementos_letras if el.text.strip()]
        return letras
    except Exception as e:
        print(f"[Erro] Não foi possível capturar as letras do dia:", e)


def capturar_letra_central(driver):
    try:
        elemento_central = driver.find_element(By.CSS_SELECTOR, "svg.hexagon-cell.center text.cell-letter")
        return elemento_central.text.strip().lower()
    except Exception as e:
        print(f"[ERRO] Não foi possível capturar a letra central:", e)
        return None