
I have built a simple command-line battle game in Python called "Defeat the Evil Wizard". It allows players to choose a fantasy character class and fight an evil wizard in a turn-based duel. 
The project demonstrates object-oriented programming (OOP) principles in a beginner-friendly and interactive way. 

Features:

- Players choose from four unique classes — Warrior, Mage, Archer, or Paladin — each with its own stats, special ability, and defense mechanic.
- On each turn, players choose to attack, use a special ability, heal/defend/evade, or view current stats.
- The Evil Wizard attacks each round and regenerates health.
- At the end of the game, a summary displays total turns, damage dealt, and damage taken.

The project is organized into two files — one for character class logic (`characters.py`) and one for the game loop (`main.py`).
It includes Object-oriented design (OOP): classes, inheritance, and method overriding.

I used Python classes to model game characters and their behavior. Each class overrides shared methods like `special_ability()` or `heal()` to provide unique gameplay. 
The game loop uses conditionals and input validation to handle player actions. 

I have ensured that all the required features are implemented, and the game is fully functional by running it in my Terminal.
