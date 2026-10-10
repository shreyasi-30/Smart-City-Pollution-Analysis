# 🌍 Smart City Pollution Analysis Using K-Means Clustering

## 📌 Project Overview

Smart City Pollution Analysis is a Python-based data analytics and machine learning project designed to analyze air pollution levels across cities. It uses air quality indicators and the **K-Means clustering algorithm** to group pollution observations into three categories: Low Pollution, Moderate Pollution, and High Pollution.

The project includes data preprocessing, pollution trend analysis, interactive visualizations, and a Streamlit dashboard that allows users to upload a CSV dataset and explore pollution patterns across cities.

## 🎯 Objectives

- Analyze air quality data across different cities.
- Clean the dataset by handling missing values.
- Study air quality indicators such as PM2.5, PM10, NO2, CO, and SO2.
- Apply K-Means clustering to identify pollution patterns.
- Categorize observations into low, moderate, and high pollution groups based on average AQI.
- Visualize AQI trends and pollution distributions.
- Identify cities with higher average Air Quality Index (AQI) values.
- Provide an interactive dashboard for exploring pollution data.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib
- **Dashboard:** Streamlit
- **Dataset Format:** CSV
- **Development Environment:** Visual Studio Code

## 🧠 Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised machine learning algorithm that groups data points into clusters based on similarities in their feature values.

In this project, K-Means is applied to five air pollution indicators:

- PM2.5
- PM10
- NO2
- CO
- SO2

### Workflow

1. Load the air quality dataset.
2. Select the relevant pollution indicators and AQI columns.
3. Remove rows containing missing values in the selected columns.
4. Standardize the pollution indicators using `StandardScaler`.
5. Apply K-Means clustering with three clusters.
6. Calculate the average AQI for each cluster.
7. Assign Low Pollution, Moderate Pollution, and High Pollution labels according to the clusters' average AQI.
8. Save the processed data and visualize the results.

**Note:** The pollution categories are derived from the average AQI of the generated clusters. They are analytical labels for this project and should not be treated as official regulatory AQI classifications.

## 📊 Features

### 1. Data Preprocessing
- Loads air quality data from a CSV file.
- Selects relevant columns.
- Removes records with missing values.

### 2. City-Wise Analysis
- Allows users to select a city.
- Displays air quality records for the selected city.
- Helps explore pollution levels across locations.

### 3. AQI Trend Visualization
- Displays a line chart showing AQI trends over time for the selected city.

### 4. Pollution Clustering
- Groups observations using K-Means.
- Identifies low, moderate, and high pollution clusters based on average AQI.

### 5. Pollution Distribution
- Displays pollution category counts.
- Provides bar charts and pie charts to understand category distribution.

### 6. Cluster Visualization
- Creates a scatter plot comparing PM2.5 and PM10 values.
- Displays cluster centroids to help visualize the grouping of observations.

### 7. Top Polluted Cities
- Calculates average AQI for each city.
- Displays the ten cities with the highest average AQI in the available dataset.

### 8. Interactive Streamlit Dashboard
- Supports CSV file uploads.
- Displays data samples, charts, cluster information, and pollution summaries.

## 📁 Project Structure

```text
Smart-City-Pollution-Analysis/
│
├── app/
│   └── app.py
│
├── data/
│   └── air_quality.csv
│
├── results/
│   └── output.csv
│
├── main.py
├── requirements.txt
└── README.md
```

- `main.py` — Runs the data preprocessing, K-Means clustering, visualization, and CSV export workflow.
- `app/app.py` — Runs the interactive Streamlit dashboard.
- `data/air_quality.csv` — Input dataset used by the Python analysis script.
- `results/output.csv` — Output file containing processed records and pollution categories.
- `requirements.txt` — Python dependencies required to run the project.
- `README.md` — Project documentation.

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or another compatible Python version.
- Visual Studio Code.
- Git, if you want to clone or upload the repository.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-City-Pollution-Analysis.git
```

Navigate to the project folder:

```bash
cd Smart-City-Pollution-Analysis
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install pandas matplotlib scikit-learn streamlit
```

Alternatively, install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes the required packages: `pandas`, `matplotlib`, `scikit-learn`, and `streamlit`.

## ▶️ How to Run the Project

### Option 1: Run the Python Analysis Script

From the project root directory, run:

```bash
python main.py
```

The script processes the dataset, applies K-Means clustering, saves the clustered records to `results/output.csv`, and displays a scatter plot.

### Option 2: Run the Streamlit Dashboard

From the project root directory, run:

```bash
streamlit run app/app.py
```

A local browser window will open with the dashboard.

Upload a CSV file containing the required columns to explore the analysis.

## 📄 Dataset Requirements

The dataset should contain the following columns:

| Column | Description |
|---|---|
| `City` | Name of the city |
| `Date` | Date of the air quality observation |
| `PM2.5` | Fine particulate matter concentration |
| `PM10` | Particulate matter concentration |
| `NO2` | Nitrogen dioxide measurement |
| `CO` | Carbon monoxide measurement |
| `SO2` | Sulfur dioxide measurement |
| `AQI` | Air Quality Index value |

The Streamlit dashboard requires all eight columns. The standalone Python script uses the city name, five pollution indicators, and AQI.

Make sure the uploaded CSV uses these column names and compatible numeric values for the pollution indicators and AQI.

## 📈 Expected Output

After running the project, users can explore:

- Cleaned air quality records.
- K-Means cluster assignments.
- Low, moderate, and high pollution category labels.
- AQI trends for individual cities.
- Pollution category counts and distribution charts.
- PM2.5 versus PM10 cluster visualization.
- Cities ranked by average AQI.
- An exported CSV file containing the analysis results.

Actual findings depend on the dataset supplied to the project.

## 🌱 Applications

- Exploratory air quality analysis.
- Smart city environmental monitoring prototypes.
- City-wise pollution comparisons.
- Identification of pollution patterns in historical data.
- Educational demonstrations of unsupervised machine learning.
- Data-driven environmental awareness.

## 🔮 Future Enhancements

- Integrate real-time air quality data from reliable sources.
- Add interactive city maps and geographic visualizations.
- Include more pollutants and weather-related variables.
- Compare clustering results with official AQI categories.
- Improve missing-value handling and outlier detection.
- Evaluate clustering quality using suitable metrics such as the silhouette score.
- Deploy the dashboard online for broader accessibility.
- Explore time-series forecasting for future AQI estimates.

## 👩‍💻 Author

**Shreyasi Gidmare**

Computer Science and Engineering | Artificial Intelligence and Machine Learning

## 📌 Conclusion

The Smart City Pollution Analysis project demonstrates how Python, data visualization, and unsupervised machine learning can be combined to explore air quality patterns across cities. By applying K-Means clustering to pollution indicators and analyzing average AQI values, the project provides a simple approach to grouping pollution observations and presenting the results through visualizations and an interactive dashboard.

The project serves as a foundation for further development of data-driven environmental monitoring and smart city analytics solutions.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
