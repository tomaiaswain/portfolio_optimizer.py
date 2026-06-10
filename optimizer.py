# =====================================================================
# PROJECT 4: MONTE CARLO PORTFOLIO OPTIMIZATION ENGINE
# =====================================================================
import random
import math

# PHASE 1: MARKET DATA INGESTION
# Simulating expected annual returns and volatility (risk) for 4 major assets
market_data = {
    "AAPL": {"expected_return": 0.15, "volatility": 0.20}, # 15% return, 20% risk
    "MSFT": {"expected_return": 0.12, "volatility": 0.18},
    "NVDA": {"expected_return": 0.35, "volatility": 0.45},
    "TSLA": {"expected_return": 0.25, "volatility": 0.50}
}
risk_free_rate = 0.04 # 4% Treasury Bond yield

def run_monte_carlo_simulation(iterations=5000):
    print(f"⚙️  [ENGINE] Running Monte Carlo Simulation: {iterations:,} Portfolio Combinations...")
    
    best_portfolio = None
    max_sharpe_ratio = 0.0
    
    # PHASE 2: ALGORITHMIC SIMULATION
    for i in range(iterations):
        # 1. Generate random investment weights that equal 100% (1.0)
        weights = {ticker: random.random() for ticker in market_data}
        total_weight = sum(weights.values())
        weights = {ticker: w / total_weight for ticker, w in weights.items()}
        
        # 2. Calculate Expected Portfolio Return
        portfolio_return = sum(weights[t] * market_data[t]["expected_return"] for t in market_data)
        
        # 3. Calculate Portfolio Volatility (Simplified Risk Approximation)
        # In production, this uses a covariance matrix. Here, we simulate diversification benefits.
        base_volatility = sum(weights[t] * market_data[t]["volatility"] for t in market_data)
        diversification_discount = 0.85 
        portfolio_risk = base_volatility * diversification_discount
        
        # 4. Calculate the Sharpe Ratio (Reward per unit of Risk)
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk
        
        # 5. Store the best performing algorithm
        if sharpe_ratio > max_sharpe_ratio:
            max_sharpe_ratio = sharpe_ratio
            best_portfolio = {
                "weights": weights,
                "return": portfolio_return,
                "risk": portfolio_risk,
                "sharpe": sharpe_ratio
            }
            
    return best_portfolio

# PHASE 3: EXECUTIVE DASHBOARD OUTPUT
def generate_investment_proposal(optimal_portfolio):
    print("\n=========================================================")
    print("      AI WEALTH MANAGEMENT: OPTIMAL EFFICIENT FRONTIER   ")
    print("=========================================================")
    print(f"🎯 MAXIMUM SHARPE RATIO ACHIEVED: {optimal_portfolio['sharpe']:.2f}")
    print("---------------------------------------------------------")
    print("💰 RECOMMENDED ASSET ALLOCATION:")
    for ticker, weight in optimal_portfolio["weights"].items():
        print(f"   -> {ticker}: {weight * 100:>5.1f}%")
    print("---------------------------------------------------------")
    print(f"📈 PROJECTED ANNUAL RETURN:       {optimal_portfolio['return'] * 100:.1f}%")
    print(f"⚠️  PROJECTED PORTFOLIO RISK:      {optimal_portfolio['risk'] * 100:.1f}%")
    print("=========================================================\n")

# Execute the pipeline
optimal_result = run_monte_carlo_simulation(iterations=10000)
generate_investment_proposal(optimal_result)
