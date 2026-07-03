# real-estate-buyer-segmentation
An AI-driven buyer segmentation pipeline and interactive Streamlit dashboard for real estate market intelligence, utilizing K-Means clustering and hierarchical validation.

# Real Estate Buyer Segmentation & Investment Profiling

An AI-driven market intelligence solution developed to discover hidden behavioral patterns in real estate transaction history. By clustering data across buyer demographics, financing records, and spending habits, this project replaces generic real estate targeting with highly personalized investor personas.

## 🚀 Project Overview
Treating all real estate buyers the same leads to inefficient marketing spend and poor property recommendations. This project implements a full-stack machine learning pipeline that aggregates raw transactional property logs with core customer profiles, engineers demographic features, and groups buyers into four distinct, highly strategic business segments.

### Key Deliverables:
1. **End-to-End ML Pipeline:** Cleans financial strings, handles missing survey entries via structural data imputation, handles multi-format date records contextually anchored to 2026, and normalizes features using `StandardScaler`.
2. **Cluster Optimization Framework:** Utilizes the Elbow Method (WCSS metrics) and Silhouette Score coefficients, alongside Agglomerative Hierarchical Dendrograms, to mathematically isolate and validate the optimal cluster topology.
3. **Interactive Streamlit Web Dashboard:** A live business intelligence web application containing global KPI metrics blocks, demographic scatter matrices, and regional market proportion distributions powered by Plotly Express.

---

## 📊 Identified Buyer Archetypes
The unsupervised K-Means clustering algorithm maps customers into four actionable personas based on project definitions:
* **Global Investors (C1):** International high-income buyers with steady real estate capital allocations.
* **First-Time Buyers (C2):** Younger demographic tiers heavily dependent on financing/loan application approval.
* **Corporate Buyers (C3):** Institutional entities and companies purchasing multiple commercial or residential units.
* **Luxury Investors (C4):** High-net-worth individuals demonstrating premium capital spend scales paired with peak customer satisfaction ratings.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Environment/Kernel:** Anaconda Jupyter Notebook
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`KMeans`, `StandardScaler`, `ColumnTransformer`)
* **Statistical Tree Analysis:** SciPy (`scipy.cluster.hierarchy`)
* **Web Framework & Interactive Visualizations:** Streamlit, Plotly Express, Seaborn, Matplotlib

---

## 📦 How to Run the App Locally

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/real-estate-buyer-segmentation.git](https://github.com/YOUR_USERNAME/real-estate-buyer-segmentation.git)
   cd real-estate-buyer-segmentation
