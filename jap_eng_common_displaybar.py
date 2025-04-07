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

# Selection for Sorting Order
sort_order = st.selectbox("Sort Order", ["Descending", "Ascending"])

# Sort Data Based on Selection
ascending = sort_order == "Ascending"
df_sorted = df.sort_values(by=ranking_choice, ascending=ascending).head(20)

# Bar Chart
fig_bar = px.bar(
    df_sorted,
    x=ranking_choice,
    y="word",
    orientation="h",
    title=f"Top 10 Words ({ranking_choice})",
    text_auto=True,
    color=ranking_choice,
    color_continuous_scale="viridis"
)

fig_bar.update_layout(
    xaxis_title="Ranking",
    yaxis_title="Words",
    transition=dict(duration=500),  # Smooth transition
)

st.plotly_chart(fig_bar)
