import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)

home = st.Page("pages/0_Home.py", title="Home", default=True)
sales = st.Page("pages/1_Sales_Overview.py", title="Sales Overview")
forecast = st.Page("pages/2_Forecast_Explorer.py", title="Forecast Explorer")
anomaly = st.Page("pages/3_Anomaly_Report.py", title="Anomaly Report")
segments = st.Page("pages/4_Demand_Segments.py", title="Demand Segments")

pg = st.navigation([home, sales, forecast, anomaly, segments])

pg.run()