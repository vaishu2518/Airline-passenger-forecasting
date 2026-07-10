import pandas as pd

df = pd.read_csv("AirPassengers.csv")

df["Year"] = range(1949, 1949 + len(df))

df_long = df.melt(id_vars="Year", var_name="Month", value_name="Passengers")

df_long["Date"] = pd.to_datetime(df_long["Year"].astype(str) + df_long["Month"], format="%Y%b")

df_long = df_long.sort_values("Date").reset_index(drop=True)

df_final = df_long[["Date", "Passengers"]]

df_final.to_csv("airpassengers_cleaned.csv", index=False)

print(df_final.head(15))
print("Total rows:", len(df_final))