# Meow Mewar - Battle for Territory

## Description

Welcome to the **Meow Mewar**, an intergalactic two-player game where two cosmic cats fight for spatial domination. The Red Cat and the Blue Cat face off in an epic battle using fireballs and agile movements. Each player has 7 lives, and the goal is to deplete the opponent's lives before your own run out.

## Story

In a distant corner of the galaxy, where the stars shine brightly, two legendary cats — **Red Cat** and **Blue Cat** — wage war for control of their territory. Using their unique skills and energetic fireballs, they are willing to fight to the end. The fate of the intergalactic cat universe is in your hands!

## How to Play

- **Start the Game**

  - Use the arrow keys to select the Play option, "Jogar".
  - The selected option will be blue.

- **Player 1 (Red Cat)**:

  - Moves using the **W, A, S, D** keys.
  - Fires fireballs by pressing **Left Ctrl**.

- **Player 2 (Blue Cat)**:
  - Moves using the **arrow keys**.
  - Fires fireballs by pressing **Right Ctrl**.

## Game Rules

- Each player starts with **7 lives**.
- A life is lost every time a player is hit by a fireball from the opponent.
- The game ends when one player's lives
- The last surviving player is crowned the winner of the intergalactic battle!

## Objective

- Be the last intergalactic cat standing by depleting your opponent's lives!

## How to Run

1. Make sure Python and the `Pygame` library are installed on your system.
2. Run the following command in the terminal to start the game:

   ```bash
   python principal.py
   ```

## For Developers

This game was developed using **Python** and the **Pygame** library. Below is a summary of the structure and the main components of the code:

### Key Global Variables

- **LARGURA, ALTURA**: Dimensions of the game window (900x500 pixels).
- **VEL**: Movement speed of the cats (5 pixels per frame).
- **FOGO_VEL**: Speed of the fire projectiles (7 pixels per frame).
- **MAX_FOGO**: Maximum number of fireballs each player can have on the screen at once (3 per player).
- **VIDA_FONTE** and **GANHADOR_FONTE**: Fonts for displaying the remaining lives and the winner message.

### Resource Structure

The game's graphic and sound resources are located in the `Recursos` folder.

### Main Functions

- **`desenhar_janela()`**: Responsible for rendering the screen every frame, including the players' positions, fireballs, and remaining lives.
- **`movimentar_vermelho()`** and **`movimentar_azul()`**: Control the movement of the cats based on the keys pressed.
- **`controlhe_fogo()`**: Updates the position of the fireballs and checks for collisions with the opponent. It also removes fireballs that go off-screen.
- **`ganhador_escrever()`**: Displays the winner on the screen and pauses the game for 3 seconds before restarting.

### Custom Events

- **`VERMELHO_ACERTADO`** and **`AZUL_ACERTADO`**: Custom events triggered when one of the cats is hit by a fireball. They decrease the hit player's health.

### Game Loops and Mechanics

The main game loop controls the following:

1. Captures input events, such as movement keys and fireball shots.
2. Updates the position of the characters and projectiles.
3. Checks for collisions and handles health reduction.
4. Updates the screen each frame to reflect the current state of the game.

### How to Contribute

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/FeatureName`).
3. Commit your changes (`git commit -m 'Adding new feature'`).
4. Push your branch to the remote repository (`git push origin feature/FeatureName`).
5. Open a Pull Request for review.

### Installation Requirements

- **Python 3.x**
- **Pygame Library** (can be installed via `pip install pygame`).

## Credits

### Public Domain

- [Cat meow sound](https://opengameart.org/content/meowing-cat-made-in-labchirp), provided by Traceletz.

### CC-BY

[Cat and Fire Sprites](https://opengameart.org/content/cat-fighter-addon1-energy-force-master-kit), provided by dogchicken.

[Fire Spell Sound](https://opengameart.org/content/spell-4-fire), provided by Bart K.

### CC BY-NC-ND

[Cat's Paw Nebula](https://photo.m-j-s.net/blog/2019/07/ngc-6334-cats-paw-nebula/), photographic record by Martin Junius, available on his [official website](https://photo.m-j-s.net/blog/about/).

### Tutorial

This game is based on the tutorial by [Tech With Tim](https://www.youtube.com/@TechWithTim).
