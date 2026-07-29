import argparse
from simulation import run_monte_carlo_simulation, calculate_ruin_probability
from visualization import plot_paths
from analysis import analyze_results

def main():
    parser = argparse.ArgumentParser(description="Betting House Edge Monte Carlo Simulator")
    parser.add_argument('--paths', type=int, default=400, help='Number of simulation paths')
    parser.add_argument('--bets', type=int, default=1000, help='Number of bets per path')
    parser.add_argument('--p_win', type=float, default=0.48, help='True win probability')
    parser.add_argument('--odds', type=float, default=1.95, help='Decimal odds')
    parser.add_argument('--model', choices=['additive', 'multiplicative'], default='additive')
    parser.add_argument('--fraction', type=float, default=0.05, help='Bet fraction for multiplicative')
    parser.add_argument('--output', default='outputs/simulation.png', help='Output image path')
    
    args = parser.parse_args()
    
    print(f"Running {args.paths} paths × {args.bets} bets | Model: {args.model}")
    
    cumulative = run_monte_carlo_simulation(
        num_paths=args.paths,
        num_bets=args.bets,
        p_win=args.p_win,
        odds=args.odds,
        model=args.model,
        fraction=args.fraction
    )
    
    # Statistics
    stats = analyze_results(cumulative)
    for k, v in stats.items():
        print(f"{k}: {v:.2f}")
    
    # Plot
    title = f"House Edge Simulation ({args.model.capitalize()} Model)"
    plot_paths(cumulative, title=title, save_path=args.output)
    print(f"Plot saved to {args.output}")

if __name__ == "__main__":
    main()