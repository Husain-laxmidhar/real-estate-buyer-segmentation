
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- 1. Page Configuration & Custom CSS ---
st.set_page_config(page_title="Parcl | Market Intelligence", page_icon="🏢", layout="wide")

# Custom CSS to hide the default Streamlit menu, footer, and style the metrics
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Styling for KPI Metric Cards */
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Custom Title Styling */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        color: #1a2b49;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 18px;
        color: #6c757d;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. Header Section ---
st.markdown('<p class="main-title">🏢 Parcl Co. Limited</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-Driven Real Estate Buyer Segmentation & Market Intelligence</p>', unsafe_allow_html=True)

# --- 3. Data Loading ---
@st.cache_data
def load_data():
    # Assuming the file is in the same directory
    df = pd.read_csv('segmented_market_intelligence.csv')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("⚠️ Data file 'segmented_market_intelligence.csv' not found. Please ensure your Jupyter Notebook ran successfully and the file is in the same folder as this app.")
    st.stop()

# --- 4. Sidebar Global Filters ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2942/2942206.png", width=60) # Placeholder generic building icon
    st.title("Control Panel")
    st.markdown("Use the filters below to slice the market data.")
    
    selected_segment = st.multiselect("Buyer Persona", options=df['Buyer_Segment'].unique(), default=df['Buyer_Segment'].unique())
    selected_country = st.multiselect("Country of Origin", options=df['country'].unique(), default=df['country'].unique())
    selected_purpose = st.multiselect("Acquisition Purpose", options=df['acquisition_purpose'].unique(), default=df['acquisition_purpose'].unique())
    
    st.markdown("---")
    st.caption("Model: K-Means Clustering (k=4)")
    st.caption("Status: Live Data Sync")

# Apply Filters
df_filtered = df[
    (df['Buyer_Segment'].isin(selected_segment)) &
    (df['country'].isin(selected_country)) &
    (df['acquisition_purpose'].isin(selected_purpose))
]

# --- 5. Executive KPI Dashboard ---
# Using standard columns to create a clean, spaced-out metric row
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(label="Total Analyzed Profiles", value=f"{len(df_filtered):,}")
with kpi2:
    st.metric(label="Portfolio Capital (AUM)", value=f"${df_filtered['total_investment'].sum():,.0f}")
with kpi3:
    st.metric(label="Total Assets Transacted", value=f"{df_filtered['units_purchased'].sum():,}")
with kpi4:
    st.metric(label="Avg. Client Satisfaction", value=f"{df_filtered['satisfaction_score'].mean():.1f} / 5.0")

st.markdown("<br>", unsafe_allow_html=True)

# --- 6. Core Visualizations ---
# Chart styling configuration for a clean, corporate look
chart_config = {'displayModeBar': False} # Hides the plotly toolbar for a cleaner look
custom_template = "plotly_white"

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### 📊 Persona Market Share")
    # Clean donut chart instead of standard bar chart
    fig_share = px.pie(df_filtered, names='Buyer_Segment', hole=0.4,
                       color='Buyer_Segment',
                       color_discrete_sequence=px.colors.sequential.Teal)
    fig_share.update_layout(template=custom_template, margin=dict(t=20, b=20, l=0, r=0), 
                            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5))
    st.plotly_chart(fig_share, use_container_width=True, config=chart_config)

with col2:
    st.markdown("##### 💰 Capital Exposure by Segment")
    # Refined box plot
    fig_box = px.box(df_filtered, x='Buyer_Segment', y='total_investment', color='Buyer_Segment',
                     color_discrete_sequence=px.colors.sequential.Teal)
    fig_box.update_layout(template=custom_template, showlegend=False, xaxis_title="", yaxis_title="Total Spend ($)",
                          margin=dict(t=20, b=20, l=0, r=0))
    st.plotly_chart(fig_box, use_container_width=True, config=chart_config)


st.markdown("<br>", unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.markdown("##### 🌍 Regional Concentration")
    # Stacked bar chart for better territory visualization
    fig_geo = px.histogram(df_filtered, x='region', color='Buyer_Segment', barmode='stack',
                           color_discrete_sequence=px.colors.sequential.Burg)
    fig_geo.update_layout(template=custom_template, xaxis_title="Geographic Region", yaxis_title="Client Count",
                          margin=dict(t=20, b=20, l=0, r=0),
                          legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
                          legend_title_text="")
    st.plotly_chart(fig_geo, use_container_width=True, config=chart_config)

with col4:
    st.markdown("##### 📈 Demographics & Financing Matrix")
    # Clean scatter with opacity to handle overlapping data points
    fig_scatter = px.scatter(df_filtered, x='Age', y='total_investment', color='Buyer_Segment',
                             size='units_purchased', opacity=0.7,
                             hover_data=['loan_applied', 'country'],
                             color_discrete_sequence=px.colors.sequential.Teal)
    fig_scatter.update_layout(template=custom_template, xaxis_title="Chronological Age", yaxis_title="Total Investment ($)",
                              margin=dict(t=20, b=20, l=0, r=0), showlegend=False)
    st.plotly_chart(fig_scatter, use_container_width=True, config=chart_config)

# --- 7. Granular Data Table (Hidden in an Expander) ---
st.markdown("---")
# Using an expander keeps the UI clean but allows users to see the raw data if they want to
with st.expander("🔍 View Raw Segmented Customer Database"):
    st.dataframe(df_filtered[['client_id', 'client_type', 'Age', 'country', 'region', 'Buyer_Segment', 'total_investment', 'units_purchased', 'loan_applied']], use_container_width=True)