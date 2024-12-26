### **Predicting DVD Rental Lengths**

---

### **1. Problem Statement**

- **Objective:** Develop regression models to predict rental durations, helping the company optimize inventory.
- **Business Goal:** By accurately predicting rental lengths, the company can enhance inventory management, reduce stock-outs, and improve customer satisfaction.

---

### **2. What I Understood**

- **Problem:** Understanding factors influencing rental durations to forecast demand.
- **Data Overview:** Dataset includes features like rental rates, movie length, release year, and categorical variables such as movie ratings.
- **Goal:** Focused on building a model with Mean Squared Error (MSE) < 3.

---

### **3. What I Did**

- **Data Preprocessing:**
  - Cleaned and transformed the dataset (e.g., created dummy variables for categorical columns).
  - Defined the target column as rental days.
  - Split data into 80% training and 20% testing sets.

- **Feature Engineering:**
  - Applied logarithmic transformation to numeric columns to reduce skewness.

- **Model Selection:**
  - Experimented with multiple regression models, including Linear Regression, Random Forest, and Gradient Boosting.

---

### **4. Evaluation Metrics**

- **Primary Metric:** Mean Squared Error (MSE) was chosen to penalize large prediction errors effectively.
- **Model Comparisons:** Random Forest Regressor performed best, achieving an MSE of 2.15.

---

### **5. Communication & Collaboration**

- Created visualizations to highlight the relationships between top features and rental durations.
- Summarized findings and recommendations for inventory optimization in a concise report.

---

### **6. Insights & Observations**

- **Key Features:**
  - `AMOUNT`: Higher amounts were strongly predictive of longer rental durations.
  - `RENTAL RATE`: Pricing directly impacted rental behavior.
  - `NC-17`: Movies with this rating were often retained longer.

- **Observations:** Limited exploratory data analysis was done due to the primary focus on achieving the MSE goal.

---

### **7. Challenges & Solutions**

- **Data Quality Issue:**
  - All rows had 2015 as the fixed rental/return year.
  - Solution: Focused on other predictive features and recommended data augmentation for future improvements.

- **Exploration Limitation:**
  - Minimal analysis was performed due to the project's machine learning-centric goal.
  - Solution: Suggested follow-up studies to explore feature relationships in depth.

---

### **8. Final Recommendation**

- The Random Forest Regressor with logarithmic preprocessing is the recommended model.
- Achieved an MSE of 2.15, meeting the goal.
- Emphasize pricing strategies (e.g., DVD price and rental rate) and consider the impact of `NC-17` rated movies on inventory planning.

---

### **9. Next Steps**

- Augment the dataset with data from other movie rental businesses to improve model generalizability.
- Conduct detailed exploratory analysis to better understand feature interactions.
- Test additional regression techniques and hyperparameter tuning for further performance gains.
