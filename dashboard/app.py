# Command to run:
# cd c:/Users/cy185005/portableapps/PortableGit/bin/my-digital-life-dashboard
# streamlit run dashboard/app.py

import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

st.set_page_config(page_title="My Digital Life Dashboard", layout="wide")

st.title("📊 My Digital Life Dashboard")

# Sample data loading from DuckDB or CSV
@st.cache_data()
def load_data():
    try:
        con = duckdb.connect(database="./db/life_data.duckdb", read_only=True)
        df = con.execute("SELECT * FROM digital_activity").fetch_df()
    except:
        df = pd.read_csv("./data/sample_activity.csv") # Fallback sample
    return df

df = load_data()

# Sidebar filters
activity_types = st.sidebar.multiselect("Filter by Activity Type", df["activity_type"].unique(), default=df["activity_type"].unique())

filtered_df = df[df["activity_type"].isin(activity_types)]

# Show KPIs

st.subheader("📈 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("First Activity", filtered_df["timestamp"].min())
col3.metric("Last Activity", filtered_df["timestamp"].max())

# Time Series Chart

st.subheader("🕒 Activity Over Time")
time_chart = px.histogram(filtered_df, x="timestamp", color="activity_type", nbins=30)
st.plotly_chart(time_chart, use_container_width=True)

# Activity Breakdown

st.subheader("📌 Activity Breakdown")
breakdown = filtered_df["activity_type"].value_counts().reset_index()
breakdown.columns = ["Activity Type", "Count"]
st.dataframe(breakdown)