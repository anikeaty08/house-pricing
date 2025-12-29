import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


# =========================
# Load CSV dataset
# =========================
df = pd.read_csv(
    "housing.csv",
    encoding="latin1",
    engine="python"
)

print("Dataset loaded.")

# =========================
# Split features and target
# =========================
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# =========================
# Train-test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Preprocessing
# =========================
num_features = X.select_dtypes(include=[np.number]).columns
cat_features = ["ocean_proximity"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipeline = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, num_features),
    ("cat", categorical_pipeline, cat_features)
])

# =========================
# Model
# =========================
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# =========================
# Train
# =========================
print("Training model...")
pipeline.fit(X_train, y_train)

# =========================
# Save model
# =========================
joblib.dump(pipeline, "models/housing_model.pkl")
print("Model saved to models/housing_model.pkl")

# =========================
# Evaluate
# =========================
predictions = pipeline.predict(X_test)

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\n✅ Model trained successfully!")
print(f"📉 RMSE: {rmse:.2f}")
print(f"📊 R² Score: {r2:.4f}")
