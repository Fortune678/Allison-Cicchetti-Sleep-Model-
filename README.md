 # Mammal Sleep Duration Predictor 🐾 💤

This project uses the classic 1976 Allison & Cicchetti dataset to predict the total daily sleep of mammals based on their physical traits (body/brain weight) and ecological factors (predation risk and danger index).

## 🚀 Overview
The model compares **Multiple Linear Regression** and **Decision Tree Regressors** to identify how environmental "danger" and physiological "scale" influence mammalian rest patterns.

## 📊 Dataset Acknowledgement
The data used in this project was sourced from the **[Sleep Dataset on Kaggle](https://www.kaggle.com)**. 
> **Note to Viewers:** If you're interested in exploring this data further or running your own kernels, I highly recommend using **[Kaggle's Notebook environment](https://www.kaggle.com)**, which provides excellent built-in tools for data visualization and community-driven insights.

  ombination of predation risk and sleep exposure) often outweighs physical weight in predicting sleep duration
  
## 🛠️ Installation & Setup

To run this project locally, ensure you have Python 3.8+ installed, then follow these steps:

  1.Clone the repository:
  
     git clone https://github.com
     cd Mammal-Sleep-Predictor
       
  2.Create a Virtual Environment (Recommended):
   This keeps your project dependencies isolated.
   
     python -m venv venv
     source venv/bin/activate  # On Windows use: venv\Scripts\activate

  3.Install all dependencies in one go:
  
     pip install pandas numpy scikit-learn jupyter

  4.Launch the analysis:

   For the Notebook: Run jupyter notebook and open mammal_sleep.ipynb.
   For the Script: Run python mammal_sleep.py directly in your terminal.

## 🧠Methodology: The "Why"

Log Transformation: Because mammalian weights range from 0.01kg (shrew) to   6,000kg (elephant), raw data creates extreme outliers. I applied np.log() to linearize these relationships, ensuring the model treats a 10% weight increase equally across all species sizes.
Decision Trees: I used DecisionTreeRegressor to capture non-linear interactions, such as how 'Danger Index' might override 'Body Weight' in high-risk environments.
   
   5. 📈 Results: MAE & Biological Meaning
 Through validation, the Decision Tree with 5 leaf nodes achieved the best  performance:
    Initial MAE: 3.52 hours
    Optimized MAE: 3.01 hours

Interpretation: On average, the model predicts a mammal's sleep within ±3 hours. The results suggest that 'Danger' and 'Gestation' are often more powerful predictors than size alone, supporting the theory that sleep is an evolutionary survival strategy.

