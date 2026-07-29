import numpy as np

def analyze_results(cumulative):
    """Generate key statistics"""
    final_wealth = cumulative[:, -1] #last column of the cumsum or cumprod
    
    stats = {
        "Mean Final Wealth": np.mean(final_wealth),
        "Median Final Wealth": np.median(final_wealth),
        "Ruin Probability (%)": np.mean(final_wealth <= 0) * 100,
        "Paths Profitable (%)": np.mean(final_wealth > 1000) * 100,  # assuming initial 1000
        "Max Drawdown (Mean)": np.mean(np.max(np.maximum.accumulate(cumulative, axis=1) - cumulative, axis=1))
    }
    return stats