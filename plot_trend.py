import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("airpassengers_cleaned.csv")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Passengers"], marker="o", linestyle="-")
plt.title("Airline Passengers Over Time (1949-1960)")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.grid(True)
plt.show()