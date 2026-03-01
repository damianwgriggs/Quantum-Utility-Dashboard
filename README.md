# 🌌 Quantum Utility Dashboard

The Quantum Utility Dashboard is a standalone Python application built using `Streamlit` and IBM's `Qiskit Runtime`.

It allows enterprises and researchers to instantly map complex business constraints (e.g., Freight Logistics, Inventory Optimization, and Credit Risk) to a Quantum Approximate Optimization Algorithm (QAOA) solving pipeline—connecting directly to real IBM Quantum hardware or running locally on a simulated backend.

## ✨ Key Features
- **Local Analytics**: Complete data generation and analysis pipelines executing on your local machine.
- **Actionable Quantum Manifests**: Every execution calculates a comparative efficiency score (Quantum QAOA vs. Classical Greedy baseline) using high-complexity node mapping (up to **20-30 nodes**). The output is strictly formatted as a downloadable CSV.
- **Data Factory Integration**: Easily generate synthesized local test sets of **30 rows** leveraging live open data via `yfinance`, `requests`, and Open-Meteo.
- **Sparse Graph Optimization**: The backend now implements **Sparse Graph weighting (40% density)** to ensure the classical greedy solver faces realistic local-optima challenges that the quantum algorithm can navigate.

## 🚀 Running the Dashboard Locally (Source)

1. Install Python 3.10+
2. Install the required dependencies: `pip install -r requirements.txt`
3. Launch the dashboard: `streamlit run app.py`

## 📦 Converting to a Windows Executable (.exe)

You can compile this entire dashboard into a portable `.exe` file that users can double-click and run locally, removing the need for them to install Python or configure dependencies.

To build the executable:
1. Ensure you have `pyinstaller` installed: `pip install pyinstaller`
2. Run the included build script: `python build_exe.py`
3. The compilation process takes a few minutes. Once complete, you will find `QuantumDashboard.exe` inside the newly created `dist/` folder.

*Note: Due to Streamlit and Qiskit architecture, the single .exe file may be large (300MB+) and take a moment to unpack when launched.*

## 🛠️ Usage Templates

### 1. Freight Logistics 🚚
- **Problem**: Traveling Salesperson / Max-Cut variation over dynamic distances and traffic weights.
- **Output Export**: Stop Order and Optimized Route Path CSV.

### 2. Inventory Optimization 📦
- **Problem**: Dynamic stock volume provisioning against live forecasted demand and storage cost functions.
- **Output Export**: SKU and Recommended Restock Quantity CSV.

### 3. Credit Risk 💳
- **Problem**: Evaluating applicant arrays across standard deviation debt-ratios against randomized global Forex distributions.
- **Output Export**: Applicant ID and Quantum Risk Score CSV.

## ⚙️ Technical Stack
- **Frontend/UI Engine**: [Streamlit](https://streamlit.io/)
- **Quantum Integration**: `qiskit>=1.0.0`, `qiskit-ibm-runtime`, `qiskit-aer`
- **Analytics & Vis**: `pandas`, `numpy`, `plotly`
- **Live Data**: `requests`, `yfinance`
