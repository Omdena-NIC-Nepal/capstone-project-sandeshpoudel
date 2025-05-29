# Nepal Climate Impact Monitoring - Streamlit App Template

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# --- App Configuration ---
st.set_page_config(page_title="Nepal Climate Dashboard", layout="wide")
st.title("🇳🇵 Climate Change Impact Monitoring Dashboard")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("final_features.csv")
    return df

df = load_data()

# Optional: Print column names for debugging
# st.write("Columns:", df.columns.tolist())

# --- Sidebar Filters ---
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Year Range",
    int(df['Year'].min()), int(df['Year'].max()),
    (int(df['Year'].min()), int(df['Year'].max()))
)
df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# --- Tabs ---
tabs = st.tabs(["📊 Overview", "📈 Modeling", "💬 Sentiment", "📥 Data"])

# 📊 Overview Tab
with tabs[0]:
    st.subheader("Climate & Economic Impact Overview")
    cols = st.columns(3)

    if 'scaled_total_tc_loss' in df.columns:
        cols[0].metric("Avg. TC Loss", f"{df_filtered['scaled_total_tc_loss'].mean():.2f}")
    else:
        cols[0].metric("Avg. TC Loss", "N/A")

    if 'scaled_Precipitation' in df.columns:
        cols[1].metric("Avg. Precipitation", f"{df_filtered['scaled_Precipitation'].mean():.2f}")
    else:
        cols[1].metric("Avg. Precipitation", "N/A")

    if 'Sentiment_Score' in df.columns:
        cols[2].metric("Avg. Sentiment", f"{df_filtered['Sentiment_Score'].mean():.2f}")
    else:
        cols[2].metric("Avg. Sentiment", "N/A")

    # Chart
    if 'scaled_total_tc_loss' in df_filtered.columns:
        fig = px.line(df_filtered, x='Year', y='scaled_total_tc_loss', title="Tropical Cyclone Loss Over Time (Scaled)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Column 'scaled_total_tc_loss' not found for plotting.")

# 📈 Modeling Tab
# Modeling Tab
with tabs[1]:
    st.subheader("Gradient Boosting Regression")

    if 'Sentiment_Score' in df.columns:
        features = ['scaled_tc_loss_lag1', 'scaled_Precipitation', 'Sentiment_Score']
    else:
        features = ['scaled_tc_loss_lag1', 'scaled_Precipitation']

    # Include 'Year' so we can use it later in visualization
    model_data = df_filtered[features + ['scaled_total_tc_loss', 'Year']].dropna()
    X = model_data[features]
    y = model_data['scaled_total_tc_loss']

    if len(X) > 5:
        model = GradientBoostingRegressor()
        model.fit(X, y)
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)

        st.write(f"**Model MSE:** {mse:.3f}")
        st.write(f"**R-squared (R²):** {r2:.3f}")

        pred_df = model_data[['Year']].copy()
        pred_df['Prediction'] = y_pred

        fig = px.line(pred_df, x='Year', y='Prediction', title="Model Prediction vs. Year")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Not enough data points to train the model.")

# 💬 Sentiment Tab
with tabs[2]:
    if 'Sentiment_Score' in df.columns:
        st.subheader("Sentiment Analysis Trends")
        fig = px.line(df_filtered, x='Year', y='Sentiment_Score', title="Sentiment Score Over Time")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Sentiment scores not available in current dataset.")

# 📥 Data Tab
with tabs[3]:
    st.subheader("Preview & Download Dataset")
    st.dataframe(df_filtered)
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button("Download Filtered Data as CSV", csv, "climate_filtered_data.csv", "text/csv")
