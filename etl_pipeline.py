import pandas as pd

# Extract
data = pd.read_csv("sample_data.csv")

# Transform
data['amount_tax'] = data['amount'] * 1.1

# Load
data.to_csv("processed_data.csv", index=False)

print("ETL pipeline completed")
