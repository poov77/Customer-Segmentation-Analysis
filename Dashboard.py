import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Customer Segmentation Dashboard")

# Load dataset with proper path handling
try:
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "customer_segments.csv")
    
    # If file not found in script directory, try current working directory
    if not os.path.exists(csv_path):
        csv_path = "customer_segments.csv"
    
    df = pd.read_csv(csv_path)
except FileNotFoundError as e:
    st.error(f"Error loading CSV file: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error reading CSV file: {e}")
    st.stop()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Segment distribution
st.subheader("Customer Segment Distribution")

try:
    segment_count = df["Cluster"].value_counts().reset_index()
    segment_count.columns = ["Cluster", "Customers"]

    fig = px.bar(
        segment_count,
        x="Cluster",
        y="Customers",
        color="Cluster",
        title="Customers per Segment"
    )

    st.plotly_chart(fig)
except Exception as e:
    st.error(f"Error creating segment distribution chart: {e}")

# Recency vs Monetary scatter
st.subheader("Customer Segmentation Scatter")

try:
    fig2 = px.scatter(
        df,
        x="Recency",
        y="Monetary",
        color="Cluster",
        title="Customer Segments"
    )

    st.plotly_chart(fig2)
except Exception as e:
    st.error(f"Error creating scatter chart: {e}")

# Cluster summary
st.subheader("Cluster Summary")

try:
    summary = df.groupby("Cluster")[["Recency","Frequency","Monetary"]].mean()
    st.dataframe(summary)
except Exception as e:
    st.error(f"Error creating cluster summary: {e}")