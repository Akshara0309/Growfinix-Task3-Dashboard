import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Tour Enquiry Dashboard")

df = pd.read_csv("tour_enquiries.csv")

st.subheader("Dataset")
st.dataframe(df)

# Destination Analysis
st.subheader("Popular Destinations")

destinations = (
    df.groupby("Destination")["Enquiries"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    destinations,
    x="Destination",
    y="Enquiries",
    title="Most Popular Destinations"
)

st.plotly_chart(fig1)

# Monthly Analysis
st.subheader("Monthly Enquiries")

monthly = (
    df.groupby("Month")["Enquiries"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly,
    x="Month",
    y="Enquiries",
    markers=True,
    title="Peak Enquiry Times"
)

st.plotly_chart(fig2)

# State Analysis
st.subheader("State-wise Distribution")

states = (
    df.groupby("State")["Enquiries"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    states,
    names="State",
    values="Enquiries",
    title="Geographic Distribution"
)

st.plotly_chart(fig3)

st.success("Dashboard Loaded Successfully")