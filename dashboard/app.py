import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecaster",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PATH SETUP & DATA LOADING ---
@st.cache_data
def load_data():
    # Historical Findex Benchmarks
    findex_df = pd.DataFrame({
        "Year": [2011, 2014, 2017, 2021, 2024],
        "Account_Ownership": [14.0, 22.0, 35.0, 46.0, 49.0],
        "Digital_Payments": [1.0, 3.0, 12.0, 35.0, 44.0],
        "Mobile_Money": [0.0, 0.1, 0.3, 4.7, 9.45]
    })
    
    # Forecast Data (2025-2027) based on Task 4 Models
    forecast_df = pd.DataFrame({
        "Year": [2025, 2026, 2027],
        "Base_Account": [61.14, 64.70, 68.26],
        "Optimistic_Account": [63.50, 68.20, 73.10],
        "Pessimistic_Account": [58.20, 60.50, 62.80],
        "Digital_Payments": [48.5, 54.2, 60.1],
        "Fayda_Enrollment": [42333333, 64500000, 86666667]
    })
    
    # Event Log
    events_df = pd.DataFrame([
        {"Year": 2021, "Event": "Telebirr Launch", "Category": "Product Launch", "Impact": "High Mobile Money Onboarding"},
        {"Year": 2022, "Event": "Safaricom Entry", "Category": "Infrastructure", "Impact": "Market Competition"},
        {"Year": 2023, "Event": "M-Pesa Launch", "Category": "Product Launch", "Impact": "Interoperability Growth"},
        {"Year": 2024, "Event": "EthSwitch P2P Growth", "Category": "Infrastructure", "Impact": "P2P > ATM Crossover"}
    ])
    
    return findex_df, forecast_df, events_df

findex_data, forecast_data, events_data = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to Section:", [
    "1. Overview", 
    "2. Historical Trends", 
    "3. Event Timeline & Impact", 
    "4. Inclusion Projections (2025-2027)"
])

st.sidebar.markdown("---")
st.sidebar.caption(" Selam Analytics | Consortium Forecasting System")

# ==========================================
# PAGE 1: OVERVIEW
# ==========================================
if page == "1. Overview":
    st.title("📈 Ethiopia Financial Inclusion Forecasting System")
    st.markdown("A data-driven analytics suite tracking Ethiopia's digital financial transformation, mobile money expansion, and target projections toward the National Financial Inclusion Strategy (NFIS).")
    
    # Top Metrics Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("2024 Account Ownership", "49.0%", "+3.0 pp vs 2021")
    with col2:
        st.metric("2027 Projected Ownership", "68.26%", "+19.26 pp (Base)")
    with col3:
        st.metric("P2P / ATM Crossover", "1.42x", "P2P Surpassed Cash")
    with col4:
        st.metric("Target NFIS-II Benchmark", "60.0%", "Achievable by 2025")
        
    st.markdown("---")
    
    # Consortium Key Questions Section
    st.subheader("💡 Key Stakeholder Consortium Insights")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**What drives inclusion in Ethiopia?**\n\nDigital wallet onboarding (Telebirr/M-Pesa), interoperable P2P transfers via EthSwitch, and national identity integration (Fayda) act as the strongest accelerants.")
    with c2:
        st.warning("**Why did account growth slow to +3pp in 2024?**\n\nDespite 65M+ mobile accounts, high account overlap (users owning multiple wallets) and low transition from digital payments to formal bank savings caused structural stagnation.")

