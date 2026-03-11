import joblib
import pandas as pd
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression

# load dataset
data = load_linnerud(as_frame=True)
X = data.data
y = data.target

# Train model
model = LinearRegression()
model.fit(X, y)
# save model

joblib.dump(model,"linnerud_model.pkl")
print("Model saved")
