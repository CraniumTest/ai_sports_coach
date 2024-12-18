import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

class PerformancePredictor:
    def __init__(self):
        self.model = GradientBoostingRegressor()
        self.data = None

    def load_data(self, data_integrator):
        self.data = data_integrator.consolidate_data()

    def train_model(self):
        X = self.data.drop('performance_metric', axis=1)
        y = self.data['performance_metric']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained with MSE: {mse}")

    def predict(self, new_data):
        return self.model.predict(new_data)
