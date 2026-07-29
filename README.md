# Betting Simulation - House Edge Visualization

A Monte Carlo simulation to demonstrate how the house edge works in repeated betting. Shows hundreds of possible paths and the inevitable long-term loss.

## Features
- Additive (fixed stake) and Multiplicative (proportional) betting models
- Customizable win probability, odds, number of paths, bets
- Beautiful matplotlib visualizations
- Statistics: ruin probability, expected return, Sharpe ratio, etc.
- Command Line Interface (CLI)
- Interactive Jupyter notebook

## Installation
```bash
pip install numpy matplotlib pandas seaborn
```

## Quick Start
```bash
python main.py --paths 500 --bets 1000 --p_win 0.48 --odds 1.95
```

## Project Structure
```
betting_simulation/
├── main.py                 # CLI entry point
├── simulation.py           # Core simulation logic
├── visualization.py        # Plotting functions
├── analysis.py             # Statistics and metrics
├── notebook.ipynb          # Interactive notebook
└── README.md
```

## Example Outputs
(See generated images in `/outputs/`)

This project clearly shows why "the house always wins in the long run."