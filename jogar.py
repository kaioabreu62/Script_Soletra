import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def digitar_palavras(driver, palavras):
    actions = ActionChains(driver)
    for palavra in palavras:
        for letra in palavra:
            actions.send_keys(letra)
            time.sleep(0.05)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        actions.reset_actions()
        print(f"[JOGOU] {palavra}")
        time.sleep(0.4)
