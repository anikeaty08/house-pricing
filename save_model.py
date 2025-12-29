import joblib
import bentoml

model = joblib.load("models/housing_model.pkl")

bentoml.sklearn.save_model(
    "housing_price_model",
    model
)

print("Model saved to BentoML store")
