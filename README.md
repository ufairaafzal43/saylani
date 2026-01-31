

# 📊 Student Dropout Early Warning System (ML Project)

**Link to Colab Notebook:**
🔗 [https://colab.research.google.com/drive/1d7mjhbuNS_4WGYZcP462T2n7gJ7r64s5?usp=sharing](https://colab.research.google.com/drive/1d7mjhbuNS_4WGYZcP462T2n7gJ7r64s5?usp=sharing)

---

## 📌 Project Summary

University administrators want to reduce student dropout rates by identifying students at risk **early in the semester** based on **academic activity and engagement data** — *before final grades or end-semester outcomes are available*.
This project uses machine learning to build an early warning system that predicts whether a student is likely to drop out, assigns a risk score, and provides actionable outputs for advisors.

---

## 🎯 Problem Statement

A university is losing students every semester. They need a **data-driven early warning system** so academic advisors can intervene before students drop out.

Your task as a data scientist is to:

* Predict which students are at risk of dropping out (binary classification: Continue vs Risk)
* Identify high-risk students early in the semester
* Provide an interpretable risk score and explanation for each prediction

---

## 📂 Dataset

**Dataset Used:**
📘 *Student performance dataset — xAPI-Edu-Data* (Kaggle)

🔗 [https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data)

The dataset contains early semester features like:

* Class engagement metrics (raisedhands, VisITedResources, AnnouncementsView, Discussion)
* Student demographics (gender, nationality, etc.)
* Parental involvement and satisfaction
* Absenteeism patterns

---

## 🚀 What You Built

The following deliverables are included:

### 1. **Trained Machine Learning Model**

* A **pipeline model** that integrates preprocessing and classification
* Trained on early engagement metrics
* Outputs:

  * **Risk score** (probability of dropout)
  * **Predicted dropout** (0 = Continue, 1 = Risk)
  * **Risk label** (Low / Medium / High)

Saved model file: `early_warning_dropout_model.joblib`

---

### 2. **Predictions Output**

Generate a **CSV of predictions** for a set of students with:

| student_id | risk_score | risk_label | predicted_dropout |
| ---------- | ---------- | ---------- | ----------------- |

This file can be downloaded from the Streamlit app.

---

### 3. **Streamlit Application**

Interactive web app where users can:

✔ Upload a CSV of student activity
✔ View a **Top 20 High-Risk Students** table
✔ Select a student’s index to view:

* Risk score
* Risk label
* Predicted dropout
* A simple feature-based explanation

App file: `app.py`

---

## 🧠 Machine Learning Approach

### ✔ Target

A binary proxy for dropout was defined using the original `Class` label:

```python
df['dropout_risk'] = df['Class'].map({'L': 1, 'M': 0, 'H': 0})
```

* `1` → High risk (Low performance)
* `0` → Continue (Medium & High performance)

This proxy enables early intervention modeling before final grades.

---

### ✔ Feature Selection

Focus was given to **early engagement metrics**:

| Feature           | Meaning                       |
| ----------------- | ----------------------------- |
| raisedhands       | Class participation           |
| VisITedResources  | Resource usage                |
| AnnouncementsView | Announcement viewing patterns |
| Discussion        | Discussion engagement         |

These are available early and directly reflect student activity.

---

### ✔ Model & Pipeline

* Preprocessing: Standard scaling
* Model: Random Forest Classifier
* Persisted as a single pipeline file
* Evaluated using precision, recall, and F1-score

This approach ensured:

✔ Fairness
✔ Interpretability
✔ Good early detection performance
✔ Advisor-friendly outputs

---

## 📊 How Risk is Determined

The model outputs a **dropout probability (risk score)**.
Risk labels are assigned as follows:

| Risk Score          | Risk Label  |
| ------------------- | ----------- |
| score ≥ 0.70        | High Risk   |
| 0.40 ≤ score < 0.70 | Medium Risk |
| score < 0.40        | Low Risk    |

This allows advisors to prioritize interventions.

---

## 🧪 Usage Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/<your-username>/student-dropout-early-warning.git
cd student-dropout-early-warning
```

---

### 2. **Install Requirements**

Create a virtual environment and install:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

pip install -r requirements.txt
```

**requirements.txt:**

```
pandas
numpy
scikit-learn
joblib
streamlit
```

---

### 3. **Run the Streamlit App**

```bash
streamlit run app.py
```

Upload your student dataset CSV and interact with risk outputs!

---

## 📝 Key Insights & Findings

* Low engagement metrics (low participation, resource usage, and discussion scores) often correlate with **high dropout risk**.
* Absence patterns and parental satisfaction also influence risk.
* A numeric-only model provides **fast, interpretable, and actionable predictions** for advisors.

---

## 📌 Ethical & Real-World Notes

* Sensitive demographic attributes (like gender) were not used as primary predictors to maintain fairness.
* Risk scores are probability estimates, not absolute certainties.
* Advisors should interpret results in context and combine with qualitative insights.

---

## 🧾 Citation

If you reuse this work, please cite:

**Student Dropout Early Warning System (ML Project)**
GitHub: [https://github.com/](https://github.com/)<your-username>/student-dropout-early-warning

---

## 🚀 Next Steps (Optional)

✔ Hyperparameter tuning for better accuracy
✔ Add SHAP explanations for feature contributions
✔ Deploy the Streamlit app on **Streamlit Community Cloud**
✔ Add student historical profiles for longitudinal insights


Just tell me! 😊

