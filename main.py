from data_integration import DataIntegrator
from performance_prediction import PerformancePredictor

if __name__ == "__main__":
    integrator = DataIntegrator()
    
    # Example usage - replace with actual data
    # data_df1 = pd.read_csv('data1.csv')
    # data_df2 = pd.read_csv('data2.csv')
    # integrator.add_data_source(data_df1)
    # integrator.add_data_source(data_df2)
    
    predictor = PerformancePredictor()
    predictor.load_data(integrator)
    predictor.train_model()
    # predictions = predictor.predict(new_data_df)
