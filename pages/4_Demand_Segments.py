import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


st.title("📦 Demand Segmentation Dashboard")
st.markdown("K-Means clustering identifies products with similar demand patterns.")

# -------------------------------------------------
# Load Data
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin1")
    return df

df = load_data()

# -------------------------------------------------
# Product Level Summary
# -------------------------------------------------
product = (
    df.groupby("Product Name")
    .agg({
        "Sales": ["sum", "mean", "count"]
    })
)

product.columns = [
    "Total Sales",
    "Average Sales",
    "Orders"
]

product.reset_index(inplace=True)

# -------------------------------------------------
# Scaling
# -------------------------------------------------
features = product[[
    "Total Sales",
    "Average Sales",
    "Orders"
]]

scaler = StandardScaler()
scaled = scaler.fit_transform(features)

# -------------------------------------------------
# KMeans
# -------------------------------------------------
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

product["Cluster"] = kmeans.fit_predict(scaled)

cluster_names = {
    0: "High Demand",
    1: "Medium Demand",
    2: "Low Demand"
}

product["Demand Segment"] = product["Cluster"].map(cluster_names)

# -------------------------------------------------
# PCA
# -------------------------------------------------
pca = PCA(n_components=2)

pcs = pca.fit_transform(scaled)

product["PC1"] = pcs[:,0]
product["PC2"] = pcs[:,1]

# -------------------------------------------------
# KPIs
# -------------------------------------------------
c1,c2,c3,c4 = st.columns(4)

c1.metric("Products", len(product))

c2.metric(
    "High Demand",
    (product["Demand Segment"]=="High Demand").sum()
)

c3.metric(
    "Medium Demand",
    (product["Demand Segment"]=="Medium Demand").sum()
)

c4.metric(
    "Low Demand",
    (product["Demand Segment"]=="Low Demand").sum()
)

st.divider()

# -------------------------------------------------
# PCA Scatter
# -------------------------------------------------
fig = px.scatter(
    product,
    x="PC1",
    y="PC2",
    color="Demand Segment",
    hover_name="Product Name",
    title="Demand Segmentation (PCA Projection)"
)

st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# Cluster Distribution
# -------------------------------------------------
fig2 = px.histogram(
    product,
    x="Demand Segment",
    color="Demand Segment",
    title="Products per Demand Segment"
)

st.plotly_chart(fig2,use_container_width=True)

# -------------------------------------------------
# Average Sales by Cluster
# -------------------------------------------------
cluster_summary = (
    product.groupby("Demand Segment")[
        "Total Sales"
    ]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    cluster_summary,
    x="Demand Segment",
    y="Total Sales",
    color="Demand Segment",
    title="Average Sales by Demand Segment"
)

st.plotly_chart(fig3,use_container_width=True)

# -------------------------------------------------
# Top Products
# -------------------------------------------------
st.subheader("Top Products")

segment = st.selectbox(
    "Select Demand Segment",
    sorted(product["Demand Segment"].unique())
)

table = (
    product[
        product["Demand Segment"]==segment
    ]
    .sort_values(
        "Total Sales",
        ascending=False
    )
)

st.dataframe(
    table,
    use_container_width=True
)

# -------------------------------------------------
# Download
# -------------------------------------------------
csv = product.to_csv(index=False).encode()

st.download_button(
    "⬇ Download Segmentation",
    csv,
    "demand_segments.csv",
    "text/csv"
)
