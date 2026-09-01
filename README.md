# AirBase-Fleet-AI-Advisor
# 🛩️ AirBase Fleet AI Advisor

An intelligent military airbase management system built with **Python**, **Object-Oriented Programming (OOP)**, and **Machine Learning (Random Forest)**. 

The system tracks military aircraft status and predicts the optimal fighter jet (**Su-35 Flanker-E** vs. **Su-57 Felon**) for tactical missions based on mission parameters.

---

## 📌 Features

- **Fleet Tracking & Management (OOP):** Add aircraft with specifications (Speed in km/h converted to Mach, Missiles count, Fuel level) and monitor fleet status.
- **Custom-Built Dataset:** Trained on a handcrafted tactical mission dataset (`AirBaseData.csv`) simulating real-world defense parameters.
- **AI Mission Advisor:** Employs a `RandomForestClassifier` to recommend the right aircraft based on:
  - **Distance** ($1 - 1000\text{ km}$)
  - **Radar Threat Level** ($1 - 10$)
  - **Stealth Requirement** ($0 = \text{No}, 1 = \text{Yes}$)

---

## 🎯 Aircraft Profile

| Aircraft | Role | Key Strengths |
| :--- | :--- | :--- |
| **Su-35** | 4++ Gen Air Superiority | Heavy payload, high speed, long-range engagements |
| **Su-57** | 5th Gen Stealth Multirole | Low radar observability, high-threat stealth penetration |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** Pandas, Scikit-Learn
- **Algorithm:** Random Forest Classifier (`n_estimators=100`)

