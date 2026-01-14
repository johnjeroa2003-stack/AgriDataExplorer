import pandas as pd

file_path = "data/raw/icrisat_raw.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully")
print("Shape:", df.shape)
print(df.head())
