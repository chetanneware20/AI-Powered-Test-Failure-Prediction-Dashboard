# AI-Powered-Test-Failure-Prediction-Dashboard

Overview

This project is an intelligent system that combines Automation Testing and Data Science to predict high-risk test cases in regression suites. It uses historical automation test execution data to train a machine learning model and provides a Streamlit dashboard to visualize results, module-wise risk, and overall test health.

The dashboard also allows exporting detailed CSV reports for stakeholders.

Features

Upload historical test results in CSV format

Predict test failures using a Random Forest classifier

Display high-risk test cases before execution

Module-wise risk analysis and summary statistics

Model evaluation metrics: Accuracy, Precision, Recall, Confusion Matrix

Interactive Streamlit dashboard for data visualization

Downloadable detailed CSV report

Technology Stack

Programming Language: Python

Frontend Dashboard: Streamlit

Machine Learning: Scikit-learn (Random Forest Classifier)

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Automation Data Source: Selenium or Playwright

Project Structure
ai-powered-test-failure-prediction-dashboard/
│
├── app.py                 # Main Streamlit dashboard
├── model.py               # ML model training and preprocessing
├── sample_test_data.csv   # Example test data
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
Installation

Clone the repository:

git clone <your-repo-url>
cd ai-powered-test-failure-prediction-dashboard

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py
Usage

Prepare your automation test results in CSV format with the following columns:

test_case_id

module

execution_time

previous_failures

last_run_status (Pass/Fail)

build_number

Upload the CSV file using the dashboard.

The system will train a Random Forest model and display:

Raw test data

Predicted failure probabilities

High-risk test cases

Module-wise risk summary

Model performance metrics

Download the detailed report as a CSV file for analysis or stakeholder review.

Sample Data

A sample CSV file is included as sample_test_data.csv for demonstration and testing purposes.

Future Enhancements

Integrate with live Selenium or Playwright test execution

Add PDF executive report generation

Deploy to cloud platforms for CI/CD integration

Include feature importance visualization for explainable AI

Implement self-healing automation based on prediction results

Business Impact

Reduces regression test execution time by prioritizing high-risk cases

Enables data-driven QA decision making

Improves release confidence

Helps identify unstable modules proactively

Author

[Chetan Neware] – Combining Automation Testing and Data Science to build intelligent QA solutions.
