import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import numpy as np

df = pd.read_csv("jap_eng_common.csv")

st.write("Here's the head of our merged data:")
st.write(df[["word", "kanji", "reading", "overall_rank", "rank_english", "rank_japanese"]])
words = df["word"].values.tolist()
words = " ".join([word for word in words if words.count(word) >= 2])
wordcloud = WordCloud().generate(words)

# Display the generated image:
fig, ax = plt.subplots()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot(fig)

# Streamlit UI
st.title("Bubble Chart: Top 20 words by rank")

df = df.head(200).copy()
df["BubbleSize"] = max(df["rank_english"]) + 1 - df["rank_english"]
df["X"] = np.random.uniform(0, 100, size=len(df))
df["Y"] = np.random.uniform(0, 100, size=len(df))

# Bubble Chart with Hover
fig_bubble = px.scatter(
    df,
    x="X",
    y="Y",
    size="BubbleSize",  # Bubble size
    color="rank_english",
    hover_name="word",  # Show word on hover
    title="Top 200 Ranked Words (Bubble Size = Importance)",
    color_continuous_scale="viridis",
    size_max=100
)

# Remove axis labels for cleaner look
fig_bubble.update_layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    showlegend=False,
    dragmode="pan" # allows dragging but disables zoom
)

# Display in Streamlit
st.plotly_chart(fig_bubble)

