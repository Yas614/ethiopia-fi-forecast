import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecaster",
    page_icon="📈",
    layout="wide"
)

# --- DATA GENERATION / LOADING ---
@st.cache_data
def load_data():
    findex_df = pd.DataFrame({
        "Year": [2011, 2014, 2017, 2021, 2024],
        "Account_Ownership": [14.0, 22.0, 35.0, 46.0, 49.0],
        "Digital_Payments": [1.0, 3.0, 12.0, 35.0, 44.0],
        "Mobile_Money": [0.0, 0.1, 0.3, 4.7, 9.45]
    })
    
    forecast_df = pd.DataFrame({
        "Year": [2025, 2026, 2027],
        "Base_Account": [61.14, 64.70, 68.26],
        "Optimistic_Account": [63.50, 68.20, 73.10],
        "Pessimistic_Account": [58.20, 60.50, 62.80],
        "Digital_Payments": [48.5, 54.2, 60.1],
        "Fayda_Enrollment": [42333333, 64500000, 86666667]
    })
    
    events_df = pd.DataFrame([
        {"Year": 2021, "Event": "Telebirr Launch", "Category": "Product Launch", "Impact": "High Mobile Money Onboarding"},
        {"Year": 2022, "Event": "Safaricom Entry", "Category": "Infrastructure", "Impact": "Market Competition"},
        {"Year": 2023, "Event": "M-Pesa Launch", "Category": "Product Launch", "Impact": "Interoperability Growth"},
        {"Year": 2024, "Event": "EthSwitch P2P Growth", "Category": "Infrastructure", "Impact": "P2P > ATM Crossover"}
    ])
    
    return findex_df, forecast_df, events_df

findex_data, forecast_data, events_data = load_data()

# --- SIDEBAR ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to Section:", [
    "1. Overview", 
    "2. Historical Trends", 
    "3. Event Timeline & Impact", 
    "4. Inclusion Projections (2025-2027)"
])

# --- PAGE 1: OVERVIEW ---
if page == "1. Overview":
    st.title("📈 Ethiopia Financial Inclusion Forecasting System")
    st.markdown("A data-driven analytics suite tracking Ethiopia's digital financial transformation.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("2024 Account Ownership", "49.0%", "+3.0 pp vs 2021")
    col2.metric("2027 Projected Ownership", "68.26%", "+19.26 pp (Base)")
    col3.metric("P2P / ATM Crossover", "1.42x", "P2P Surpassed Cash")
    col4.metric("Target NFIS-II Benchmark", "60.0%", "Achievable by 2025")
    
    st.subheader("💡 Key Stakeholder Consortium Insights")
    c1, c2 = st.columns(2)
    c1.info("**What drives inclusion in Ethiopia?**\n\nDigital wallet onboarding (Telebirr/M-Pesa), interoperable P2P transfers via EthSwitch, and national identity integration (Fayda) act as the strongest accelerants.")
    c2.warning("**Why did account growth slow to +3pp in 2024?**\n\nDespite 65M+ mobile accounts, high account overlap and low transition from digital payments to formal bank savings caused structural stagnation.")

# --- PAGE 2: HISTORICAL TRENDS ---
elif page == "2. Historical Trends":
    st.title("📊 Historical Findex Trends & Channel Analysis")
    
    selected_metrics = st.multiselect(
        "Select Metrics to Display:",
        ["Account_Ownership", "Digital_Payments", "Mobile_Money"],
        default=["Account_Ownership", "Digital_Payments"]
    )
    
    fig = go.Figure()
    for metric in selected_metrics:
        fig.add_trace(go.Scatter(
            x=findex_data["Year"], 
            y=findex_data[metric],
            mode='lines+markers',
            name=metric.replace("_", " ")
        ))
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: EVENT TIMELINE ---
elif page == "3. Event Timeline & Impact":
    st.title("🚀 Macro Events & Policy Intervention Overlay")
    fig_event = px.line(findex_data, x="Year", y="Account_Ownership", title="Account Ownership vs Market Events", markers=True)
    st.plotly_chart(fig_event, use_container_width=True)
    st.dataframe(events_data, use_container_width=True)

# --- PAGE 4: PROJECTIONS ---
elif page == "4. Inclusion Projections (2025-2027)":
    st.title("🎯 Financial Inclusion Forecasts (2025–2027)")
    
    scenario = st.selectbox(
        "Select Forecasting Scenario:",
        ["Base Case", "Optimistic", "Pessimistic"]
    )
    
    y_map = {
        "Base Case": forecast_data["Base_Account"],
        "Optimistic": forecast_data["Optimistic_Account"],
        "Pessimistic": forecast_data["Pessimistic_Account"]
    }
    
    fig_fc = go.Figure()
    fig_fc.add_trace(go.Scatter(x=findex_data["Year"], y=findex_data["Account_Ownership"], name="Historical"))
    fig_fc.add_trace(go.Scatter(x=forecast_data["Year"], y=y_map[scenario], name=f"Forecast ({scenario})", line=dict(dash='dash')))
    fig_fc.add_hline(y=60.0, line_dash="dot", line_color="orange", annotation_text="60% Target")
    
    st.plotly_chart(fig_fc, use_container_width=True)
    st.dataframe(forecast_data, use_container_width=True)