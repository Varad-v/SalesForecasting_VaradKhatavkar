import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="Forecast Explorer", layout="wide")

st.title("📈 Forecast Explorer")
st.markdown("Sales Forecast using Linear Regression Trend Projection")

# ------------------------
# Load Data
# ------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin1")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d/%m/%Y"
    )

    return df

df = load_data()

# ------------------------
# Monthly Sales
# ------------------------
monthly = (
    df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
      .sum()
      .reset_index()
)

monthly["Month_Num"] = np.arange(len(monthly))

# ------------------------
# Train Trend Model
# ------------------------
X = monthly[["Month_Num"]]
y = monthly["Sales"]

model = LinearRegression()
model.fit(X, y)

monthly["Predicted"] = model.predict(X)

# ------------------------
# Future Forecast
# ------------------------
months = st.slider(
    "Forecast Months",
    min_value=3,
    max_value=24,
    value=12
)

future_x = np.arange(
    len(monthly),
    len(monthly)+months
).reshape(-1,1)

future_pred = model.predict(future_x)

future_dates = pd.date_range(
    monthly["Order Date"].max()+pd.offsets.MonthEnd(),
    periods=months,
    freq="ME"
)

future = pd.DataFrame({
    "Order Date":future_dates,
    "Forecast":future_pred
})

# ------------------------
# KPIs
# ------------------------
c1,c2,c3=st.columns(3)

c1.metric(
    "Current Monthly Avg",
    f"${monthly['Sales'].mean():,.0f}"
)

c2.metric(
    "Forecast Avg",
    f"${future['Forecast'].mean():,.0f}"
)

growth=((future["Forecast"].mean()-monthly["Sales"].mean())
         /monthly["Sales"].mean())*100

c3.metric(
    "Projected Growth",
    f"{growth:.2f}%"
)

st.divider()

# ------------------------
# Actual vs Trend
# ------------------------
fig=px.line(
    monthly,
    x="Order Date",
    y=["Sales","Predicted"],
    title="Historical Sales vs Trend"
)

st.plotly_chart(fig,use_container_width=True)

# ------------------------
# Future Forecast
# ------------------------
fig2=px.line(
    future,
    x="Order Date",
    y="Forecast",
    markers=True,
    title="Future Sales Forecast"
)

st.plotly_chart(fig2,use_container_width=True)

# ------------------------
# Forecast Table
# ------------------------
st.subheader("Forecast Values")

st.dataframe(
    future.style.format({
        "Forecast":"${:,.2f}"
    }),
    use_container_width=True
)

csv=future.to_csv(index=False).encode()

st.download_button(
    "⬇ Download Forecast",
    csv,
    "forecast.csv",
    "text/csv"
)