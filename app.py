import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="COVID-19 Analytics Dashboard",
    page_icon="🦠",
    layout="wide"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🦠 COVID-19 Analytics Dashboard")
st.write("Interactive COVID-19 data analysis and visualization")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

df = pd.read_csv("covid_data_sample.csv")
df["date"] = pd.to_datetime(df["date"])

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Dashboard Filters")

countries = st.sidebar.multiselect(
    "Select Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

filtered_df = df[df["country"].isin(countries)]

# -------------------------------------------------
# KEY METRICS
# -------------------------------------------------

st.subheader("📊 COVID-19 Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Cases",
        f"{filtered_df['total_cases'].max():,}"
    )

with col2:
    st.metric(
        "Total Deaths",
        f"{filtered_df['total_deaths'].max():,}"
    )

with col3:
    st.metric(
        "New Cases",
        f"{filtered_df['new_cases'].sum():,}"
    )

with col4:
    st.metric(
        "New Deaths",
        f"{filtered_df['new_deaths'].sum():,}"
    )

# -------------------------------------------------
# COUNTRY SUMMARY
# -------------------------------------------------

st.subheader("🌍 Country-wise Summary")

summary = (
    filtered_df
    .groupby("country")[
        ["new_cases", "new_deaths", "total_cases", "total_deaths"]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    summary,
    use_container_width=True
)

# -------------------------------------------------
# NEW CASES CHART
# -------------------------------------------------

st.subheader("📈 Daily New COVID-19 Cases")

fig1, ax1 = plt.subplots(figsize=(10, 5))

for country, group in filtered_df.groupby("country"):
    ax1.plot(
        group["date"],
        group["new_cases"],
        marker="o",
        label=country
    )

ax1.set_xlabel("Date")
ax1.set_ylabel("New Cases")
ax1.set_title("Daily New COVID-19 Cases")
ax1.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig1)

# -------------------------------------------------
# NEW DEATHS CHART
# -------------------------------------------------

st.subheader("💀 Daily New COVID-19 Deaths")

fig2, ax2 = plt.subplots(figsize=(10, 5))

for country, group in filtered_df.groupby("country"):
    ax2.plot(
        group["date"],
        group["new_deaths"],
        marker="o",
        label=country
    )

ax2.set_xlabel("Date")
ax2.set_ylabel("New Deaths")
ax2.set_title("Daily New COVID-19 Deaths")
ax2.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2)

# -------------------------------------------------
# TOTAL CASES CHART
# -------------------------------------------------

st.subheader("📊 Total COVID-19 Cases Over Time")

fig3, ax3 = plt.subplots(figsize=(10, 5))

for country, group in filtered_df.groupby("country"):
    ax3.plot(
        group["date"],
        group["total_cases"],
        marker="o",
        label=country
    )

ax3.set_xlabel("Date")
ax3.set_ylabel("Total Cases")
ax3.set_title("Total COVID-19 Cases Over Time")
ax3.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig3)

# -------------------------------------------------
# TOTAL DEATHS CHART
# -------------------------------------------------

st.subheader("📉 Total COVID-19 Deaths Over Time")

fig4, ax4 = plt.subplots(figsize=(10, 5))

for country, group in filtered_df.groupby("country"):
    ax4.plot(
        group["date"],
        group["total_deaths"],
        marker="o",
        label=country
    )

ax4.set_xlabel("Date")
ax4.set_ylabel("Total Deaths")
ax4.set_title("Total COVID-19 Deaths Over Time")
ax4.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig4)

# -------------------------------------------------
# RAW DATA
# -------------------------------------------------

st.subheader("📋 COVID-19 Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)