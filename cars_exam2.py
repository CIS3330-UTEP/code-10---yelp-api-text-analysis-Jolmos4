import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('cars.csv')
# car_brands = ['Audi', 'BMW', 'Volkswagen']
# cars_df = df.query('Identification_Make == @car_brands')

# cars_count = cars_df.groupby(by='Identification_Make')

file_path = 'cars.csv' 
cars_data = pd.read_csv(file_path)


numeric_cols = cars_data.select_dtypes(include=['number'])

unique_features = numeric_cols.groupby(cars_data['Identification.Make']).mean()

print(unique_features)

print("Available numeric columns:", numeric_cols.columns)