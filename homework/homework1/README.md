# Project Title
**Market Microstructure & Volatility Spillovers in Financial Assets**

**Stage:** Problem Framing & Scoping (Stage 01)

---

## Problem Statement
Volatility shocks in one financial asset often spill over into others, especially in highly interconnected markets such as equity indices, volatility derivatives, and cryptocurrencies. Understanding the **direction, magnitude, and timing** of these spillovers is critical for traders, portfolio managers, and risk teams.  
This project seeks to model realized volatility from high-frequency data, estimate cross-asset spillovers using econometric tools (HAR-RV, DCC-GARCH, Diebold–Yilmaz Spillover Index), and track **time-varying contagion patterns**. The ultimate aim is to identify who transmits volatility, who absorbs it, and under what market conditions.

---

## Stakeholder & User
- **Stakeholders:** Quant researchers, traders, portfolio managers, and risk management teams.  
- **Users:**  
  - Traders: adjust hedging and cross-asset exposure.  
  - Researchers: validate market microstructure hypotheses.  
  - Risk teams: identify periods of heightened systemic risk.  
- **Workflow Context:**  
  - Input: high-frequency returns or realized volatility series.  
  - Output: spillover indices, rolling time series plots, and directed network graphs.  
  - Timing: daily/weekly reporting cycles or event-driven analysis.

---

## Useful Answer & Decision
- **Answer Type:** Descriptive + Predictive  
- **Artifacts Delivered:**  
  - Quantified spillover table (TO/FROM/NET).  
  - Rolling spillover index for time-varying dynamics.  
  - Directed network visualization of cross-asset volatility transmission.  
- **Metrics:** Adjusted R² for HAR-RV models, spillover percentages, Granger causality p-values, predictive accuracy for realized volatility.  
- **Decisions Enabled:**  
  - Which asset acts as a volatility leader?  
  - When to expect contagion vs. decoupling across markets?  
  - How to rebalance or hedge portfolios under shifting volatility regimes?

---

## Assumptions & Constraints
- Data availability: Intraday OHLCV (crypto: Binance API; equities/ETFs: Yahoo Finance, WRDS if accessible).  
- Capacity: 2-week project scope with limited computational resources (Python, open-source econometrics libraries).  
- Latency: End-of-day or T+1 reporting; no real-time execution required.  
- Compliance: Use only publicly available or academic-accessible data; no proprietary feeds.  
- Model scope: GARCH-class models, VAR-based spillover indices; no deep learning in Stage 01.

---

## Known Unknowns / Risks
- Data quality: Missing or irregular timestamps in intraday data.  
- Microstructure noise: Bias in realized variance at high frequencies.  
- Model specification: VAR lag order sensitivity, GARCH convergence issues.  
- Interpretation risk: Spillover ≠ causality; need robustness checks (Granger tests, event windows).  
- Generalization: Results may depend heavily on chosen assets and time horizon.

---

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Identify volatility spillover drivers → Problem Framing & Scoping (Stage 01) → README (this file)  
- Collect & clean high-frequency returns → Data Engineering (Stage 02) → Cleaned dataset  
- Estimate realized volatility & baseline models → Modeling (Stage 03) → HAR-RV & GARCH fits  
- Quantify & visualize spillovers → Analysis (Stage 04) → Spillover table, rolling indices, network graph  
- Package reproducible results → Delivery (Stage 05) → Report + repo + figures

---

## Repo Plan
- `/data_raw/`: Raw intraday OHLCV (CSV/Parquet).  
- `/data_clean/`: Processed returns, realized volatility, aligned datasets.  
- `/src/`: Core scripts (`features.py`, `models.py`, `spillovers.py`, `viz.py`).  
- `/notebooks/`: Exploratory analysis, step-by-step experiments.  
- `/docs/`: Method notes, references, figures, writeup drafts.  
- `/reports/`: Final plots, tables, and paper-like summary.  

**Cadence for updates:**  
- Daily commits during 2-week sprint.  
- Stage checkpoints every ~3 days (scoping → data → modeling → analysis → delivery).  
