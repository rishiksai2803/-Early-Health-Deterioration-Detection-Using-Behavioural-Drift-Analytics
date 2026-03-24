# -Early-Health-Deterioration-Detection-Using-Behavioural-Drift-Analytics
A behavioural drift analytics-based system that detects early health deterioration by analyzing lifestyle deviations using a 7-day rolling baseline and generating interpretable health risk scores.
# 🧠 Early Health Deterioration Detection Using Behavioural Drift Analytics

## 📌 Project Overview
This project presents an intelligent system for detecting early signs of health deterioration by analyzing lifestyle behaviour patterns using **Behavioural Drift Analytics**. The system focuses on identifying gradual deviations in daily habits, enabling preventive healthcare rather than reactive treatment.

---

## ❗ Problem Statement
Traditional health monitoring systems:
- Use fixed thresholds
- Analyze individual parameters separately
- Fail to detect gradual lifestyle changes

However, health deterioration usually occurs **gradually through behavioural changes**, not sudden events.

---

## 💡 Proposed Solution
This project introduces a **Behavioural Drift Analysis Framework** that:
- Continuously monitors lifestyle behaviour
- Uses a **7-day rolling baseline**
- Detects deviations using drift analysis
- Generates a health score
- Classifies risk levels

---

## ⚙️ Features
- 📊 Behavioural Drift Score Calculation  
- ❤️ Health Score Evaluation  
- ⚠️ Risk Classification (Normal / Moderate / High)  
- 📈 Graph Visualization  
- 🧾 Lifestyle Trend Analysis  
- 🔍 Early Risk Detection  

---

## 🧠 Methodology

### Step 1: Data Collection
The system collects lifestyle parameters:
- Sleep Duration  
- Screen Time  
- Hydration Level  
- Physical Activity  

### Step 2: Baseline Calculation
A **7-day rolling average** is calculated:
Baseline = Average of last 7 days

### Step 3: Drift Calculation
Drift = |Current Value - Baseline|

### Step 4: Drift Score
Drift Score = Average of all parameter deviations

### Step 5: Health Score
Health Score = 100 - (Drift Score × Weight)



### Step 6: Risk Classification
- 80–100 → Normal  
- 60–79 → Moderate Risk  
- Below 60 → High Risk  

---

## 📊 Output
- Behavioural Drift Score  
- Health Score  
- Risk Level Classification  
- Graphical Comparison of Behaviour  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- (Optional: Streamlit)

---

## 📁 Project Structure
Early-Health-Deterioration-Detection/
│
├── main.py
├── data_input.py
├── baseline.py
├── drift.py
├── health_score.py
├── visualization.py
├── requirements.txt
├── README.md
│
├── data/
│ └── sample_data.csv
│
├── images/
│ └── output.png
│
├── report/
│ └── project_report.pdf

---

## ▶️ How to Run

### Step 1: Install Dependencies
pip install -r requirements.txt

### Step 2: Run the Project
python main.py

(For Streamlit version)
streamlit run app.py



---

## 📈 Example Output
- Drift Score: 1.85  
- Health Score: 81.5  
- Risk Level: Normal  

---

## 🌍 SDG Alignment
This project supports:

👉 **SDG 3 – Good Health and Well-being**

---

## ⚠️ Limitations
- Limited lifestyle parameters  
- Depends on accurate user input  
- No real-time sensor integration  
- Not a medical diagnosis system  

---

## 🚀 Future Scope
- Real-time wearable sensor integration  
- Machine learning prediction models  
- Personalized health monitoring  
- Mobile application development  
- Smart recommendation system  

---

## ⭐ Key Innovation
The project introduces a **Behavioural Drift Scoring System** that detects gradual lifestyle deviations using rolling statistical analysis instead of fixed thresholds or black-box prediction models.

---

## 📢 Conclusion
This system shifts healthcare from **reactive diagnosis to proactive lifestyle monitoring**, enabling early detection of potential health risks and promoting preventive wellness.

---

## 👨‍💻 Author
- Yellank Rishik sai  

## 🏫 Institution
- B V Raju Institute of Technology 

## 📅 Year
- 2026
