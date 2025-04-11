import pandas as pd
import matplotlib.pyplot as plt
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

crop_variety = input("Enter the crop variety you want predictions for: ")
state = input("Enter the state: ")
market = input("Enter the market: ")

api_url = f"http://127.0.0.1:5000/request?commodity={crop_variety}&state={state}&market={market}"

try:
    response = requests.get(api_url)
    live_data = response.json()

    if isinstance(live_data, list) and len(live_data) > 0:
        live_df = pd.DataFrame(live_data)

        # Ensure numeric columns are properly formatted
        live_df['Min Prize'] = pd.to_numeric(live_df['Min Prize'], errors='coerce')
        live_df['Max Prize'] = pd.to_numeric(live_df['Max Prize'], errors='coerce')
        live_df['Model Prize'] = pd.to_numeric(live_df['Model Prize'], errors='coerce')

        live_df['Date'] = pd.to_datetime(live_df['Date'], format='%d %b %Y')

        live_df.rename(columns={
            'Min Prize': 'Minimum Prices',
            'Max Prize': 'Maximum Prices',
            'Model Prize': 'Modal Prices'
        }, inplace=True)

    else:
        print(f"No live data available for {crop_variety} in {state}, {market}")
        exit()

except Exception as e:
    print(f"Error fetching live data: {e}")
    exit()

X = live_df[['Minimum Prices', 'Maximum Prices']]
y = live_df['Modal Prices']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error for {crop_variety}: {mse}")

predicted_prices = model.predict(X_scaled)

live_df['Predicted Prices'] = predicted_prices

average_prices = live_df.groupby('Date').agg({
    'Minimum Prices': 'mean',
    'Maximum Prices': 'mean',
    'Modal Prices': 'mean',
    'Predicted Prices': 'mean'
}).reset_index()

print(average_prices)

#Trend Chart with Averaged Prices
plt.figure(figsize=(10, 6))

# Plotting the average minimum prices
plt.plot(average_prices['Date'], average_prices['Minimum Prices'], marker='o', linestyle='-', color='green',
         linewidth=2, label='Avg. Minimum Prices')

# Plotting the average maximum prices
plt.plot(average_prices['Date'], average_prices['Maximum Prices'], marker='o', linestyle='-', color='red', linewidth=2,
         label='Avg. Maximum Prices')

# Plotting the average modal prices
plt.plot(average_prices['Date'], average_prices['Modal Prices'], marker='o', linestyle='-', color='blue', linewidth=2,
         label='Avg. Modal Prices')

# Plotting the average predicted prices
plt.plot(average_prices['Date'], average_prices['Predicted Prices'], marker='o', linestyle='--', color='orange',
         linewidth=2, label='Avg. Predicted Prices')

# Title and labels
plt.title(f"Average Price Trend for {crop_variety}", fontsize=16, fontweight='bold')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Average Price (₹ per Quintal)", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adding legend
plt.legend(fontsize=12)

# Additional styling
plt.tight_layout()
plt.show()