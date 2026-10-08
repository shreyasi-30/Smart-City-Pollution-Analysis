import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Pollution Analysis", layout="wide")

st.title("Smart City Pollution Analysis using K-Means")
st.write("Upload dataset to analyze pollution levels across cities.")

# Upload file
file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if file:
    # ========================
    # LOAD DATA
    # ========================
    data = pd.read_csv(file)

    st.subheader(" Random Sample Data")
    st.write(data.sample(10))

    # ========================
    # CLEAN DATA
    # ========================
    data = data[['City','Date','PM2.5','PM10','NO2','CO','SO2','AQI']]
    data = data.dropna()

    st.success("Data cleaned successfully")

    # ========================
    # CITY FILTER
    # ========================
    st.subheader(" Filter by City")

    city = st.selectbox("Select a City", data['City'].unique())
    filtered_data = data[data['City'] == city]

    st.write(f"Showing data for: {city}")
    st.write(filtered_data.head(10))

    # ========================
    # TIME GRAPH
    # ========================
    st.subheader(" AQI Trend for Selected City")

    filtered_data = filtered_data.sort_values('Date')
    filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

    st.line_chart(filtered_data.set_index('Date')['AQI'])

    # ========================
    #  K-MEANS CLUSTERING
    # ========================
    X = data[['PM2.5','PM10','NO2','CO','SO2']]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(X_scaled)

    #  FIXED CATEGORY LOGIC
    cluster_avg = data.groupby('Cluster')['AQI'].mean()
    sorted_clusters = cluster_avg.sort_values().index.tolist()

    labels = {
        sorted_clusters[0]: "🟢 Low Pollution",
        sorted_clusters[1]: "🟡 Moderate Pollution",
        sorted_clusters[2]: "🔴 High Pollution"
    }

    data['Category'] = data['Cluster'].map(labels)

    # ========================
    # CLUSTERED DATA
    # ========================
    st.subheader(" Clustered Data (Selected City)")
    st.write(data[data['City'] == city].head(10))

    st.subheader("Random Clustered Data (All Cities)")
    st.write(data.sample(10))

    # ========================
    #  CATEGORY COUNT
    # ========================
    st.subheader(" Pollution Category Count")
    st.write(data['Category'].value_counts())

    # ========================
    # BAR CHART
    # ========================
    st.subheader("Pollution Distribution")
    st.bar_chart(data['Category'].value_counts())

    # ========================
    #  PIE CHART
    # ========================
    st.subheader("Pollution Category Distribution")

    fig1, ax1 = plt.subplots()
    data['Category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
    st.pyplot(fig1)

    # ========================
    # SCATTER PLOT
    # ========================
    st.subheader(" Cluster Visualization")

    fig, ax = plt.subplots()

    colors = ['green', 'orange', 'red']

    for cluster in data['Cluster'].unique():
        cluster_data = data[data['Cluster'] == cluster]
        
        ax.scatter(
            cluster_data['PM2.5'],
            cluster_data['PM10'],
            color=colors[cluster],
            label=labels[cluster],
            alpha=0.6
        )

    centroids = kmeans.cluster_centers_

    ax.scatter(
        centroids[:, 0],
        centroids[:, 1],
        s=200,
        c='black',
        marker='X',
        label='Centroids'
    )

    ax.set_xlabel("PM2.5")
    ax.set_ylabel("PM10")
    ax.legend()

    st.pyplot(fig)

    # ========================
    # TOP POLLUTED CITIES
    # ========================
    st.subheader("Top Polluted Cities")

    city_pollution = data.groupby('City')['AQI'].mean().sort_values(ascending=False)
    st.write(city_pollution.head(10))

    st.success("Analysis Completed Successfully!")