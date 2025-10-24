from navegador import iniciar_navegador, fechar_navegador
from inicio import iniciar_jogo
from letras import capturar_letras_dia
from gerador_palavras import carregar_dicionario, gerar_palavras_possiveis
from config import URL
 
 
def main():
 
    driver = iniciar_navegador(URL)
 
    iniciar_jogo(driver)

    letras = capturar_letras_dia(driver)

    dicionario = carregar_dicionario("palavras.txt")

    palavras = gerar_palavras_possiveis(letras, dicionario)

    print(palavras)
 
    input("Pressione Enter para fechar o navegador...")
    fechar_navegador(driver)
 
if __name__ == "__main__":
    main()
