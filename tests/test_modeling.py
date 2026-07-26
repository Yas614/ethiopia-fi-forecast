import pytest
import pandas as pd
import os
from src.impact_model import build_association_matrix
from src.forecasting import generate_financial_inclusion_forecasts

def test_association_matrix_fallback():
    matrix = build_association_matrix(pd.DataFrame(), pd.DataFrame())
    assert not matrix.empty
    assert "ACC_OWNERSHIP" in matrix.columns

def test_forecast_generation_shape():
    hist_df = pd.DataFrame({
        "Year": [2021, 2024],
        "Account_Ownership": [46.0, 49.0]
    })
    forecast_df = generate_financial_inclusion_forecasts(hist_df)
    assert len(forecast_df) == 3  # Years 2025, 2026, 2027
    assert "Base_Account" in forecast_df.columns

def test_forecast_values_range():
    hist_df = pd.DataFrame({"Year": [2024], "Account_Ownership": [49.0]})
    forecast_df = generate_financial_inclusion_forecasts(hist_df)
    # Optimistic should be greater than or equal to Base Case
    assert forecast_df["Optimistic_Account"].iloc[-1] >= forecast_df["Base_Account"].iloc[-1]

def test_processed_data_output_exists():
    path = "data/processed/forecasts_2025_2027.csv"
    assert os.path.exists(path)