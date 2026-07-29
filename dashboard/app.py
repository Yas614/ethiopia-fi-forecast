import sys
import os

# --- PATH RESOLUTION (MUST BE BEFORE ANY LOCAL IMPORTS) ---
# Calculates the root directory (ethiopia-fi-forecast) and inserts it at index 0
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Standard Third-Party Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Local Project Module Imports (Line 11 works cleanly now!)
from src.impact_model import load_impact_data, build_association_matrix
from src.forecasting import generate_financial_inclusion_forecasts
# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Analytics Platform",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA PROCESSING & CACHING ---
@st.cache_data
def load_dashboard_datasets():
    # Historical Global Findex Data
    findex_df = pd.DataFrame({
        "Year": [2011, 2014, 2017, 2021, 2024],
        "Account_Ownership": [14.0, 22.0, 35.0, 46.0, 49.0],
        "Digital_Payments": [1.0, 3.0, 12.0, 35.0, 44.0],
        "Mobile_Money": [0.0, 0.1, 0.3, 4.7, 9.45]
    })
    
    # Try loading precomputed forecast artifact or generate dynamically
    processed_file = "data/processed/forecasts_2025_2027.csv"
    if os.path.exists(processed_file):
        forecast_df = pd.read_csv(processed_file)
    else:
        forecast_df = generate_financial_inclusion_forecasts(findex_df)

    # Load Impact Modeling Datasets
    raw_data_path = "data/raw/ethiopia_fi_unified_data.csv"
    if not os.path.exists(raw_data_path):
        raw_data_path = "../data/raw/ethiopia_fi_unified_data.csv"
        
    events_df, impact_links_df = load_impact_data(raw_data_path)
    association_matrix = build_association_matrix(events_df, impact_links_df)
    
    events_timeline = pd.DataFrame([
        {"Year": 2021, "Event": "Telebirr Launch", "Category": "Product Launch", "Impact": "Rapid Mobile Money Onboarding"},
        {"Year": 2022, "Event": "Safaricom Entry", "Category": "Infrastructure", "Impact": "Telecom Market Liberalization"},
        {"Year": 2023, "Event": "M-Pesa Launch", "Category": "Product Launch", "Impact": "Interoperable Payment Expansion"},
        {"Year": 2024, "Event": "EthSwitch P2P Scale", "Category": "Infrastructure", "Impact": "P2P Transfers Crossover Cash ATM"}
    ])
    
    return findex_df, forecast_df, association_matrix, events_timeline

findex_data, forecast_data, association_matrix, events_data = load_dashboard_datasets()

