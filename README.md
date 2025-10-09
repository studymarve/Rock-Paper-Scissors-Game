🎮 Rock Paper Scissors Game (v4 → v5 Evolution)

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A modular, Python-based Rock Paper Scissors game built to practice clean code, structure, and creativity — inspired by [Programming with Mosh](https://www.youtube.com/c/programmingwithmosh).

🧭 Summary

**Rock Paper Scissors v4** is a modular Python CLI game designed and architected by **Olawale Marvellous**.  
Built from scratch with creativity, planning, and minimal AI assistance for debugging and structure, it demonstrates how a beginner can think like a **software architect** — breaking logic into reusable modules while keeping gameplay fun and educational.

 🚀 About the Project

This project began as a simple CLI experiment and evolved through multiple versions.  
By **v4**, it became fully modular — each file handles one responsibility (logic, scoring, display, etc.).

Future versions (v5–v10) will explore:
- Object-Oriented Programming (Player & Game classes)
- Data persistence and player stats
- Personality-driven messages
- AI gesture recognition

The long-term goal is to make this both a **learning project for developers** and a **creative foundation for future AI-based games**.

🧠 Features

✅ Modular file structure  
✅ Two game modes (Infinity ♾️ and Round 🏆)  
✅ Score tracking and personality messages  
✅ Game history logging  
✅ Clean input validation  
✅ Developer-friendly and beginner-focused design  

🧩 File Overview

| File | Description |
|------|--------------|
| `welcome.py` | Handles player input and welcome messages |
| `game_logic.py` | Core rules and game logic |
| `get_computer_choice.py` | Random computer move generator |
| `display.py` | Handles emoji display of player choices |
| `winner.py` | Determines round outcome |
| `result.py` | Tracks and updates score |
| `messages.py` | Generates personality-based comments |
| `history.py` | Saves match history to a text file |
| `utils.py` | Helper functions (yes/no, integer validation) |
| `method.py` | Selects game mode |
| `game_mode.py` | Controls gameplay loop |
| `fixed_main.py` | Main entry point for running the game |

🔭 Future Roadmap

| Version | Focus | Skills Learned |
|----------|--------|----------------|
| **v5** | Refactor with OOP (Player & Game classes) | Classes, attributes, encapsulation |
| **v6** | Save/load player stats (JSON) | File handling, data persistence |
| **v7** | GUI version | Tkinter or visual terminal design |
| **v8** | Multiplayer mode | State management |
| **v9** | AI opponent | Pattern detection, basic ML |
| **v10** | Gesture recognition | Computer vision (OpenCV) |

🧑‍💻 How to Run

Make sure you have **Python 3.10+** installed.

```bash
# Clone this repository
git clone https://github.com/<your-username>/rock-paper-scissors-game.git
cd rock-paper-scissors-game

# Run the game
python fixed_main.py


---

💡 Learning Purpose

This project is part of my self-learning journey inspired by:

Code With Mosh

Python Official Documentation

AI-assisted development (DeepSeek, Claude, GPT) — for structure, not creativity


🧩 My rule: I design the logic; AI helps me implement it efficiently.
This balance keeps my creativity and understanding at the center of every build.


---

🤝 How to Contribute

Contributions are welcome!

1. Fork this repo


2. Create a feature branch (git checkout -b feature-new-idea)


3. Commit your changes (git commit -m "Add new feature")


4. Push to the branch (git push origin feature-new-idea)


5. Open a Pull Request



Suggestions, refactors, and new ideas are always appreciated — especially from other learners and developers building their own versions.



🪪 License

This project is licensed under the MIT License — see the LICENSE file for details.
You’re free to use, learn from, and modify this project, but please give proper credit.


---

🌟 Acknowledgments

Programming with Mosh — for inspiring clean code habits and learning discipline.

Python Docs — for clear, official documentation.

All open learners and developers — who believe in learning by building.


> 🧭 “Build small projects deeply, not big projects shallowly.”
— Mosh Hamedani
