from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from config import CAMINHO_WEBDRIVER

def iniciar_navegador(url):
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(CAMINHO_WEBDRIVER)
    driver = webdriver.Edge(service=service, options=options)  
    driver.get(url)

    return driver

def fechar_navegador(driver):
    driver.quit()
