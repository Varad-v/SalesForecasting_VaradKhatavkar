import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="Anomaly Report", layout="wide")

st.title("🚨 Sales Anomaly Report")
st.markdown("Isolation Forest identifies unusual sales observations.")

# ------------------------------------------------
# Load Data
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y"
)
    return df

df = load_data()

# ------------------------------------------------
# Monthly Sales
# ------------------------------------------------
monthly = (
    df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
      .sum()
      .reset_index()
)

# ------------------------------------------------
# Isolation Forest
# ------------------------------------------------
model = IsolationForest(
    contamination=0.08,
    random_state=42
)

monthly["Anomaly"] = model.fit_predict(monthly[["Sales"]])

monthly["Status"] = monthly["Anomaly"].map({
    1: "Normal",
   -1: "Anomaly"
})

# ------------------------------------------------
# KPIs
# ------------------------------------------------
total = len(monthly)
anomalies = (monthly["Status"] == "Anomaly").sum()
normal = total - anomalies
percent = (anomalies / total) * 100

c1, c2, c3, c4 = st.columns(4)

c1.metric("Months Analysed", total)
c2.metric("Anomalies", anomalies)
c3.metric("Normal Months", normal)
c4.metric("Anomaly Rate", f"{percent:.1f}%")

st.divider()

# ------------------------------------------------
# Time Series
# ------------------------------------------------
fig = px.line(
    monthly,
    x="Order Date",
    y="Sales",
    title="Monthly Sales"
)

fig.add_scatter(
    x=monthly[monthly["Status"]=="Anomaly"]["Order Date"],
    y=monthly[monthly["Status"]=="Anomaly"]["Sales"],
    mode="markers",
    marker=dict(size=12, color="red"),
    name="Anomaly"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------
# Scatter Plot
# ------------------------------------------------
fig2 = px.scatter(
    monthly,
    x="Order Date",
    y="Sales",
    color="Status",
    size="Sales",
    title="Detected Anomalies"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------
# Monthly Sales Distribution
# ------------------------------------------------
fig3 = px.box(
    monthly,
    y="Sales",
    points="all",
    title="Monthly Sales Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------
# Anomaly Table
# ------------------------------------------------
st.subheader("Detected Anomalies")

anomaly_df = monthly[monthly["Status"] == "Anomaly"]

st.dataframe(
    anomaly_df,
    use_container_width=True
)

# ------------------------------------------------
# Download
# ------------------------------------------------
csv = anomaly_df.to_csv(index=False).encode()

st.download_button(
    "⬇ Download Anomaly Report",
    csv,
    "anomaly_report.csv",
    "text/csv"
)