# Miau Miwar - A Batalha pelo Território

## Descrição

Bem-vindo à **Miau Miwar**, um jogo intergaláctico de dois jogadores onde dois gatos cósmicos lutam pelo domínio espacial. O Gato Vermelho e o Gato Azul se enfrentam em uma batalha épica utilizando bolas de fogo e movimentos ágeis. Cada jogador tem 7 vidas, e o objetivo é esgotar as vidas do oponente antes que suas próprias vidas se esgotem.

## História

Em um canto distante da galáxia, onde as estrelas brilham intensamente, dois gatos lendários — **Gato Vermelho** e **Gato Azul** — travam uma guerra pelo controle de seu território. Utilizando suas habilidades únicas e bolas de fogo energéticas, eles estão dispostos a lutar até o fim. O destino do universo dos gatos intergalácticos está nas mãos de vocês!

## Como Jogar

- **Inicie o Jogo**

  - Com as setas, selecione a opção "Jogar".
  - A opção selecionada será azul.

- **Jogador 1 (Gato Vermelho)**:

  - Movimenta-se utilizando as teclas **W, A, S, D**.
  - Atira bolas de fogo pressionando o **Ctrl esquerdo**.

- **Jogador 2 (Gato Azul)**:
  - Movimenta-se utilizando as **setas do teclado**.
  - Atira bolas de fogo pressionando o **Ctrl direito**.

## Regras do Jogo

- Cada jogador começa com **7 vidas**.
- Uma vida é perdida toda vez que um jogador é atingido por uma bola de fogo do oponente.
- O jogo termina quando a vida de um dos jogadores chega a **zero**.
- O último jogador sobrevivente é coroado como o vencedor da batalha intergaláctica!

## Requisitos para Jogar

- Python 3.x
- Biblioteca `Pygame`

## Como Executar

1. Certifique-se de que o Python e a biblioteca `Pygame` estão instalados no seu sistema.
2. Baixe o conteúdo desse repositório. Não esqueça de descompactar!
3. Execute o seguinte comando no terminal para iniciar o jogo:

```bash
python principal.py
```

## Para Pessoas Desenvolvedoras

Este jogo foi desenvolvido utilizando **Python** e a biblioteca **Pygame**. Abaixo está um resumo da estrutura e dos principais componentes do código:

### Principais Variáveis Globais

- **LARGURA, ALTURA**: Dimensões da janela do jogo (900x500 pixels).
- **VEL**: Velocidade de movimento dos gatos (5 pixels por frame).
- **FOGO_VEL**: Velocidade dos projéteis de fogo (7 pixels por frame).
- **MAX_FOGO**: Número máximo de bolas de fogo que cada jogador pode ter na tela simultaneamente (3 por jogador).
- **VIDA_FONTE** e **GANHADOR_FONTE**: Fontes para exibir as vidas e a mensagem do vencedor.

### Estrutura de Recursos

Os recursos gráficos e sonoros do jogo estão localizados na pasta `Recursos`.

### Funções Principais

- **`desenhar_janela()`**: Responsável por renderizar a tela a cada frame, incluindo a posição dos jogadores, bolas de fogo, e as vidas restantes.
- **`movimentar_vermelho()`** e **`movimentar_azul()`**: Controlam o movimento dos gatos com base nas teclas pressionadas.
- **`controlhe_fogo()`**: Atualiza a posição das bolas de fogo e verifica se houve colisão com o oponente. Também remove as bolas de fogo que saem da tela.
- **`ganhador_escrever()`**: Exibe o vencedor na tela e pausa o jogo por 3 segundos antes de reiniciar.

### Eventos Personalizados

- **`VERMELHO_ACERTADO`** e **`AZUL_ACERTADO`**: Eventos personalizados disparados quando um dos gatos é atingido por uma bola de fogo. Eles decrementam a vida do jogador atingido.

### Loops e Mecânicas do Jogo

O loop principal do jogo controla o seguinte:

1. Captura eventos de entrada, como teclas pressionadas para movimento e tiros.
2. Atualiza a posição dos personagens e projéteis.
3. Verifica colisões e trata a diminuição de vidas.
4. Atualiza a tela a cada frame para refletir o estado atual do jogo.

### Como Contribuir

1. Faça um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b feature/NomeDaFeature`).
3. Faça commit das suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Envie seu branch para o repositório remoto (`git push origin feature/NomeDaFeature`).
5. Abra um Pull Request para análise.

### Requisitos de Instalação

- **Python 3.x**
- **Biblioteca Pygame** (pode ser instalada via `pip install pygame`).

## Créditos

### Domínio Público

- [Som de um miado de gato](https://opengameart.org/content/meowing-cat-made-in-labchirp), disponibilizado por Traceletz.

### CC-BY

[Sprint do gatinho e do Fogo](https://opengameart.org/content/cat-fighter-addon1-energy-force-master-kit), disponibilizado por dogchicken.

[Som de Feitiço de Fogo](https://opengameart.org/content/spell-4-fire), disponibilizado por Bart K.

### CC BY-NC-ND

[Nebula de patas de gato](https://photo.m-j-s.net/blog/2019/07/ngc-6334-cats-paw-nebula/), registro fotográfico de Martin Junius, disponível em seu [site ofical](https://photo.m-j-s.net/blog/about/).

### Tutorial

Esse jogo foi baseado no tutorial de [Tech With Tim](https://www.youtube.com/@TechWithTim).
