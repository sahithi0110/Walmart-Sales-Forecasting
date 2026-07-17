# Walmart Sales Forecasting

## Project Overview

This project focuses on forecasting weekly sales for Walmart stores using historical sales data and machine learning techniques. Accurate sales forecasting helps retailers optimize inventory, improve demand planning, and make informed business decisions.

---

## Objectives

* Analyze historical Walmart sales data.
* Perform data cleaning and preprocessing.
* Engineer meaningful features to improve prediction accuracy.
* Train and evaluate multiple machine learning models.
* Compare model performance using standard regression metrics.

---

## Dataset

The project uses the **Walmart Sales Dataset**, which contains historical sales records along with store information, promotional markdowns, economic indicators, and holiday information.

### Dataset Features

* Store
* Department (Dept)
* Date
* Weekly_Sales (Target Variable)
* IsHoliday
* Temperature
* Fuel_Price
* MarkDown1–MarkDown5
* CPI
* Unemployment
* Store Type
* Store Size

---

## Data Preprocessing

The following preprocessing steps were performed:

* Removed missing and inconsistent values.
* Converted the `Date` column into datetime format.
* Extracted:

  * Year
  * Month
  * Week
  * Quarter
* Encoded categorical variables.
* Sorted data by Store, Department, and Date.

---

## Feature Engineering

Additional time-series features were created to improve forecasting performance:

* Lag_1
* Lag_2
* Lag_4
* MA_4 (4-week Moving Average)
* Rolling_STD_4 (4-week Rolling Standard Deviation)

These features help capture historical sales trends and seasonality.

---

## Machine Learning Models

The following regression models were implemented:

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor
* XG Boost Regressor

---

## Model Evaluation

The models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

The best-performing model can be selected based on these evaluation metrics.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab
* XG Boost

---

## Project Structure

```
Walmart-Sales-Forecasting/
│
├── data/
│   └── Sales Dataset.csv
│
├── notebooks/
│   └── sales_forecasting.ipynb
│
├── outputs/
│   ├── graphs/
│   └── predictions/
│
├── report/
│
├── src/
│
├── README.md
│
└── requirements.txt
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/sahithi0110/Walmart-Sales-Forecasting.git
```

2. Navigate to the project directory:

```bash
cd Walmart-Sales-Forecasting
```

3. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

4. Open the notebook:

```bash
jupyter notebook
```

or upload the notebook to **Google Colab** and run all cells.

---
## Conclusion
This project successfully developed a machine learning-based Walmart sales forecasting system using historical retail data. Through data preprocessing, exploratory data analysis, feature engineering, and the implementation of multiple regression models—including Linear Regression, Random Forest, Gradient Boosting, and XGBoost—the project demonstrates the application of machine learning techniques for accurate weekly sales prediction and retail demand forecasting.
