# 🎯 Jogo da Forca (Hangman)

Um jogo da forca (hangman) desenvolvido em Python, com palavras em português organizadas pelos temas distritos de Moçambique, frutas e animais.

## 📋 Descrição

Este é um jogo clássico da forca onde o jogador tenta adivinhar uma palavra secreta, letra por letra, antes que o boneco seja completamente enforcado. O projeto foi desenvolvido como parte dos meus estudos de Python ( utilizando o curso 100 Days of Code - App Brewery).

## ✨ Funcionalidades

- Escolha aleatória de palavras a partir de diferentes categorias temáticas;
- Arte ASCII do boneco da forca, atualizada a cada erro;
- Feedback visual do progresso da palavra (letras acertadas e espaços em branco);
- Contagem de tentativas restantes;
- Mensagens de vitória e derrota.

## 🛠️ Tecnologias utilizadas

- Python 3.13.12
- Git version 2.53.0.windows.1
- Github

## 📁 Estrutura do projeto

```
hangman/
├── main.py            # Arquivo principal com a lógica do jogo
├── hangmanArt.py       # Arte ASCII de cada estágio da forca
├── hangmanWords.py     # Listas de palavras por categoria
└── documentation/
|    └── README.md
|    └── Fluxograma Hangman.drawio
|    └── Fluxograma Hangman.jpg
|    └── LICENSE

```

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Jaimepelembe/hangman.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd hangman
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 🎮 Como jogar

1. Ao iniciar, uma palavra secreta é escolhida aleatoriamente.
2. Digite uma letra por vez tentando adivinhar a palavra.
3. Cada letra errada aproxima o boneco de ser enforcado.
4. O jogo termina quando você acerta a palavra completa (vitória) ou erra tentativas suficientes para completar a forca (derrota).


## 👤 Autor

Desenvolvido por **Jaime Fernando**
- GitHub: [@jaimepelembe](https://github.com/jaimepelembe)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.