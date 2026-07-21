# Forecasting Financial Inclusion in Ethiopia (2025–2027)

> **Selam Analytics | Financial Technology Consulting**  
> *A time-series forecasting and policy intervention modeling system tracking Ethiopia's digital financial transformation.*

---

## 📊 Project Overview

This repository builds an end-to-end forecasting framework to track progress on the two primary dimensions of financial inclusion in Ethiopia as defined by the World Bank's Global Findex:
1. **Access:** Account Ownership Rate (% of adults age 15+).
2. **Usage:** Digital Payment Adoption Rate (% of adults sending/receiving digital payments).

By combining historical Global Findex demand-side data, administrative infrastructure data, and macro market events (such as the launch of Telebirr, M-Pesa, EthSwitch P2P interoperability, and Fayda Digital ID enrollment), this system projects progress toward the National Financial Inclusion Strategy (NFIS-II) targets through 2027.

---

## 🏗 Repository Structure

```text
ethiopia-fi-forecast/
├── .github/workflows/         # CI/CD Workflows
│   └── unittests.yml
├── dashboard/                 # Streamlit Interactive Application
│   └── app.py
├── data/
│   ├── processed/             # Cleaned & enriched data
│   └── raw/                   # Unified starter dataset & reference codes
├── notebooks/                 # Sequential Analytical Pipeline
│   ├── task1_data_exploration.ipynb
│   ├── task2_eda.ipynb
│   ├── task3_event_impact_modeling.ipynb
│   └── task4_Forecasting.ipynb
├── reports/                   # Documentation & Submission Reports
│   ├── data_enrichment_log.md
│   ├── interim_report.md
│   └── final_report.md
├── requirements.txt           # Environment Dependencies
└── README.md                  # Project Documentation