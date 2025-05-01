import pandas as pd
import json

# Step 1: Check CSV
csv_path = 'Data/tree-loss-provincewise-2001-2023.csv'
df_csv = pd.read_csv(csv_path)
print("CSV Dataset Preview:")
print(df_csv.head())
print("\nCSV Columns:", df_csv.columns.tolist())

# Step 2: Check JSON
json_path = 'Data/NPL-weather-from 1950-2023.json'
with open(json_path) as f:
    treeloss_data = json.load(f)

print("\nJSON Keys/Structure:")
print(treeloss_data.keys() if isinstance(treeloss_data, dict) else type(treeloss_data))
