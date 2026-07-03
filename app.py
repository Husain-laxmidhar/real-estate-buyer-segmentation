# ==========================================
# STREAMLIT WEB APP: app.py
# ==========================================
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Parcl Buyer Market Intelligence", layout="wide")
st.title("📊 Real Estate Buyer Segmentation & Investment Profiling")
st.markdown("Automated AI-Driven Customer Intelligence Dashboard for Parcl Co. Limited")

# 2. Load the Engine Data
@st.cache_data
def load_data():
    df = pd.read_csv('segmented_market_intelligence.csv')
    return df

df = load_data()

# 3. Sidebar Filtering Module
st.sidebar.header("Filter Analytics Profile")
selected_country = st.sidebar.multiselect("Select Country", options=df['country'].unique(), default=df['country'].unique())
selected_purpose = st.sidebar.multiselect("Acquisition Purpose", options=df['acquisition_purpose'].unique(), default=df['acquisition_purpose'].unique())
selected_segment = st.sidebar.multiselect("Buyer Archetype Segment", options=df['Buyer_Segment'].unique(), default=df['Buyer_Segment'].unique())

# Apply filters
df_filtered = df[
    (df['country'].isin(selected_country)) &
    (df['acquisition_purpose'].isin(selected_purpose)) &
    (df['Buyer_Segment'].isin(selected_segment))
]

# 4. Key Performance Indicator (KPI) Metric Blocks
metric1, metric2, metric3, metric4 = st.columns(4)
with metric1:
    st.metric("Total Customers Evaluated", f"{len(df_filtered)}")
with metric2:
    st.metric("Total Under-Management Portfolio", f"${df_filtered['total_investment'].sum():,.2f}")
with metric3:
    st.metric("Total Units Closed", f"{df_filtered['units_purchased'].sum()}")
with metric4:
    st.metric("Average Customer Satisfaction", f"{df_filtered['satisfaction_score'].mean():.2f} / 5")

st.markdown("---")

# 5. Core Dashboard Visualizations (Side-by-Side Columns)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("1. Volume Distribution of Buyer Segments")
    fig_count = px.histogram(df_filtered, x='Buyer_Segment', color='Buyer_Segment',
                             category_orders={"Buyer_Segment": ['Global Investors', 'First-Time Buyers', 'Corporate Buyers', 'Luxury Investors']},
                             title="Total Client Count per Archetype Profile",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_count.update_layout(showlegend=False, xaxis_title="Buyer Persona", yaxis_title="Client Count")
    st.plotly_chart(fig_count, use_container_width=True)

with chart_col2:
    st.subheader("2. Total Capital Investment Scales ($)")
    fig_inv = px.box(df_filtered, x='Buyer_Segment', y='total_investment', color='Buyer_Segment',
                     title="Capital Exposure Ranges Across Segments",
                     color_discrete_sequence=px.colors.qualitative.Set2)
    fig_inv.update_layout(showlegend=False, xaxis_title="Buyer Persona", yaxis_title="Total Investment Amount ($)")
    st.plotly_chart(fig_inv, use_container_width=True)

st.markdown("---")

chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("3. Regional Market Proportions")
    fig_geo = px.histogram(df_filtered, x='region', color='Buyer_Segment', barmode='group',
                           title="Segment Concentrations across Territory Horizons",
                           color_discrete_sequence=px.colors.sequential.Burg)  # <-- Fixed attribute here
    st.plotly_chart(fig_geo, use_container_width=True)

with chart_col4:
    st.subheader("4. Demographics & Financing Matrix")
    fig_scatter = px.scatter(df_filtered, x='Age', y='total_investment', color='Buyer_Segment',
                             size='units_purchased', hover_data=['loan_applied', 'referral_channel'],
                             title="Age vs. Spend Scale Matrix cross-referenced by Unit Counts")
    st.plotly_chart(fig_scatter, use_container_width=True)

# 6. Granular Segment Data Query Module
st.markdown("---")
st.subheader("🔍 Granular Customer Records Explorer")
st.dataframe(df_filtered[['client_id', 'client_type', 'Age', 'country', 'region', 'Buyer_Segment', 'total_investment', 'units_purchased', 'loan_applied']])