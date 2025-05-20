
# HR Analytics Dashboard

This interactive dashboard provides insights into employee attrition using HR data. Built with Streamlit, it combines descriptive and predictive analytics to help HR professionals identify risk factors and make data-driven decisions.

## Features

- **Descriptive Analytics:**
  - Key metrics like attrition rate, average monthly income, and average age.
  - Interactive filters by department, education, and gender.
  - Visualizations showing attrition by job role, monthly income distribution, and satisfaction scores.

- **Predictive Analytics:**
  - Logistic regression model predicts the probability of employee attrition.
  - Displays an attrition risk score for each employee.
  - Visual highlights of high-risk groups for targeted interventions.

- **User-friendly UI:**
  - Clear layout with sidebar filters and explanatory markdown text.
  - Download filtered data as an Excel file for further analysis.

## Technologies Used

- Python, Pandas, Streamlit
- Plotly for interactive visualizations
- Scikit-learn for predictive modeling
- Openpyxl for Excel export

## How to Run

1. Clone the repo:
   ```
   git clone https://github.com/your-username/hr_analytics.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Business Value

This tool helps HR teams at organizations like RBC Wealth Management identify employees at risk of leaving, enabling proactive retention strategies that save costs and improve workforce stability.
