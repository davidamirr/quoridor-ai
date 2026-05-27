# Quoridor AI Project

A complete, production-quality implementation of the classic board game **Quoridor**, featuring multiple AI difficulty levels, robust pathfinding, and full Undo/Redo capabilities. Developed in Python using Pygame for a university AI course project.

![Quoridor Gameplay](https://via.placeholder.com/800x450.png?text=Quoridor+Gameplay+Screenshot)

## 🌟 Features

- **Full Game Logic:** 100% accurate implementation of Quoridor rules, including diagonal pawn jumping, wall collision, and path verification.
- **Advanced AI Opponents:**
  - **Easy:** Makes random, valid moves with occasional wall placements.
  - **Medium:** Heuristic-driven logic that greedily follows the shortest path and blocks the player when threatened.
  - **Hard:** Advanced Minimax algorithm with Alpha-Beta pruning, utilizing custom board evaluation heuristics.
- **Robust Pathfinding:** BFS-based pathfinding ensures walls can never completely box in any player.
- **Full Undo/Redo Stack:** Mistakes happen! Use the UI buttons or standard keyboard shortcuts (`Ctrl+Z` / `Ctrl+Y`) to traverse the game state history seamlessly.
- **Modern GUI:** Clean, visually appealing Pygame interface with valid move highlighting, wall placement preview colors, and turn indicators.
- **Game Modes:** Support for Human vs Human (PvP) and Human vs AI.

## 🛠 Project Structure

```
/
├── main.py                 # Game entry point and event loop
├── game/                   # Core game logic
│   ├── board.py            # Board state and wall management
│   ├── constants.py        # System-wide configuration
│   ├── game_state.py       # Centralized immutable-safe state manager
│   ├── history_manager.py  # Undo/Redo logic using a state-history stack
│   ├── player.py           # Player dataclass and goals
│   ├── rules.py            # Movement validation and pawn jump logic
│   └── wall.py             # Wall dataclass
├── ai/                     # Artificial Intelligence logic
│   ├── easy_ai.py          # Random valid moves
│   ├── medium_ai.py        # Shortest path heuristics
│   ├── hard_ai.py          # Minimax Alpha-Beta entry point
│   ├── heuristics.py       # Board evaluation functions
│   ├── minimax.py          # Minimax algorithm implementation
│   └── pathfinding.py      # BFS graph traversal
├── ui/                     # Presentation layer
│   ├── button.py           # Pygame interactive button component
│   └── renderer.py         # Pygame drawing routines
├── requirements.txt        # Python dependencies
└── README.md               # You are here
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/quoridor-ai.git
   cd quoridor-ai
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Play

Run the main game file to launch the GUI:
```bash
python main.py
```

### Controls

- **Move Pawn:** Click on any highlighted adjacent cell.
- **Place Wall:** Hover your mouse between cells. If the preview is green, click to place a wall. The orientation (horizontal/vertical) is determined by where you hover within the cell intersection.
- **Undo Move:** Press `Ctrl+Z` or click the `Undo` button.
- **Redo Move:** Press `Ctrl+Y` or click the `Redo` button.
- **Change Game Mode:** Use the mode selectors on the right to toggle between PvP and various AI difficulties.
- **Restart Game:** Click the `Restart` button to reset the board instantly.

## 🧠 AI & Architecture Highlights

- **State Management:** The game operates on a centralized `GameState` object. Rather than mutating a single board and attempting to reverse commands, every move creates a deep copy of the state, ensuring that the Undo/Redo system (`history_manager.py`) is completely bug-free and mathematically sound.
- **Minimax with Alpha-Beta Pruning:** The Hard AI evaluates future board states by simulating pawn moves and a curated, highly heuristic subset of wall placements (walls immediately around the opponent). This dramatically cuts down the branching factor, allowing depth-based search to run fast in Python.
- **Pathfinding:** Before any wall is placed, the board uses a Breadth-First Search (BFS) to guarantee that a path still exists for all players.

## 🎥 Demo Video

[Link to Demo Video Placeholder]

## 👥 Contributors

- Your Name - *Lead Developer & AI Architect*
