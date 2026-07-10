# Airline Passenger Forecasting

A time series forecasting project that predicts future airline passenger 
demand using Facebook Prophet, based on the classic 1949-1960 
AirPassengers dataset.

## What it does
- Loads and reshapes historical monthly passenger data into a proper time series
- Visualizes the historical trend (1949-1960)
- Builds a forecasting model using Facebook Prophet
- Predicts passenger numbers for the next 2 years with confidence intervals
- Breaks down the forecast into trend and yearly seasonality components

## Key Insight
Air travel demand shows a consistent upward trend year over year, with 
strong seasonality — passenger numbers peak every July (summer travel) 
and dip every November.

## Tech Stack
- Python
- Pandas
- Facebook Prophet
- Matplotlib

## Files
- `forecasting.py` - reshapes raw data into a clean time series
- `plot_trend.py` - visualizes the historical trend
- `forecast_model.py` - builds the Prophet model and generates forecasts
- `airpassengers_cleaned.csv` - cleaned time series data
- `forecast_results.csv` - forecasted values with confidence intervals

## How to run
1. Install dependencies: `pip install pandas prophet matplotlib`
2. Run `forecasting.py` to prepare the data
3. Run `plot_trend.py` to visualize the historical trend
4. Run `forecast_model.py` to generate and view the 2-year forecast

## Sample Output
The model successfully forecasts passenger demand 24 months into the 
future, capturing both the long-term growth trend and the repeating 
seasonal pattern in air travel.
