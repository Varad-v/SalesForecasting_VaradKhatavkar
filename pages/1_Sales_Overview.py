import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Sales Overview", layout="wide")

st.title("📊 Sales Overview Dashboard")
st.markdown("Interactive overview of sales performance across regions, categories, and products.")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin1")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d/%m/%Y"
    )

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

    return df

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

years = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

filtered = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Year"].isin(years))
]

# -----------------------------
# KPI Cards
# -----------------------------
total_sales = filtered["Sales"].sum()
total_orders = filtered["Order ID"].nunique()
customers = filtered["Customer ID"].nunique()
avg_sales = filtered["Sales"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Total Sales", f"${total_sales:,.0f}")
c2.metric("🛒 Orders", f"{total_orders:,}")
c3.metric("👥 Customers", f"{customers:,}")
c4.metric("📦 Avg Order Value", f"${avg_sales:,.2f}")

st.divider()

# -----------------------------
# Monthly Sales Trend
# -----------------------------
monthly = (
    filtered.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month"])
)

fig_month = px.line(
    monthly,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_month, use_container_width=True)

# -----------------------------
# Region & Category Charts
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    region_sales = (
        filtered.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        color="Region",
        title="Sales by Region"
    )

    st.plotly_chart(fig_region, use_container_width=True)

with col2:

    category_sales = (
        filtered.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig_category = px.pie(
        category_sales,
        values="Sales",
        names="Category",
        hole=0.45,
        title="Sales by Category"
    )

    st.plotly_chart(fig_category, use_container_width=True)

# -----------------------------
# Top Products
# -----------------------------
top_products = (
    filtered.groupby("Product Name")["Sales"]
    .sum()
    .nlargest(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig_products, use_container_width=True)

# -----------------------------
# Segment Analysis
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    seg = (
        filtered.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig_seg = px.bar(
        seg,
        x="Segment",
        y="Sales",
        color="Segment",
        title="Sales by Customer Segment"
    )

    st.plotly_chart(fig_seg, use_container_width=True)

with col2:

    state = (
        filtered.groupby("State")["Sales"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig_state = px.bar(
        state,
        x="Sales",
        y="State",
        orientation="h",
        title="Top 10 States by Sales"
    )

    st.plotly_chart(fig_state, use_container_width=True)

# -----------------------------
# Data Preview
# -----------------------------
st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    height=350
)