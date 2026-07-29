import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional

# Named Constants
FORECAST_YEARS: List[int] = [2025, 2026, 2027]
BASE_ANNUAL_GROWTH_PP: float = 3.6
OPTIMISTIC_ACCELERATION_PP: float = 1.8
PESSIMISTIC_FRICTION_PP: float = 1.5

@dataclass
class ForecastConfig:
    data_path: str = "data/processed/forecasts_2025_2027.csv"
    start_year: int = 2025
    end_year: int = 2027
    forecast_years: List[int] = None

    def __post_init__(self):
        if self.forecast_years is None:
            self.forecast_years = FORECAST_YEARS


def generate_financial_inclusion_forecasts(
    findex_historical_df: pd.DataFrame, 
    start_year: int = 2025, 
    end_year: int = 2027
) -> pd.DataFrame:
    """
    Generates scenario-based forecasts (2025-2027) for Access (Account Ownership) 
    and Usage (Digital Payments) using event-augmented trend extrapolation.
    """
    years: List[int] = list(range(start_year, end_year + 1))
    
    last_account_val: float = 49.0
    last_digital_val: float = 44.0
    
    if not findex_historical_df.empty and "Account_Ownership" in findex_historical_df.columns:
        last_account_val = float(findex_historical_df["Account_Ownership"].iloc[-1])
    if not findex_historical_df.empty and "Digital_Payments" in findex_historical_df.columns:
        last_digital_val = float(findex_historical_df["Digital_Payments"].iloc[-1])
        
    records: List[dict] = []
    for i, yr in enumerate(years, start=1):
        base_acc: float = last_account_val + (BASE_ANNUAL_GROWTH_PP * i)
        opt_acc: float = base_acc + (OPTIMISTIC_ACCELERATION_PP * i)
        pess_acc: float = base_acc - (PESSIMISTIC_FRICTION_PP * i)
        
        dig_pay: float = last_digital_val + (5.2 * i)
        fayda_enrollment: int = int(20_000_000 + (22_166_667 * i))
        
        records.append({
            "Year": yr,
            "Base_Account": round(base_acc, 2),
            "Optimistic_Account": round(opt_acc, 2),
            "Pessimistic_Account": round(pess_acc, 2),
            "Digital_Payments": round(dig_pay, 2),
            "Fayda_Enrollment": fayda_enrollment
        })
        
    return pd.DataFrame(records)


def save_forecasts_to_csv(
    forecast_df: pd.DataFrame, 
    output_path: str = ForecastConfig().data_path
) -> None:
    """
    Saves forecast output to data/processed/ for dashboard consumption.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    forecast_df.to_csv(output_path, index=False)