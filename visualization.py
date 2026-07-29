import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import os


def plot_paths(cumulative, title="Betting Monte Carlo Simulations", save_path=None):
    """Plot all paths with mean highlighted"""
    plt.figure(figsize=(12, 7))
    
    # Plot individual paths
    for path in cumulative:
        plt.plot(path, color='skyblue', alpha=0.18, linewidth=0.6)
    
    # Mean path
    mean_path = np.mean(cumulative, axis=0)
    plt.plot(mean_path, color='gold', linewidth=3.5, label='Average Path')
    
    plt.xlabel('Number of Bets')
    plt.ylabel('Cumulative Capital')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)


    if save_path:
        dir_name = os.path.dirname(save_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()