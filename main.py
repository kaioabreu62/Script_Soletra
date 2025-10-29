from navegador import iniciar_navegador, fechar_navegador
from inicio import iniciar_jogo
from letras import capturar_letras_dia, capturar_letra_central
from gerador_palavras import carregar_dicionario, gerar_palavras_possiveis
from jogar import digitar_palavras
from config import URL

def main():
    """
    Módulo responsável por chamar todas as funções do robô.
    """

    # abrir o jogo no navegador
    driver = iniciar_navegador(URL)

    # inicia a jogatina
    iniciar_jogo(driver)

    # captura letras do dia
    letras = capturar_letras_dia(driver)

    # captura letra central do dia
    letra_central = capturar_letra_central(driver)

    # carrega dicionário local
    dicionario = carregar_dicionario("palavras.txt")

    # gera lista de palavras possíveis
    palavras = gerar_palavras_possiveis(driver, dicionario, letras, letra_central)

    # printa informações pertinentes do jogo
    print(f"\n[INFO] Letras do dia: {' '.join(letras)}")
    print(f"[INFO] Letra central: {letra_central}")
    print(f"[INFO] Total de palavras possíveis do dia: {len(palavras)}")

    # digita palavras da lista de palavras possíveis
    digitar_palavras(driver, palavras)

    # fecha o navegador, jogo e o programa
    input("Pressione Enter para fechar o navegador...")
    fechar_navegador(driver)

# verifica se o arquivo está sendo executado diretamente (e não importado), execute a função main()
if __name__ == "__main__":
    main()
