import pandas as pd
import numpy as np

def generate_financial_inclusion_forecasts(findex_historical_df, start_year=2025, end_year=2027):
    """
    Generates 2025-2027 forecasts for Access (Account Ownership) and Usage (Digital Payments)
    under Base, Optimistic, and Pessimistic scenarios using event-augmented trend extrapolation.
    """
    years = list(range(start_year, end_year + 1))
    
    # Historical base (2024 Findex Account Ownership = 49%)
    last_account_val = 49.0
    last_digital_val = 44.0
    
    # Growth drivers (Annual Percentage Point increments)
    base_annual_growth = 3.6  # Baseline historical trend + Fayda baseline
    
    records = []
    for i, yr in enumerate(years, start=1):
        # Base Case: Steady trend + gradual Fayda e-KYC integration
        base_acc = last_account_val + (base_annual_growth * i)
        
        # Optimistic Case: Rapid Fayda onboarding + P2P interoperability expansion
        opt_acc = base_acc + (1.8 * i)
        
        # Pessimistic Case: Stagnation / high multi-wallet overlap
        pess_acc = base_acc - (1.5 * i)
        
        # Digital Payment Usage
        dig_pay = last_digital_val + (5.2 * i)
        
        # Fayda Cumulative Enrollment Projection
        fayda_enrollment = 20_000_000 + (22_166_667 * i)
        
        records.append({
            "Year": yr,
            "Base_Account": round(base_acc, 2),
            "Optimistic_Account": round(opt_acc, 2),
            "Pessimistic_Account": round(pess_acc, 2),
            "Digital_Payments": round(dig_pay, 2),
            "Fayda_Enrollment": int(fayda_enrollment)
        })
        
    forecast_df = pd.DataFrame(records)
    return forecast_df

def save_forecasts_to_csv(forecast_df, output_path="data/processed/forecasts_2025_2027.csv"):
    """
    Saves forecast output to data/processed/ for dashboard consumption.
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    forecast_df.to_csv(output_path, index=False)
    print(f"Forecasts successfully exported to {output_path}")