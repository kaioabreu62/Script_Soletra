# 🔤 Script Soletra

Automação em Python para o jogo **Soletra**, disponível no portal G1.

O projeto utiliza **Selenium WebDriver** para acessar o jogo, identificar automaticamente as letras disponíveis, localizar a letra central, gerar palavras válidas a partir de um dicionário local e inseri-las automaticamente no jogo.

> **Aviso:** Este é um projeto independente, desenvolvido para fins de estudo e aprendizado em Python, automação web e Selenium. Não possui afiliação oficial com o G1 ou com a Globo.

---

## 🎯 Objetivo

O objetivo do projeto é automatizar as principais etapas necessárias para jogar o Soletra:

1. Abrir o jogo no navegador;
2. Iniciar a partida;
3. Capturar as letras disponíveis;
4. Identificar a letra central;
5. Carregar um dicionário de palavras;
6. Filtrar as palavras de acordo com as regras do jogo;
7. Detectar automaticamente o tamanho máximo permitido no dia;
8. Enviar as palavras encontradas para o jogo;
9. Evitar o envio repetido de palavras;
10. Encerrar o navegador após a execução.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Selenium**
* **WebDriver Manager**
* **Google Chrome**
* **Git / GitHub**

---

## 📂 Estrutura do projeto

```text
Script_Soletra/
│
├── config.py
├── gerador_palavras.py
├── inicio.py
├── jogar.py
├── letras.py
├── main.py
├── navegador.py
├── palavras.txt
├── requisitos.txt
├── teste.py
└── README.md
```

### `main.py`

É o ponto de entrada da aplicação.

Responsável por coordenar todo o fluxo do projeto:

```text
Abrir navegador
      ↓
Iniciar jogo
      ↓
Capturar letras
      ↓
Identificar letra central
      ↓
Carregar dicionário
      ↓
Gerar palavras válidas
      ↓
Enviar palavras ao jogo
      ↓
Encerrar navegador
```

### `navegador.py`

Responsável pelo gerenciamento do navegador.

O módulo inicializa o Google Chrome utilizando Selenium e `webdriver-manager`, que realiza o gerenciamento do ChromeDriver automaticamente.

Também possui a função responsável por encerrar o navegador ao final da execução.

### `inicio.py`

Responsável por iniciar a partida.

O módulo localiza os botões necessários no jogo e realiza as ações para iniciar a partida e fechar a seção de ajuda, quando apresentada.

### `letras.py`

Responsável por capturar as informações do tabuleiro.

São obtidas:

* As letras disponíveis;
* A letra central obrigatória.

Essas informações são utilizadas posteriormente para gerar as palavras possíveis.

### `gerador_palavras.py`

Responsável pelo processamento do dicionário.

O módulo:

* Carrega o arquivo `palavras.txt`;
* Remove espaços desnecessários;
* Ignora palavras menores que 4 letras;
* Remove palavras duplicadas;
* Identifica o tamanho máximo permitido pelo jogo;
* Verifica a presença da letra central;
* Verifica se todas as letras da palavra estão entre as letras disponíveis;
* Trata acentos para fins de comparação;
* Ordena as palavras encontradas por tamanho.

### `jogar.py`

Responsável por inserir as palavras encontradas no jogo.

O módulo utiliza o campo de entrada do Soletra para:

* Digitar cada palavra;
* Pressionar `Enter`;
* Registrar palavras tentadas;
* Evitar repetições;
* Identificar palavras aceitas;
* Acompanhar a quantidade de palavras encontradas.

### `config.py`

Centraliza algumas configurações do projeto.

Atualmente contém:

```python
URL = 'https://g1.globo.com/jogos/soletra/'
TEMPO_ESPERA = 0.30
```

Isso facilita a alteração da URL e do tempo utilizado nas esperas do Selenium sem precisar modificar vários arquivos.

### `palavras.txt`

Arquivo utilizado como dicionário local pelo gerador de palavras.

O programa percorre esse arquivo e utiliza seu conteúdo como base para encontrar palavras que atendam às regras do jogo.

### `requisitos.txt`

Contém as dependências necessárias para executar o projeto:

```text
selenium
webdriver_manager
```

---

## ⚙️ Requisitos

Antes de executar o projeto, certifique-se de possuir:

* Python 3 instalado;
* Google Chrome instalado;
* Conexão com a internet;
* Um ambiente para execução de Python.

O projeto utiliza `webdriver-manager`, portanto o ChromeDriver é gerenciado automaticamente pelo programa.

---

