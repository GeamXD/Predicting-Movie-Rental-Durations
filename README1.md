Welcome to the DVD Rental Length Prediction Project!

This project aims to predict DVD rental durations to optimize inventory management and maximize revenue potential for a DVD rental company.

**Project Background**

This project addresses the business problem of inefficient inventory management in a DVD rental company. Accurate prediction of rental durations allows for better stock allocation, minimizing losses due to overstocking or stockouts. This project uses historical rental data to train regression models. The intended end-users are the company's inventory management team and business strategists.

*   **Objective:** To predict DVD rental durations to optimize inventory management.
*   **Scope:** Develop regression models using historical rental data, focusing on achieving a Mean Squared Error (MSE) of less than 3.

**Data Overview and Preprocessing**

The dataset contains historical DVD rental information.

**Data Description:**

*   Number of records: Not specified in the provided information.
*   Features: Rental rates, movie length, release year, amount paid (`AMOUNT`), rental rate itself (`RENTAL RATE`), and a flag for NC-17 rated movies (`NC-17`).
*   Target Variable: Rental duration.

**Preprocessing Steps:**

1.  **Data Cleaning:** Basic cleaning was performed, but specific details are not provided. A significant data quality issue was identified: all rows had 2015 as the fixed rental/return year, limiting the scope of analysis.
2.  **Feature Engineering:** Dummy variables were created for categorical features. The target column (rental duration) was set up. Logarithmic preprocessing was applied to numeric features for the best performing model.
3.  **Data Splitting:** The data was split into training (80%) and testing (20%) sets.
4. **Feature Selection:** Implicitly, the model training and evaluation process served as a form of feature selection, highlighting the importance of AMOUNT, RENTAL RATE, and NC-17.

**Machine Learning Pipeline**

This project employed multiple regression models to predict rental durations.

*   **Model Selection:** Multiple regression models were tested, with the Random Forest Regressor showing the best performance. The choice of Random Forest was likely due to its ability to handle non-linear relationships and feature importance analysis.
*   **Training:** Models were trained on the 80% training data.
*   **Evaluation:** Model performance was evaluated using Mean Squared Error (MSE). The target was to achieve an MSE less than 3.
*   **Deployment:** No deployment details were provided as the focus was on model performance.

**Executive Summary**

**Key Results:**

The project successfully trained a Random Forest Regressor that achieved an MSE of 2.15, meeting the target metric. This model can be used to improve inventory planning by predicting rental durations.

*   The Random Forest Regressor achieved an MSE of 2.15.
*   Predicting rental durations can lead to optimized inventory, reducing costs and increasing revenue potential.

**Model Insights**

**Category 1 (Feature Importance):**

*   **Insight 1:** `AMOUNT`, `RENTAL RATE`, and `NC-17` were identified as the top predictive features.
*   **Insight 2:** This suggests that pricing and content rating significantly influence how long customers keep DVDs.

**Recommendations**

*   **Price sensitivity:** Lowering DVD prices could lead to shorter rental durations. -> Consider strategic pricing experiments to optimize revenue.
*   **Rental rate adjustments:** Adjusting rental rates for different movie types or release dates could optimize returns. -> Implement dynamic pricing strategies based on predicted demand.
*   **NC-17 content impact:** NC-17 rated movies are rented for longer periods. -> Develop specific rental strategies for this content category, such as longer rental periods or different pricing.

**Assumptions and Caveats**

*   **Assumption 1:** The models assume historical rental patterns are indicative of future trends.
*   **Caveat 1:** The fixed rental/return year (2015) in the data is a significant limitation, potentially affecting the model's generalizability to other time periods.
*   **Caveat 2:** Limited data exploration due to the project's focus on model performance might have missed other valuable insights.
*   **Caveat 3:** The project suggests the need for data augmentation from other movie rental businesses to address the data quality issues
