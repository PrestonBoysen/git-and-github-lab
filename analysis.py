import pandas as pd
df = pd.read_csv("sales.csv")
print("N Rows:", len(df))
print("Mean sale", df["amount"].mean())
print("Largest Sale", df["amount"].max())