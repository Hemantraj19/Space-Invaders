# Space Invaders Game

This is a simple implementation of the classic game Space Invaders using Turtle graphics in Python. Below is a breakdown of the components and functionalities of the code:

## Components:

### 1. Invaders (`invaders.py`)
   - Manages the behavior of the invading aliens.
   - Handles the movement of the invaders.
   - Controls dropping bombs from the invaders.

### 2. Shooter (`shooter.py`)
   - Represents the player-controlled shooter.
   - Allows the shooter to move left and right.

### 3. Laser (`laser.py`)
   - Defines the laser fired by the shooter.
   - Controls the shooting mechanism.

### 4. Scoreboard (`scoreboard.py`)
   - Keeps track of the player's score.
   - Displays the score on the screen.

### 5. Heart (`heart.py`)
   - Manages the player's lives (hearts).
   - Displays the remaining hearts on the screen.

## Functionalities:

- The game starts with a player-controlled shooter at the bottom of the screen and a set of invading aliens at the top.
- The player can move the shooter left and right using the left and right arrow keys.
- Pressing the spacebar fires a laser from the shooter towards the aliens.
- Invading aliens move horizontally across the screen and periodically drop bombs towards the shooter.
- The player loses a life if hit by a bomb from the aliens.
- The game ends when the player loses all their lives or destroys all the invading aliens.
- A "Game Over" message is displayed upon game termination.

## Usage:

1. Ensure all required image files (`invader.png`, `shooter.png`, `heart.png`) are present in the same directory.
2. Run the Python script to start the game.
3. Use the left and right arrow keys to move the shooter.
4. Press the spacebar to shoot lasers at the invaders.
5. Press 's' to start the game.
6. Enjoy playing Space Invaders!

Feel free to modify the code, add new features, or improve existing ones to customize the game further!