## 📥 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/kaioabreu62/Script_Soletra.git
```

### 2. Entre na pasta do projeto

```bash
cd Script_Soletra
```

### 3. Instale as dependências

```bash
pip install -r requisitos.txt
```

---

## ▶️ Executando o projeto

Após instalar as dependências, execute:

```bash
python main.py
```

O programa irá abrir o Google Chrome e acessar automaticamente:

```text
https://g1.globo.com/jogos/soletra/
```

A partir daí, o fluxo de automação será iniciado.

---

## 🔎 Como o gerador de palavras funciona

O projeto utiliza o arquivo `palavras.txt` como fonte de palavras.

Depois de capturar as letras do jogo, o programa verifica cada palavra do dicionário.

Uma palavra é considerada candidata quando:

* Possui pelo menos 4 letras;
* Não ultrapassa o tamanho máximo permitido pelo jogo;
* Contém obrigatoriamente a letra central;
* Utiliza somente as letras disponíveis no desafio.

Por exemplo, considerando:

```text
Letras disponíveis: A B C D E I R
Letra central: A
```

Uma palavra como:

```text
cadeira
```

pode ser considerada válida caso todas as suas letras estejam disponíveis e ela contenha a letra central.

---

## 🧩 Fluxo de execução

```text
                    ┌──────────────────┐
                    │     main.py      │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   navegador.py      │
                  │ Abre o Google Chrome│
                  └──────────┬──────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │    inicio.py   │
                    │ Inicia o jogo  │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │    letras.py   │
                    │ Captura letras │
                    └───────┬────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ gerador_palavras.py │
                 │ Filtra o dicionário  │
                 └──────────┬───────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │    jogar.py    │
                    │ Digita palavras│
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ Finalização    │
                    │ do programa    │
                    └────────────────┘
```

---

## 📚 Conceitos utilizados

Este projeto foi desenvolvido utilizando conceitos importantes de programação e automação, incluindo:

* Manipulação de arquivos;
* Estruturas `set`, `list` e `string`;
* Funções e módulos Python;
* Expressões regulares;
* Tratamento de exceções;
* Manipulação de caracteres Unicode;
* Automação de navegador;
* Localização de elementos HTML;
* CSS Selectors;
* Selenium WebDriver;
* Gerenciamento automático do ChromeDriver;
* Separação de responsabilidades entre módulos.

---

## 🚧 Possíveis melhorias

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Melhorar o tratamento de exceções;
* [ ] Substituir `time.sleep()` por esperas explícitas sempre que possível;
* [ ] Criar testes automatizados;
* [ ] Melhorar a estrutura do dicionário;
* [ ] Criar um sistema de logs;
* [ ] Adicionar uma interface gráfica;
* [ ] Criar configurações externas para os seletores do Selenium;
* [ ] Melhorar a detecção de mudanças na estrutura HTML do jogo;
* [ ] Adicionar suporte para atualização automática do dicionário;
* [ ] Criar documentação técnica mais detalhada.

---

## ⚠️ Observações

Como o projeto utiliza Selenium para interagir com elementos específicos da página, alterações na estrutura HTML do jogo podem fazer com que alguns seletores deixem de funcionar.

O projeto também depende da disponibilidade do site e de uma conexão com a internet.

O arquivo `palavras.txt` influencia diretamente a quantidade e a qualidade das palavras encontradas.

---

## 🎓 Finalidade do projeto

Este projeto foi desenvolvido como uma forma prática de estudar e aplicar conceitos de:

**Python + Selenium + Automação Web + Manipulação de arquivos + Estruturação de projetos.**

Além da automação do jogo, o projeto serve como exercício prático de desenvolvimento e organização de código Python.

---

## 👨‍💻 Autor

**Kaio Abreu**

GitHub: [kaioabreu62](https://github.com/kaioabreu62)

---

## 📄 Licença

Este projeto não possui uma licença de software definida no momento.

Caso o projeto seja disponibilizado para reutilização por terceiros, recomenda-se adicionar uma licença, como a **MIT License**, conforme a intenção do autor.

```

Esse README está alinhado com o código que encontrei. Por exemplo, `main.py` realmente coordena o fluxo completo, `navegador.py` utiliza `webdriver-manager`, `letras.py` captura as letras, `gerador_palavras.py` aplica os filtros e `jogar.py` envia as palavras ao campo de entrada.

**Uma observação importante:** eu não colocaria no README que o projeto "encontra todas as palavras possíveis" sem ressalvas. Ele encontra as palavras possíveis **dentro do conteúdo de `palavras.txt`**. Isso é importante para documentar o comportamento real do programa.

Se você quiser, no próximo passo também posso fazer uma **análise técnica do seu projeto arquivo por arquivo**, apontando o que está bem feito, o que pode ser melhorado e como deixá-lo com uma estrutura mais profissional para colocar no seu **portfólio de Desenvolvedor Júnior**.
```
