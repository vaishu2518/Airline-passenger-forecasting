import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv("airpassengers_cleaned.csv")

df = df.rename(columns={"Date": "ds", "Passengers": "y"})
df["ds"] = pd.to_datetime(df["ds"])

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=24, freq="ME")

forecast = model.predict(future)

fig1 = model.plot(forecast)
plt.title("Airline Passengers Forecast (Next 2 Years)")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.show()

fig2 = model.plot_components(forecast)
plt.show()

forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].to_csv("forecast_results.csv", index=False)

print("Forecasting done. Preview of predictions:")
print(forecast[["ds", "yhat"]].tail(24))