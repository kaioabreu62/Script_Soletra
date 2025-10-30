from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
Módulo para entrar no jogo pelo navegador e para fechá-lo.
"""

def iniciar_navegador(url):
    # Configurações opcionais (como abrir maximizado)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    # Inicializa o Chrome com o driver gerenciado automaticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

def fechar_navegador(driver):
    driver.quit()
