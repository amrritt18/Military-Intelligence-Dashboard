# 🛡️ AI-Based Military Intelligence Dashboard

An end-to-end AI-powered Military Intelligence Dashboard built using **Python**, **Streamlit**, **Machine Learning**, **Time Series Forecasting**, and **Interactive Data Visualization** to analyze historical terrorism incidents from the **Global Terrorism Database (GTD)**.

The dashboard enables users to explore terrorism data, identify trends, predict attack types, estimate threat levels, forecast future incidents, and generate AI-assisted intelligence reports through an interactive web interface.

---

# 📌 Project Overview

Understanding terrorism trends is critical for intelligence analysis, strategic planning, and decision support.

This project transforms raw historical terrorism records into actionable insights by integrating:

* Interactive dashboards
* Machine Learning prediction models
* Time-series forecasting
* AI-generated intelligence reports
* Data exploration tools

The dashboard is designed to support data-driven security analysis while demonstrating practical applications of Machine Learning and Data Science.

---

# 🚀 Key Features

### 🏠 Home Dashboard

* Dashboard overview
* Key performance indicators
* Historical attack trend visualization

---

### 🌍 Global Threat Map

* Interactive world map
* Geographic visualization of terrorism incidents
* Year-wise filtering

---

### 🌎 Country Analysis

* Country-specific intelligence dashboard
* Historical attack trends
* Top terrorist organizations
* Weapon analysis
* Interactive incident map
* Download filtered country data

---

### 🤖 Attack Type Prediction

Predicts the likely attack type using a trained Random Forest classifier.

**Input Features**

* Country
* Region
* Weapon Type
* Target Type
* Terrorist Group
* Success
* Suicide Attack
* Fatalities
* Injuries

**Output**

* Predicted Attack Type
* Prediction Confidence

---

### 🚨 Threat Level Prediction

Predicts the severity of a potential terrorist incident.

**Input Features**

* Country
* Region
* Attack Type
* Weapon Type
* Target Type
* Terrorist Group

**Output**

* LOW
* MEDIUM
* HIGH

---

### 📈 Terrorism Forecasting

Forecasts future terrorist incidents using the **Prophet Time Series Forecasting Model**.

Features include:

* Historical trend visualization
* Future forecasting
* Confidence interval
* Growth analysis
* Threat trend assessment

---

### 🧠 AI Intelligence Report

Automatically generates an intelligence report including:

* Executive Summary
* Threat Assessment
* High-Risk Countries
* Active Terrorist Organizations
* Strategic Recommendations
* Future Outlook

---

### 📊 Data Explorer

Interactive dataset exploration with:

* Multi-level filters
* Search functionality
* Statistical summary
* Missing value analysis
* Visual analytics
* CSV export

---

### ⚙️ Dashboard Information

Provides:

* Dataset statistics
* Machine learning model details
* Forecasting model information
* Technology stack
* Project structure
* System information

---

# 🧠 Machine Learning Models

## Attack Type Prediction

* Algorithm: Random Forest Classifier
* Multi-class Classification

---

## Threat Level Prediction

* Algorithm: Random Forest Classifier

Threat Levels:

* LOW
* MEDIUM
* HIGH

---

## Forecasting

* Algorithm: Prophet Time Series Forecasting

---

# 📊 Dataset

**Dataset Name**

Global Terrorism Database (GTD)

The dataset contains historical information about terrorism incidents worldwide, including:

* Country
* Region
* City
* Attack Type
* Weapon Type
* Target Type
* Terrorist Group
* Fatalities
* Injuries
* Success
* Suicide Attack
* Latitude & Longitude

---

# 🛠️ Technologies Used

### Programming

* Python

### Dashboard

* Streamlit

### Machine Learning

* Scikit-learn
* Random Forest

### Forecasting

* Prophet

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Model Serialization

* Joblib

### Version Control

* Git
* GitHub

---

# 📁 Project Structure

```
Military-Intelligence-Dashboard/
│
├── app.py
├── train_attack_model.py
├── train_threat_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── globalterrorism.csv
│
├── models/
│   ├── attack_prediction_model.pkl
│   ├── feature_encoders.pkl
│   ├── target_encoder.pkl
│   ├── threat_level_model.pkl
│   ├── threat_feature_encoders.pkl
│   └── threat_target_encoder.pkl
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Global_Threat_Map.py
│   ├── 3_Country_Analysis.py
│   ├── 4_Attack_prediction.py
│   ├── 5_Threat_Level_Prediction.py
│   ├── 6_Forecasting.py
│   ├── 7_AI_Intelligence_Report.py
│   ├── 8_Data_Explorer.py
│   └── 9_Settings.py
│
└── utils/
    ├── constants.py
    ├── data_loader.py
    ├── helpers.py
    ├── prediction.py
    ├── preprocessing.py
    ├── report_generator.py
    └── visualization.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <YOUR_REPOSITORY_LINK>
```

Move into the project

```bash
cd Military-Intelligence-Dashboard
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Dashboard Preview

Add screenshots of:

* Home Dashboard
* Global Threat Map
* Country Analysis
* Attack Prediction
* Threat Level Prediction
* Forecasting
* AI Intelligence Report
* Data Explorer

---

# 🎯 Skills Demonstrated

* Machine Learning
* Classification
* Time Series Forecasting
* Feature Engineering
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Interactive Dashboard Development
* Data Visualization
* AI-assisted Reporting
* Python Programming
* Git & GitHub

---

# 💡 Future Improvements

* Deep Learning–based prediction models
* LSTM forecasting
* Real-time intelligence feeds
* NLP-based intelligence summarization
* User authentication
* REST API integration
* Cloud deployment
* Advanced geospatial analytics

---

# 👨‍💻 Author

**Amrit Raj**

M.Tech – Robotics & Artificial Intelligence
Indian Institute of Technology (IIT) Bhubaneswar

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.
