import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import gradio as gr
import numpy as np

df = pd.read_csv("data/fuel_data.csv")

X = df[['Speed', 'EngineSize', 'Weight']]
y = df['FuelEfficiency']  # Target

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')

def predict_fuel_efficiency(speed, engine_size, weight):
    input_data = np.array([[speed, engine_size, weight]])
    prediction = model.predict(input_data)[0]
    return round(prediction, 2)

interface = gr.Interface(
    fn=predict_fuel_efficiency,
    inputs=[
        gr.Number(label="Speed (km/h)"),
        gr.Number(label="Engine Size (liters)"),
        gr.Number(label="Weight (kg)")
    ],
    outputs=gr.Text(label="Estimated Fuel Efficiency (km/l)"),
    title="Fuel Consumption Estimator",
    description="Enter vehicle speed, engine size, and weight to estimate fuel efficiency."
)
if __name__ == "__main__":
    interface.launch(share=True)
