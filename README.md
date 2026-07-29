# Ethiopia Financial Inclusion Forecasting & Event Impact Analysis

![Python Version](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An end-to-end data science and scenario modeling framework designed to analyze historical financial inclusion trends in Ethiopia (2011–2024), quantify the impact of macro interventions (e.g., Telebirr, Safaricom, Fayda ID), and project national account ownership trajectory (2025–2027).
## 🎯 Business Problem & Context
Despite rapid digital finance growth in Ethiopia, overall formal bank account ownership grew by only 3 percentage points between 2021 and 2024 (reaching 49%). Financial institutions, policy regulators, and development funds need transparent, data-driven frameworks to:
1. **Quantify Event Impact:** Measure how specific product launches and digital identity infrastructure affect formal account adoption and payment usage.
2. **Evaluate National Targets:** Forecast whether Ethiopia will achieve its **National Financial Inclusion Strategy (NFIS-II) goal of 60% account ownership** by 2027 under varying market scenarios.

---

## 🛠️ Key Results & Findings
* **Task 3 (Event Impact Analysis):** Mobile money launches (Telebirr, M-Pesa) demonstrate immediate high-velocity impact on mobile account creation (+12 to +15 pp boost), whereas core infrastructure rollouts (Fayda ID) serve as long-term adoption catalysts across formal bank channels.
* **Task 4 (Scenario Projections):** 
  * **Base Case:** Account ownership crosses the **60% NFIS-II target during 2025**, reaching **68.26% by 2027**.
  * **Optimistic Scenario (Accelerated e-KYC):** Reaches **73.10% by 2027**.
  * **Pessimistic Scenario (Low Conversion / Stagnation):** Reaches **62.80% by 2027**.

---

## 💻 Repository Structure
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml          # GitHub Actions CI pipeline
├── data/
│   ├── processed/             # Exported model outputs (forecasts_2025_2027.csv)
│   └── raw/                   # Historical Findex & macro event datasets
├── dashboard/
│   └── app.py                 # Interactive Streamlit dashboard
├── notebooks/
│   ├── task3_event_impact_modeling.ipynb
│   └── task4_Forecasting.ipynb
├── reports/
│   ├── final_report.md
│   └── slides_presentation.pdf
├── src/                       # Modularized Python package
│   ├── init.py
│   ├── forecasting.py         # Scenario forecasting & artifact exporter
│   └── impact_model.py        # Binary decoding & association matrix builder
├── tests/
│   └── test_modeling.py       # Pytest unit testing suite
├── README.md
└── requirements.txt


---

## 🚀 Quick Start & Installation

```bash
# 1. Clone Repository
git clone [https://github.com/YOUR_USERNAME/ethiopia-fi-forecast.git](https://github.com/Yas614/ethiopia-fi-forecast.git)
cd ethiopia-fi-forecast

# 2. Activate Virtual Environment & Install Dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Run Automated Tests
pytest

# 4. Launch Interactive Streamlit Dashboard
streamlit run dashboard/app.py