# --- SIDEBAR CONTROLS ---
st.sidebar.markdown("### 🏛️ Navigation & Filters")
page = st.sidebar.radio(
    "Select Interface View:",
    [
        "Executive Dashboard", 
        "Historical Findex Trends", 
        "Macro Impact Analysis", 
        "Scenario Projections (2025-2027)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Scenario Parameters")
selected_target_year = st.sidebar.select_slider("Forecast Target Year:", options=[2025, 2026, 2027], value=2027)
selected_scenario = st.sidebar.selectbox("Active Forecast Model:", ["Base Case", "Optimistic", "Pessimistic"])

st.sidebar.markdown("---")
st.sidebar.caption("🔒 **National Bank of Ethiopia & Policy Framework Aligned**")

# --- PAGE 1: EXECUTIVE DASHBOARD ---
if page == "Executive Dashboard":
    st.title("🏛️ Ethiopia Financial Inclusion Policy & Forecast Engine")
    st.markdown("Macro-level analytics evaluating account ownership, digital payments, and policy intervention trajectories.")
    
    st.markdown("---")
    
    # KPI Row with standard professional styling
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(
        label="2024 Formal Account Baseline",
        value="49.0%",
        delta="+3.0% (2021-2024)"
    )
    
    # Dynamic computation for scenario target metric
    target_row = forecast_data[forecast_data["Year"] == selected_target_year].iloc[0]
    metric_col_map = {
        "Base Case": "Base_Account",
        "Optimistic": "Optimistic_Account",
        "Pessimistic": "Pessimistic_Account"
    }
    projected_val = target_row[metric_col_map[selected_scenario]]
    
    col2.metric(
        label=f"{selected_target_year} Projected Account Share ({selected_scenario})",
        value=f"{projected_val:.2f}%",
        delta=f"{projected_val - 49.0:+.2f}% vs 2024"
    )
    
    col3.metric(
        label="Digital P2P / ATM Ratio",
        value="1.42x",
        delta="P2P Exceeds Cash ATM"
    )
    
    col4.metric(
        label="Fayda e-KYC Target (2027)",
        value="86.7M",
        delta="National ID Integration"
    )
    
    st.markdown("---")
    
    # Overview Layout
    c1, c2 = st.columns([3, 2])
    
    with c1:
        st.subheader("📈 National Forecast vs Target Benchmark")
        fig_overview = go.Figure()
        fig_overview.add_trace(go.Scatter(x=findex_data["Year"], y=findex_data["Account_Ownership"], mode='lines+markers', name='Historical', line=dict(color='#1f77b4', width=3)))
        fig_overview.add_trace(go.Scatter(x=forecast_data["Year"], y=forecast_data["Base_Account"], mode='lines+markers', name='Base Forecast', line=dict(color='#2ca02c', dash='dash')))
        fig_overview.add_hline(y=60.0, line_dash="dot", line_color="#ff7f0e", annotation_text="60% NFIS-II Benchmark Target")
        fig_overview.update_layout(xaxis_title="Year", yaxis_title="Percentage of Adult Population (%)", margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_overview, use_container_width=True)
        
    with c2:
        st.subheader("📌 Key Strategic Directives")
        st.info("**Primary Growth Driver:** Mobile wallet onboarding via Telebirr and M-Pesa expanded access to digital accounts rapidly between 2021 and 2024.")
        st.warning("**Structural Stagnation Risk:** Account growth slowed to +1.0% per year due to account duplication and friction in transitioning wallet users to formal bank savings accounts.")

# --- PAGE 2: HISTORICAL TRENDS ---
elif page == "Historical Findex Trends":
    st.title("📊 Historical Findex Indicators (2011–2024)")
    st.markdown("Detailed channel decomposition of financial inclusion metrics based on World Bank Global Findex benchmarks.")
    
    selected_metrics = st.multiselect(
        "Select Indicators for Comparative Analysis:",
        ["Account_Ownership", "Digital_Payments", "Mobile_Money"],
        default=["Account_Ownership", "Digital_Payments"]
    )
    
    fig_hist = go.Figure()
    for metric in selected_metrics:
        fig_hist.add_trace(go.Scatter(
            x=findex_data["Year"], 
            y=findex_data[metric],
            mode='lines+markers',
            name=metric.replace("_", " ")
        ))
    
    fig_hist.update_layout(xaxis_title="Year", yaxis_title="Population Share (%)", hovermode="x unified")
    st.plotly_chart(fig_hist, use_container_width=True)
    st.dataframe(findex_data, use_container_width=True)

# --- PAGE 3: MACRO IMPACT ANALYSIS ---
elif page == "Macro Impact Analysis":
    st.title("🔍 Macro Interventions & Event Impact Modeling")
    st.markdown("Evaluation of major product rollouts, market liberalizations, and infrastructure deployments.")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        st.subheader("🔥 Event-Indicator Impact Matrix")
        fig_heatmap = px.imshow(
            association_matrix,
            labels=dict(x="Financial Indicator", y="Macro Event", color="Impact Magnitude"),
            x=association_matrix.columns,
            y=association_matrix.index,
            color_continuous_scale="Viridis",
            aspect="auto"
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
    with col_b:
        st.subheader("📋 Policy Event Log")
        st.dataframe(events_data, use_container_width=True)

# --- PAGE 4: SCENARIO PROJECTIONS ---
elif page == "Scenario Projections (2025-2027)":
    st.title("🎯 Financial Inclusion Scenario Projections (2025–2027)")
    st.markdown("Compare baseline trajectories against optimistic (accelerated e-KYC) and pessimistic (high account overlap) models.")
    
    fig_proj = go.Figure()
    fig_proj.add_trace(go.Scatter(x=findex_data["Year"], y=findex_data["Account_Ownership"], mode='lines+markers', name='Historical Data', line=dict(color='black', width=2)))
    fig_proj.add_trace(go.Scatter(x=forecast_data["Year"], y=forecast_data["Base_Account"], mode='lines+markers', name='Base Case', line=dict(color='blue', dash='dash')))
    fig_proj.add_trace(go.Scatter(x=forecast_data["Year"], y=forecast_data["Optimistic_Account"], mode='lines+markers', name='Optimistic Scenario', line=dict(color='green', dash='dot')))
    fig_proj.add_trace(go.Scatter(x=forecast_data["Year"], y=forecast_data["Pessimistic_Account"], mode='lines+markers', name='Pessimistic Scenario', line=dict(color='red', dash='dot')))
    fig_proj.add_hline(y=60.0, line_dash="dash", line_color="orange", annotation_text="60% Target Benchmark")
    
    fig_proj.update_layout(xaxis_title="Year", yaxis_title="Account Ownership Rate (%)", hovermode="x unified")
    st.plotly_chart(fig_proj, use_container_width=True)
    
    st.subheader("📄 Model Output Summary Table")
    st.dataframe(forecast_data, use_container_width=True)