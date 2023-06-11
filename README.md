# Othello-AI

This is a project for Artificial Intelligence 🤖 course CSE472 at ASU-FE.

## Introduction

The project is an implementation of Othello (aka. Reversi) game 🎮 with an AI engine. 

In this project, we will explore the game playing of Othello using search algorithms and heuristics. Othello is a two-player strategy game played on a 8x8 board, where each player has pieces that are either black or white. The goal of the game is to have the most pieces of your color on the board at the end of the game.

For more information about the game, please refer to [Wikipedia](https://en.wikipedia.org/wiki/Reversi) 🌐.

For game rules, you can watch this [video](https://www.youtube.com/watch?v=zFrlu3E18BA) 📺.

## Game Description

The game has 3 modes with different difficulty levels:


| Game Mode |
| --- |
| Human vs Human |
| Human vs AI |
| AI vs AI |


Both of the AI modes has 3 difficulty levels:

| Difficulty Level | 
| --- |
| Easy |
| Medium |
| Hard |

## Game Algorithms

The game algorithms used in this project are:

1. The minimax algorithm: a basic search algorithm that examines all possible moves from a given position and selects the move that leads to the best outcome for the current player

2. Alpha-beta pruning: an improvement on the minimax algorithm that can reduce the number of nodes that need to be searched.

3. Alpha-beta pruning with iterative deepening (depth is increased iteratively in the search
tree until the timing constraints are violated)

The Algorithms are implemented in [alphaBetaPruning.py](./backend/alphaBetaPruning.py) and [MinMax.py](./backend/MinMax.py).

## Heuristics

// TODO

## The GUI

The GUI is implemented using [PyGame](https://www.pygame.org/news) 🐍🎮 and [pygame-menu](https://pygame-menu.readthedocs.io/en/latest/) 📃.

[![PyPI version](https://badge.fury.io/py/pygame.svg)](https://badge.fury.io/py/pygame) [![PyPI version](https://badge.fury.io/py/pygame-menu.svg)](https://badge.fury.io/py/pygame-menu)

GUI main functions are implemented in [othello_ui.py](./othello_ui.py).

## How to run the game

1. Clone the repo

```bash
git clone https://github.com/MahmoudAAbdelkader/Othello-AI.git

cd Othello-AI/
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Run the game

```bash
python othello_ui.py
```


