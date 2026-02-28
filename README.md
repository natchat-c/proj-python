# Shooter Game 

A 2D shooter game built in **Python** using **Pygame**.  
This project demonstrates how to create a basic space shooter where the player controls a rocket, shoots enemies, and tries to survive as long as possible.

## About

This is a beginner friendly Python game that showcases basic game loop logic, sprite handling, collision detection, and sound integration using the **Pygame** library.

You control a rocket at the bottom of the screen, shoot incoming enemies, and avoid being hit or missing enemies.

## Features

- Player movement (left/right)
- Shooting bullets
- Enemy spawn & descent
- Score tracking
- Win and lose conditions
- Background music and sound effects

## How to Play

1. **Clone the repository**

```bash
git clone https://github.com/natchat-c/proj-python.git
```

2. **Install dependencies**

```bash
pip install pygame
```
3. **Run the game**

```bash
python shooter_game.py
```

## Controls
| Key   | Action      |
| ----- | ----------- |
| ←     | Move left   |
| →     | Move right  |
| SPACE | Fire bullet |

## Game Rules

- The player loses after an enemy escape the bottom of the screen.
- The player wins when 10 enemies are shot.
- Colliding with an enemy results in a loss.

## Project Structure

```
proj-python/
├── main.py
├── shooter_game.py       # Main game logic
├── galaxy.jpg            # Background image
├── rocket.png            # Player sprite
├── ufo.png               # Enemy sprite
├── bullet.png            # Bullet sprite
├── PhantomfromSpace.wav  # Background music
├── fire.ogg              # Shooting sound
└── README.md
```

## Requirements

- Python 3.x
- Pygame library

## License

This project is released under the CC0-1.0 License — meaning it’s dedicated to the public domain. Feel free to use, modify, and share!