# ==========================================
# PAGE 2: HISTORICAL TRENDS
# ==========================================
elif page == "2. Historical Trends":
    st.title("📊 Historical Findex Trends & Channel Analysis")
    st.markdown("Explore demand-side survey indicators from Global Findex (2011–2024).")
    
    # Interactive Metric Selection
    selected_metrics = st.multiselect(
        "Select Metrics to Display:",
        ["Account_Ownership", "Digital_Payments", "Mobile_Money"],
        default=["Account_Ownership", "Digital_Payments"]
    )
    
    # Plotly Time Series Plot
    fig = go.Figure()
    for metric in selected_metrics:
        fig.add_trace(go.Scatter(
            x=findex_data["Year"], 
            y=findex_data[metric],
            mode='lines+markers',
            name=metric.replace("_", " "),
            line=dict(width=3)
        ))
        
    fig.update_layout(
        title="Historical Inclusion Metrics (2011 - 2024)",
        xaxis_title="Survey Year",
        yaxis_title="Adult Population Share (%)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Data Download Section
    st.download_button(
        label="📥 Download Findex Data CSV",
        data=findex_data.to_csv(index=False),
        file_name="ethiopia_findex_historical.csv",
        mime="text/csv"
    )

# ==========================================
# PAGE 3: EVENT TIMELINE & IMPACT
# ==========================================
elif page == "3. Event Timeline & Impact":
    st.title("🚀 Macro Events & Policy Intervention Overlay")
    st.markdown("Analyzing how major product launches, infrastructure developments, and policies correlate with adoption.")
    
    fig_event = px.line(findex_data, x="Year", y="Account_Ownership", title="Account Ownership Overlayed with Market Events", markers=True)
    
    # Add vertical event markers
    for _, row in events_data.iterrows():
        fig_event.add_vline(
            x=row["Year"], 
            line_dash="dash", 
            line_color="red",
            annotation_text=row["Event"],
            annotation_position="top left"
        )
        
    fig_event.update_layout(yaxis_title="Account Ownership (%)")
    st.plotly_chart(fig_event, use_container_width=True)
    
    # Display Event Data Table
    st.subheader("Cataloged Market Interventions")
    st.dataframe(events_data, use_container_width=True)

# ==========================================
# PAGE 4: INCLUSION PROJECTIONS (2025-2027)
# ==========================================
elif page == "4. Inclusion Projections (2025-2027)":
    st.title("🎯 Financial Inclusion Forecasts & Scenarios (2025–2027)")
    st.markdown("Predictive forecasts combining trend regression and event-augmented intervention modeling.")
    
    # Interactive Scenario Selector
    scenario = st.selectbox(
        "Select Forecasting Scenario:",
        ["Base Case", "Optimistic (Accelerated Fayda)", "Pessimistic (Stagnation)"]
    )
    
    # Dynamic Scenario Mapping
    if scenario == "Base Case":
        y_vals = forecast_data["Base_Account"]
        color = "blue"
    elif scenario == "Optimistic (Accelerated Fayda)":
        y_vals = forecast_data["Optimistic_Account"]
        color = "green"
    else:
        y_vals = forecast_data["Pessimistic_Account"]
        color = "red"
        
    # Forecast Plot with Confidence Bounds
    fig_fc = go.Figure()
    
    # Historical Line
    fig_fc.add_trace(go.Scatter(x=findex_data["Year"], y=findex_data["Account_Ownership"], name="Historical Data", line=dict(color="black", width=3)))
    
    # Forecast Line
    fig_fc.add_trace(go.Scatter(x=forecast_data["Year"], y=y_vals, name=f"Forecast ({scenario})", line=dict(color=color, width=3, dash='dash')))
    
    # 60% National Policy Goal Line
    fig_fc.add_hline(y=60.0, line_dash="dot", line_color="orange", annotation_text="60% National Policy Target")
    
    fig_fc.update_layout(
        title=f"Account Ownership Projection: {scenario}",
        xaxis_title="Year",
        yaxis_title="Account Ownership Rate (%)",
        hovermode="x unified"
    )
    st.plotly_chart(fig_fc, use_container_width=True)
    
    # Projections Summary Table
    st.subheader("📋 Forecasted Metrics Table")
    st.dataframe(forecast_data[["Year", "Base_Account", "Digital_Payments", "Fayda_Enrollment"]], use_container_width=True)