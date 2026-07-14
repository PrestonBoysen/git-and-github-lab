import pandas as pd
df = pd.read_csv("sales.csv")
print("rows:", len(df))
print("Mean sale amount", df["amount"].mean())