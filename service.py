import bentoml
import pandas as pd

@bentoml.service
class HousingPriceService:
    def __init__(self):
        # Load model from BentoML model store
        self.model = bentoml.sklearn.load_model(
            "housing_price_model:mbdbcq7e22w6xehi"
        )

    @bentoml.api
    def predict(self, input_data: dict) -> dict:
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]
        return {
            "predicted_price": float(prediction)
        }
