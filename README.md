 # Mammal Sleep Duration Predictor 🐾 💤

This project uses the classic 1976 Allison & Cicchetti dataset to predict the total daily sleep of mammals based on their physical traits (body/brain weight) and ecological factors (predation risk and danger index).

## 🚀 Overview
The model compares **Multiple Linear Regression** and **Decision Tree Regressors** to identify how environmental "danger" and physiological "scale" influence mammalian rest patterns.

## 📊 Dataset Acknowledgement
The data used in this project was sourced from the **[Sleep Dataset on Kaggle](https://www.kaggle.com)**. 
> **Note to Viewers:** If you're interested in exploring this data further or running your own kernels, I highly recommend using **[Kaggle's Notebook environment](https://www.kaggle.com)**, which provides excellent built-in tools for data visualization and community-driven insights.

 🛠️ Installation & Setup
To run this project locally, ensure you have Python 3.8+ installed, then follow these steps:

    Clone the repository:
    bash

    git clone https://github.com
    cd Mammal-Sleep-Predictor

    Use code with caution.
    Create a Virtual Environment (Recommended):
    This keeps your project dependencies isolated.
    bash

    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

    Use code with caution.
    Install all dependencies in one go:
    bash

    pip install pandas numpy scikit-learn jupyter

    Use code with caution.
    Launch the analysis:
        For the Notebook: Run jupyter notebook and open mammal_sleep.ipynb.
        For the Script: Run python mammal_sleep.py directly in your terminal.

🧠 Key Findings

    Log Transformation: Essential for normalizing the massive weight difference between species (e.g., Shrew vs. Elephant).
    Validation: A Decision Tree with 5 leaf nodes provided the lowest Mean Absolute Error (MAE), balancing the model between underfitting and overfitting.
    Top Predictor: The Danger Index (a combination of predation risk and sleep exposure) often outweighs physical weight in predicting sleep durati
