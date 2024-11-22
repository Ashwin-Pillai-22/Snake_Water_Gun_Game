# Snake-Water-Gun Game

This is a Python implementation of the classic "Snake-Water-Gun" game, a fun and simple game you can play against the computer.

## How the Game Works:

- There are three entities in the game: **Snake**, **Water**, and **Gun**.
- The interactions between the entities follow these rules:
  1. **Snake**:
     - **Wins against Water** (Snake drinks water).
     - **Loses to Gun** (Gun kills snake).
  2. **Water**:
     - **Wins against Gun** (Water rusts the gun).
     - **Loses to Snake** (Snake drinks water).
  3. **Gun**:
     - **Wins against Snake** (Gun kills snake).
     - **Loses to Water** (Water rusts the gun).

### Example Scenarios:
1. **You choose Gun, and the computer chooses Snake**:  
   **Result:** You win because Gun kills Snake.
2. **You choose Gun, and the computer chooses Water**:  
   **Result:** You lose because Water rusts the Gun.

---

### Features:
- Play against the computer.
- Simple rules and easy to understand.
- A nostalgic game for everyone to enjoy.
