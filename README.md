# Linnerud Fitness Prediction System

This project predicts **Weight, Waist, and Pulse** based on exercise performance using **Linear Regression**.  
It is implemented as an interactive **Streamlit app**.

---

## Project Overview

The main purpose of this project is to know how does physical fitness — **Chins, Situps, and Jumps** —  relate to the body measument.
Using Liner Regression Model aim is to predict body measurement based on exercise perfomance and analyze how exercies impact overall physical health

## Dataset
Linnerud dataset contains exercise performance variables (Chins, Situps, Jumps) and physiological measurements (Weight, Waist, Pulse) for 20 individuals.

- Source: [Linnerud Dataset - Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html)  
- Type: Multi-Output Regression Datasets
- **Features (Exercises):**
  - Chins – upper-body strength exercise
  - Situps – abdominal muscles exercise
  - Jumps – vertical jump test for lower body strength and power
- **Targets (Physiological measurements):**
  - Weight - body weight of individual (lbs)  
  - Waist - Central body fat distribution (inches)  
  - Pulse - Number of heart beat per min while person is at rest (bpm)  

---

## Exploratory Data Analysis (EDA)

EDA was performed to **understand the dataset, detect patterns, and guide modeling**. The following steps were taken:

### 1. **Data Understanding and Preprocessing**
Linnerud dataset contain 20 observation and 6 variables, where by 3 are feature variable and 3 are target variable, no missing value in all variable and all record are unique (no duplicate)

### 2. **Statistical Summary**
- Calculated **mean, median, standard deviation, min, max, and quartiles** for all features and target variables.
- Observations:
  - `Chins` and `Situps` have moderate spread and a few high-value outliers.
  - `Jumps` has slightly lower variability.
  - `Weight` and `Waist` are positively correlated.
  - `Pulse` has smaller variance, showing less dependency on exercises.

### 3. **Unvariate Analysis**
- **Histograms** were used to visualize the **frequency distribution** of each feature and target.
  - `Situps` is widely distribution indicating larger differences in physical exercise
  - `Chins` is roughly normally distributed.
  - `jumps` is positive skewed indicating highy perfoming individual
    
- **Density plots** provide smooth curves showing **probability distribution**.
- - `Situps` shows most participants perform between 100–200 repetitions.
  - `Chins` indicating that most participants perform a moderate number of chin-ups
  - `Jumps` distribution slightly extend toward higher values
  
### 4. **Outlier Detection**
- **Box plots** reveal extreme values:
  - `Jumps` and `Situps` have no outliers and showing that many participants perform a moderate to high number of sit-ups..
  - `Chins` no outliers and showing Most individuals have similar upper-body strength levels, with mostly performing moderate to fewer chin-ups.
- Outliers are considered but retained because the dataset is small and they represent real variation.

### 5. **Relationships Between Variables**
- **Scatter plots** and **regression plots** were used:
  - `Situps` vs `Waist` show negative relationship, participant who doing more situps have small waist size..
  - `Chins` vs `Pulse` shows weak correlation.
  - `Jumps` vs `Weight` shows slightly negative correlation.
- This indicates **exercise performance affects physiological measurements differently** also becouse of small observation many correlation are not strong.

### 6. **Correlation Analysis**
- **Heatmap** was created to visualize correlations:
  - `Situps` strongly correlated with `Weight` (moderate positive correlation).
  - `Chins` moderately correlated with `Waist`.
  - `Pulse` weakly correlated with all exercises.
- Correlation values guided feature importance for modeling.

### **Insights from EDA**
No missing values or extreme outliers were detected also Correlation analysis shows moderate negative relationships between features and targets,
and scatter plots indicate roughly linear trends
Feature distributions are mostly symmetric with slight skewness in exercise counts and Multicollinearity is low

- **All features contribute differently** to target predictions.
- EDA confirms that Overall, the dataset is clean and well suited for a linear regression model without extensive preprocessing.

---

## Machine Learning Model
our model is Multi-Target Regression where a single model is used to predict multiple continuous target variables at the same time.

- **Algorithm:** Linear Regression  
- **Inputs (Features):** Chins, Situps, Jumps  
- **Outputs (Targets):** Weight, Waist, Pulse  

The model estimates **coefficients** that describe how exercises affect physiological measurements.
Regression Model involve predicting a continuous numeric output based on input variables and in linnerud dataset target variable ( weight, waist and pulse) 
are continuous numeric on their measurement which are suitable for prediction

---

## Model Split and Evaluation

- **Data splitting:** Typically train-test split (e.g., 80-20%), though small dataset may use full data.  
- **Evaluation Metrics:**  
  - **R² score:** How well the model fits the data.  
  - **Mean Squared Error (MSE):** Average squared prediction error  
- **Observations:** Model predicts values closely aligned with actual measurements.
  The regression model shows poor predictive performance on the Linnerud dataset. The Mean Squared Error (239) indicates large prediction errors, and the negative R² score (-1.35) suggests that the model does not fit linnerud dataset
  This result occurs due to the extremely small dataset size (20 samples) and weak correlations between exercise variables and body measurements.

---

## Prediction

- **Workflow:**  
  1. User inputs **Chins, Situps, Jumps**  
  2. Model predicts **Weight, Waist, Pulse**  
  3. Predictions shown in a **transparent table**  
  4. Scatter plots compare prediction to dataset values  

- **Interpretation:**  
  - Predicted values inside dataset cluster → normal/typical  
  - Predicted values outside cluster → unusual or extreme

- **General Conclution:**  
The Linear Regression model was used to predict Weight, Waist, and Pulse from exercise variables (Chins, Situps, and Jumps).
Due to the small size of the Linnerud dataset and the relatively weak correlations between features and target variables, the R² score may appear low or even negative.
However, the model still produces reasonable predictions that follow the general pattern of the dataset.
Therefore, the model can still be used as a simple predictive tool, but results should be interpreted with caution.
---

## Deployment
In the Linnerud project, deployment allows users to enter exercise data and
obtain predicted body measurements through a Streamlit web application hosted online and render.

- **Platform:** [Streamlit](https://streamlit.io/)  
- **Features:**  
  - Interactive input for exercises  
  - Transparent prediction table  
  - Scatter plots comparing predictions with dataset  
- **Advantages:**  
  - Lightweight, fast, and user-friendly  
  - Visual insights immediately available  
  - Can be hosted on Render, Heroku, or locally

---

## Libraries Used

- [Streamlit](https://streamlit.io/) – for web app interface  
- [Pandas](https://pandas.pydata.org/) – for data manipulation  
- [NumPy](https://numpy.org/) – for numerical operations  
- [Scikit-learn](https://scikit-learn.org/stable/) – for Linear Regression and dataset  
- [Matplotlib](https://matplotlib.org/) – for plotting  
- [Seaborn](https://seaborn.pydata.org/) – for enhanced visualization  

> All libraries are open-source and can be installed via `pip`.

---

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/linnerud-fitness.git
cd linnerud-fitness
