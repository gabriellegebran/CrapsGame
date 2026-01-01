# CrapsGame
A simple Craps casino game built in Unity using C# and TextMeshPro. The player enters their name and starting amount, places bets using chips, rolla two dices, and wins or loses money based on classic Craps rules.

## Features
- Player name input
- Custom starting balance
- Betting system with chip values:
    - 1$
    - 5$
    - 25$
    - 200$
- Random dice rolls (1-6)
- Automatic sum calculation
- Win / Lose logic basedf on Craps rules
- Two-page UI flow
    - Start page (player setup)
    - Game page (betting & dice)
- Prevents betting while a round is in progress

## Technologies Used
- Unity
- C#
- TextMeshPro
- Unity UI (Buttons, Input Fields, GameObjects)

## How to Play
1. Enter your name and starting amount
2. Click Enregistrer to start the game
3. Place the bet using the chip buttons
4. Click Lancer to roll the dice
5. The game will:
   - Instantly win or lose on first roll OR
   - Set a "point" and continue rolling
6. Your balance updates automatically after each round

## Possible Improvements
- Dice roll animations
- Sound effects
- Custom chip values
- Restart game button
- Multiplayer mode

## Learning Objectives
This project was built to practice:
- Unity UI management
- C# scripting
- Game logic implementation
- State control in games
- Randomization

## License
This project is intended for educational purposes and is free to use or modify
