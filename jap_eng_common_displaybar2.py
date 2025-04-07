import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Sample Data
np.random.seed(42)

# Get the original dataframe
df = pd.read_csv("jap_eng_common_long.csv")
df.drop_duplicates(subset=["word"], inplace=True) # Gets rid of duplicate words

df["rank_difference"] = df["rank_english"] - df["rank_japanese"]
df["rank_difference_abs"] = np.abs(df["rank_difference"])

# Selection for Ranking Type
ranking_choice = st.selectbox("Choose Ranking Type", ["overall_rank", "rank_english", "rank_japanese", "rank_difference", "rank_difference_abs"])

# Sort Data for Both Orders
df_asc = df.sort_values(by=ranking_choice, ascending=True).head(15).sort_values(by=ranking_choice, ascending=False)
df_desc = df.sort_values(by=ranking_choice, ascending=False).head(15).sort_values(by=ranking_choice, ascending=True)

# Create Side-by-Side Layout
col1, col2 = st.columns(2)

# Left Chart (Ascending Order)
with col1:
    st.subheader("Ascending")
    fig_asc = px.bar(
        df_asc, 
        x=ranking_choice, 
        y="word", 
        orientation="h", 
        text_auto=True,
        color=ranking_choice,
        color_continuous_scale="viridis"
    )
    fig_asc.update_layout(
        xaxis=dict(showticklabels=False),  # Hide x-axis ticks
        yaxis=dict(showticklabels=True))  # Hide y-axis ticks
    st.plotly_chart(fig_asc)

# Right Chart (Descending Order)
with col2:
    st.subheader("Descending")
    fig_desc = px.bar(
        df_desc, 
        x=ranking_choice, 
        y="word", 
        orientation="h", 
        text_auto=True,
        color=ranking_choice,
        color_continuous_scale="viridis"
    )
    fig_desc.update_layout(
        xaxis=dict(showticklabels=False),  # Hide x-axis ticks
        yaxis=dict(showticklabels=True))  # Hide y-axis ticks
    st.plotly_chart(fig_desc)
