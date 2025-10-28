from navegador import iniciar_navegador, fechar_navegador
from inicio import iniciar_jogo
from letras import capturar_letras_dia, capturar_letra_central
from gerador_palavras import carregar_dicionario, gerar_palavras_possiveis
from jogar import digitar_palavras  # já importa tudo o que precisa internamente
from config import URL


def main():
    driver = iniciar_navegador(URL)
    iniciar_jogo(driver)

    # captura letras do dia
    letras = capturar_letras_dia(driver)
    letra_central = capturar_letra_central(driver)

    # carrega dicionário local
    dicionario = carregar_dicionario("palavras.txt")

    # gera lista inicial de palavras possíveis
    palavras = gerar_palavras_possiveis(driver, dicionario, letras, letra_central)

    print(f"\n[INFO] Letras do dia: {' '.join(letras)}")
    print(f"[INFO] Letra central: {letra_central}")
    print(f"[INFO] Total de palavras iniciais: {len(palavras)}")

    # agora passa também letras e letra_central para o robô
    digitar_palavras(driver, palavras)

    input("Pressione Enter para fechar o navegador...")
    fechar_navegador(driver)


if __name__ == "__main__":
    main()
