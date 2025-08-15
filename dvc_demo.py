import pandas as pd
import os

#create a directory in data folder
os.makedirs("data/raw", exist_ok=True)

#create a dataframe
df = pd.DataFrame({
    "name": ["Adam", "Bob", "Charlie"],
    "age": [28, 35, 30],
    "car": ["Audi", "BMW", "Mercedes"]
})

#save the dataframe
df.to_csv("data/raw/abc_data.csv", index=False)
print("Data ingested successfully!")