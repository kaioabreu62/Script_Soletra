# 🔹 Arquivos de origem do seu dicionário
arquivos = [
    "pt_BR.dic.txt",
    "words.txt"
]

palavras = set()

# 🔹 Lê e junta todas as palavras dos arquivos (sem mudar nada)
for nome in arquivos:
    try:
        with open(nome, "r", encoding="utf-8") as f:
            for linha in f:
                palavra = linha.strip()
                if palavra:
                    palavras.add(palavra)
    except FileNotFoundError:
        print(f"[AVISO] Arquivo não encontrado: {nome}")

# 🔹 Ordena as palavras únicas alfabeticamente
palavras_unicas = sorted(palavras)

# 🔹 Salva no arquivo final
with open("palavras.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(palavras_unicas))

print(f"[OK] Gerado 'palavras.txt' com {len(palavras_unicas):,} palavras únicas (sem remover acentos, hífens ou nada mais).")
