import pandas as pd

iris_data = pd.read_csv('iris.csv')

# Check for missing values and handle them
missing_values = iris_data.isnull().sum()
print("Missing Values:\n", missing_values)

iris_data.dropna(inplace=True)

iris_data.columns = ['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm', 'class']

iris_data.to_excel('cleaned_iris.xlsx', index=False)

imported_iris_data = pd.read_excel('cleaned_iris.xlsx')

print("Imported Data:\n", imported_iris_data.head())

iris_subset = iris_data[['sepal_length_cm', 'sepal_width_cm', 'class']].head(10)  # Example subset
iris_subset.to_json('iris_subset.json', orient='records')
