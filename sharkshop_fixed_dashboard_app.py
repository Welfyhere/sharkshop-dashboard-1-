
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='SharkShop Insights Dashboard', layout='wide')

@st.cache_data
def load_data():
    df = pd.read_csv('fixed_ecommerce_data_5_years.csv')
    df['Month'] = pd.to_datetime(df['Month'])
    return df

df = load_data()

# Title and logo
st.markdown("""
<div style='display: flex; align-items: center;'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/3/34/Shark_icon.png' width='80'/>
    <h1 style='padding-left: 1rem;'>SharkShop Strategic Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# Key Metrics Summary
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
col2.metric("Avg Monthly Customers", f"{int(df['New_Customers'].mean()):,}")
col3.metric("Lowest CAC", f"${df['Customer_Acquisition_Cost'].min():.2f}")

# Revenue Line Chart
st.subheader("Revenue Trend Over Time")
revenue_chart = alt.Chart(df).mark_line(point=True).encode(
    x='Month:T',
    y='Revenue:Q',
    tooltip=['Month:T', 'Revenue:Q']
).properties(width=900, height=400)
st.altair_chart(revenue_chart, use_container_width=True)

# CAC Trend
st.subheader("Customer Acquisition Cost (CAC) Over Time")
cac_chart = alt.Chart(df).mark_area(opacity=0.5, color='orangered').encode(
    x='Month:T',
    y='Customer_Acquisition_Cost:Q',
    tooltip=['Month:T', 'Customer_Acquisition_Cost:Q']
).properties(width=900, height=300)
st.altair_chart(cac_chart, use_container_width=True)

# Top Product Category Frequency
st.subheader("Top Product Category Frequency")
category_counts = df['Top_Product_Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Months']
bar_chart = alt.Chart(category_counts).mark_bar().encode(
    x='Category:N',
    y='Months:Q',
    color='Category:N',
    tooltip=['Category', 'Months']
).properties(width=900, height=300)
st.altair_chart(bar_chart, use_container_width=True)

# Strategic Takeaway Block
st.subheader("Strategic Observations")
st.markdown("""
- SharkShop has generated **$16.5M** in revenue across 5 years, with strong Q1 performance and a January 2022 peak.
- CAC has improved drastically from ~$75 to <$20, reflecting more efficient marketing efforts.
- Apparel dominates as a recurring top category, suggesting durability and sustained consumer interest.
- Retention is strongest in Electronics and Sports; opportunities exist for deeper loyalty programming.
- Customer acquisition trends upward each summer, offering a prime window for scaling campaigns.
""")
