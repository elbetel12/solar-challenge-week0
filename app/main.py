import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data(country):
    df = pd.read_csv(f"data/{country.lower()}_clean.csv")
    df["Country"] = country
    return df

# 
st.title("🌞 Solar Energy Insights Dashboard")
st.markdown("Explore and compare solar radiation metrics across countries")

# Country selection
countries = ["Benin", "Sierra_Leone", "Togo"]
selected_countries = st.multiselect("Select countries:", countries, default=countries)

# Load and combine
data = pd.concat([load_data(c) for c in selected_countries])

# Metric selection
metric = st.selectbox("Select metric:", ["GHI", "DNI", "DHI"])

# Boxplot
fig = px.box(data, x="Country", y=metric, color="Country",
             title=f"{metric} Distribution by Country")
st.plotly_chart(fig, use_container_width=True)

# Summary table
st.markdown("### Summary Table")
summary = data.groupby("Country")[metric].agg(["mean", "median", "std"]).reset_index()
st.dataframe(summary)
