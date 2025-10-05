# numberGuessingGame
In this program, after execution of codes, it will generate a random no between 1 to 100 and you have to guess it.

# 🎯 Number Guessing Game (Python)

A simple and fun **Number Guessing Game** built using Python’s `random` module.  
This game challenges the player to guess a randomly generated number between **1 and 100**.  

---

## 🧠 Game Rules

1. The computer generates a **random number** between **1 and 100**.  
2. The player must **guess the correct number**.  
3. After each guess:
   - If your guess is **too high**, you'll be prompted to guess a **smaller number**.  
   - If your guess is **too low**, you'll be prompted to guess a **bigger number**.  
4. Type **`Quit`** or **`quit`** to exit the game at any time.  
5. When the correct number is guessed, the game congratulates you and ends.  

## ⚙️ How It Works

This project uses:
- **`random.randint(1,100)`** to generate a random target number.
- A **while loop** to keep the game running until the user wins or quits.
- **Conditional statements** to compare the guesses and provide hints.

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed on your system.  
2. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/number-guessing-game.git
   
---

✅ **How to Use This Entire Block**
1. Create a new folder, say `number-guessing-game`.  
2. Inside it, make two files:  
   - `guess_game.py` → paste the first Python code.  
   - `README.md` → paste the second part (starting with `# 🎯 Number Guessing Game`).  
3. Then run:
   ```bash
   git add .
   git commit -m "Added Number Guessing Game with README"
   git push origin main
