**Date:** July 2026  
**Target Audience:** Consortium Stakeholders (Development Finance Institutions, Mobile Money Operators, National Bank of Ethiopia)

---

## Executive Summary

Ethiopia is undergoing a fundamental shift in its financial architecture. Interoperable peer-to-peer (P2P) digital transfers have officially surpassed traditional ATM cash withdrawals. However, according to the 2024 Global Findex survey, formal account ownership stands at **49%**—a modest 3 percentage point increase from 2021. 

This report presents a comprehensive forecasting model evaluating how product launches, policy interventions, and national digital infrastructure investments (such as the Fayda Digital ID) will influence financial **Access** (Account Ownership) and **Usage** (Digital Payment Adoption) through 2027.

---

## 1. Data Schema & Enrichment Strategy

To overcome the challenges of sparse survey data (only 5 Global Findex data points over 13 years), we utilized a unified dataset schema consisting of:
* **Observations (30 records):** Demand-side survey data and supply-side institutional indicators.
* **Events (10 records):** Policy shifts, license issuances, and product rollouts.
* **Impact Links (14 records):** Modeled lead-lag relationships connecting macro market interventions to inclusion metrics.

### Key Enriched Data Points
1. **Telebirr Base Expansion:** Scaled to over 54M users by 2025.
2. **M-Pesa Growth:** Reached over 10M active users post-2023 market entry.
3. **Fayda Digital ID Rollout:** Projected enrollment scaling past 80M citizens by 2027, significantly lowering KYC barriers for rural onboarding.

---

## 2. Key Exploratory Data Analysis (EDA) Findings

### Finding 1: The 2021–2024 Account Ownership Plateau
Account ownership grew from 14% (2011) to 46% (2021), before slowing down dramatically to 49% in 2024. While mobile money registration surged, account overlap (users owning multiple wallets) and limited transition from pure payments to savings/credit created a bottleneck.

### Finding 2: The P2P vs. Cash Withdrawal Crossover
The volume of digital P2P transactions processed via EthSwitch exceeded physical ATM withdrawals for the first time in 2024 (1.42x ratio), signaling that digital money is increasingly being used for direct commerce rather than mere cash-out operations.

---

## 3. Event Impact Modeling Methodology

Interventions were modeled using an **Association Matrix** that maps event categories to target indicators with calibrated lag effects:
$$\text{Indicator}_{t} = \text{Baseline Trend}_{t} + \sum_{i} \text{Impact}_{i} \times f(t - \text{Lag}_{i})$$

* **Telebirr Launch (2021):** Immediate short-term surge in digital payment adoption (+8.5 pp impact over 24 months).
* **Fayda Digital ID Integration (2024–2027):** Long-term sustained reduction in onboarding friction (+0.25 pp growth rate boost per 10M enrollments).

---

## 4. Financial Inclusion Forecasts (2025–2027)

### Account Ownership Rate Projections (%)

| Year | Pessimistic Scenario | **Base Case** | Optimistic Scenario |
| :--- | :---: | :---: | :---: |
| **2025** | 58.20% | **61.14%** | 63.50% |
| **2026** | 60.50% | **64.70%** | 68.20% |
| **2027** | 62.80% | **68.26%** | 73.10% |

> **Key Milestone:** Under the Base Case scenario, Ethiopia will cross the National Financial Inclusion Strategy (NFIS-II) goal of **60% account ownership during 2025**.

---

## 5. Strategic Recommendations for Stakeholders

1. **National Bank of Ethiopia (NBE):** Leverage Fayda ID e-KYC protocols to streamline tiered account creation for informal and rural populations.
2. **Mobile Money Operators (Telebirr & M-Pesa):** Shift strategy from account registration to **deep usage products** (micro-loans, savings, and merchant payments).
3. **Development Finance Institutions:** Focus investments on rural 4G network coverage and digital literacy initiatives to address the widening urban-rural inclusion gap.

---

## 6. Interactive Dashboard & Screenshots

The accompanying interactive Streamlit application (`dashboard/app.py`) enables real-