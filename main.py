from navegador import iniciar_navegador, fechar_navegador
from inicio import iniciar_jogo
from config import URL


def main():

    driver = iniciar_navegador(URL)

    iniciar_jogo(driver)

    #start_button = driver.find_element(By.CSS_SELECTOR, '.button.button--game-white.intro-button.svelte-1t84pcu')

    #start_button.click()

    input("Pressione Enter para fechar o navegador...")
    fechar_navegador(driver)

if __name__ == "__main__":
    main()


