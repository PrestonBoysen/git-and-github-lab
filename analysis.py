import pandas as pd
df = pd.read_csv("sales.csv")
print("Number of transacations:", len(df))
print("Mean transaction sale", df["price"].mean())
# Print the Largest Sale: 
print("Largest transaction", df["price"].max())
# Print the Smallest sale: 
print("Smallest transaction", df["price"].min())
#Print the standard deviation of the transaction prices: 
print("Standard deviation of transaction prices:", df["Price"].sd())

