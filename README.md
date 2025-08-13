#  Fuel Consumption Estimator

##  Overview

This project predicts **fuel efficiency** (in km/l) of a vehicle using a **Linear Regression** model. The model is trained on a dataset containing vehicle speed, engine size, and weight. The predictive model is then deployed via a **Flask web application** with a clean HTML and CSS frontend.

-----

##  Features

  - **Linear Regression** model for accurate prediction.
  - **Flask backend** for serving predictions.
  - **HTML/CSS frontend** for user input and output display.
  - Simple, clean user interface.

-----

##  Project Structure

```
fuel_consumption_estimator/
│
├── model.py             # Trains and saves the Linear Regression model
├── app.py               # Flask app for prediction
├── templates/
│   └── index.html       # User input form and prediction result page
├── static/
│   └── style.css        # CSS styles for the frontend
├── data/
│   └── fuel_data.csv    # Dataset for training
├── model.pkl            # Trained model
└── README.md            # Project documentation
```

-----

##  Requirements

To install the necessary dependencies, use `pip`:

```bash
pip install Flask pandas numpy scikit-learn
```

-----

##  Dataset Description

The dataset (`data/fuel_data.csv`) contains historical vehicle data. An example of the data format is not provided, but the code shows the columns used.

**Columns:**

  - `Speed`: Vehicle speed in km/h.
  - `EngineSize`: Engine size in liters.
  - `Weight`: Vehicle weight in kg.
  - `FuelEfficiency`: Fuel efficiency in km/l (target variable).

-----

##  How It Works

### Model Training (`model.py`)

  - Loads the dataset from `data/fuel_data.csv`.
  - Splits the data into features (`X`) and the target variable (`y`).
  - Trains a `LinearRegression` model on the data.
  - Saves the trained model to a file named `model.pkl`.

### Prediction (`app.py`)

  - The Flask application loads the pre-trained `model.pkl` file.
  - It provides a web form where users can input `Speed`, `EngineSize`, and `Weight`.
  - Upon submission, it uses the loaded model to predict the fuel efficiency.
  - The prediction is then displayed on the same page.

-----

##  Running the Project

1.  **Train the Model**
    ```bash
    python model.py
    ```
2.  **Run Flask App**
    ```bash
    python app.py
    ```
3.  **Open in Browser**
    Go to: `http://127.0.0.1:5000/`

-----

##  Screenshots
---
Home Page

<img width="1172" height="465" alt="Screenshot 2025-08-13 102315" src="https://github.com/user-attachments/assets/93eaf445-5e9a-4901-92ff-cebb392b3ec8" />

---
Prediction Result

<img width="1148" height="351" alt="Screenshot 2025-08-13 102328" src="https://github.com/user-attachments/assets/67e28a50-60a8-4823-a261-5b225db576dd" />
