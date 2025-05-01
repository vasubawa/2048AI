# 2048 AI Game

This project implements an AI for the popular game 2048 using various algorithms. The AI can be selected through a graphical user interface (GUI), allowing users to experiment with different strategies.

## Project Structure

```
2048AI/
├── main.py             # Main entry point
├── game.py             # 2048 game logic
├── gui.py              # GUI implementation
├── algorithms/         # Different AI algorithms
│   ├── __init__.py     # Package initialization
│   ├── minimax.py      # Minimax algorithm
│   ├── mcts.py         # Monte Carlo Tree Search
│   ├── expectimax.py   # Expectimax algorithm
│   └── dqn.py          # Deep Q-Network (reinforcement learning)
└── utils.py            # Helper functions
```

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/vasubawa/2048AI
   cd 2048AI
   ```

2. Install any required packages (if applicable):
   ```
   pip install -r requirements.txt
   ```

### Running the Game

To start the game, run the following command:

```
python main.py
```

https://www.pygame.org/docs/

### Selecting Algorithms (If applicable)

In the GUI, you can choose from different AI algorithms implemented in the `algorithms` directory. Each algorithm has its own strengths and weaknesses, so feel free to experiment!

## Algorithms Overview

- **Minimax**: A decision-making algorithm that evaluates possible moves and selects the best one based on a heuristic.
- **Monte Carlo Tree Search (MCTS)**: Uses random sampling to evaluate potential outcomes of moves.
- **Expectimax**: A variant of Minimax that accounts for chance events in the game.
- **Deep Q-Network (DQN)**: A reinforcement learning approach that allows the AI to learn optimal moves through experience.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
