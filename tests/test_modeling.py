import pytest
import pandas as pd
import os
from src.impact_model import build_association_matrix, load_impact_data
from src.forecasting import generate_financial_inclusion_forecasts, save_forecasts_to_csv, FORECAST_YEARS

def test_association_matrix_fallback():
    """Verify default fallback matrix is populated if datasets are empty."""
    matrix = build_association_matrix(pd.DataFrame(), pd.DataFrame())
    assert not matrix.empty
    assert "ACC_OWNERSHIP" in matrix.columns

def test_forecast_generation_shape():
    """Ensure forecast generation matches expected target horizon."""
    hist_df = pd.DataFrame({
        "Year": [2021, 2024],
        "Account_Ownership": [46.0, 49.0],
        "Digital_Payments": [35.0, 44.0]
    })
    forecast_df = generate_financial_inclusion_forecasts(hist_df)
    assert len(forecast_df) == len(FORECAST_YEARS)
    assert "Base_Account" in forecast_df.columns

def test_forecast_values_range():
    """Verify logical scenario order: Optimistic >= Base >= Pessimistic."""
    hist_df = pd.DataFrame({"Year": [2024], "Account_Ownership": [49.0], "Digital_Payments": [44.0]})
    forecast_df = generate_financial_inclusion_forecasts(hist_df)
    
    last_row = forecast_df.iloc[-1]
    assert last_row["Optimistic_Account"] >= last_row["Base_Account"]
    assert last_row["Base_Account"] >= last_row["Pessimistic_Account"]

def test_missing_data_load_handling():
    """Ensure graceful handling when loading non-existent files."""
    events, impact = load_impact_data("non_existent_file.csv")
    assert events.empty
    assert impact.empty

def test_save_forecasts_utility(tmp_path):
    """Check artifact export utility saves correctly to specified path."""
    sample_df = pd.DataFrame({"Year": [2025], "Base_Account": [52.6]})
    output_file = tmp_path / "test_forecast.csv"
    
    save_forecasts_to_csv(sample_df, str(output_file))
    assert os.path.exists(output_file)

def test_forecast_constants():
    """Verify forecast configuration constants."""
    assert FORECAST_YEARS == [2025, 2026, 2027]