import numpy as np

def run_monte_carlo_simulation(
    num_paths=300,
    num_bets=800,
    p_win=0.48,
    odds=1.95,
    bet_size=10,
    model='additive',
    initial_capital=1000,
    fraction=0.05
):
    """
    Run Monte Carlo simulation for betting paths.
    
    model: 'additive' (fixed stake) or 'multiplicative' (proportional)
    """
    np.random.seed(42)
    
    # Generate all outcomes at once
    wins = np.random.rand(num_paths, num_bets) < p_win
    
    if model == 'additive':
        returns = np.where(wins, odds - 1, -1) * bet_size
        cumulative = np.cumsum(returns, axis=1)
        # Add initial capital
        cumulative = initial_capital + cumulative
    else:  # multiplicative
        multipliers = np.where(wins, 1 + (odds - 1) * fraction, 1 - fraction)
        # Cumulative product
        cumulative = np.cumprod(multipliers, axis=1) * initial_capital
    
    return cumulative


def calculate_ruin_probability(cumulative, ruin_threshold=0):
    """Calculate % of paths that hit ruin"""
    ruined = np.any(cumulative <= ruin_threshold, axis=1)
    return np.mean(ruined) * 100