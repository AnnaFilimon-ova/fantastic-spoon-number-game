# 🔐 Password Cracking Game

## 📌 Description
Password Cracking Game is a simple number-guessing puzzle built with Pygame.  
The goal is to guess a hidden 5-digit code and get feedback after each attempt.

You can see how many numbers are correct and how many are in the correct position.

## 🎮 How to Play
- A random 5-digit code is generated (no repeated digits)
- You enter a 5-digit number
- The game gives you feedback:
  - how many digits are correct
  - how many are in the correct position
- Guess all digits in the correct order to win

## 🚀 Features
- Random 5-digit code generation
- Live keyboard input
- Backspace support
- Match counter (correct digits)
- Position counter (correct placement)
- Win screen when solved

## ⚙️ Installation
```bash
git clone <https://github.com/AnnaFilimon-ova/fantastic-spoon-number-game.git>
cd fantastic-spoon-number-game
source myenv/bin/activate
pip install pygame
python main.py
```

## 🎮 Controls
* `0–9` → enter digits
* `Backspace` → delete last digit
* `Enter` → submit answer
* Close window → exit game

## 🛠 Tech Stack
- Python 
- Pygame 

## ✨ Goal
Guess the secret 5-digit password using logic and deduction!
