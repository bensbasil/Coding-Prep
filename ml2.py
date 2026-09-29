import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# 1. Read the CSV
df = pd.read_csv("house_data.csv")

print(df)


# 2. Separate input features (X) and target (y)

X = df[["area", "bedrooms"]]
y = df["price"]


# 3. Split into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4. Create the Linear Regression model

model = LinearRegression()


# 5. Train the model

model.fit(X_train, y_train)


# 6. Make predictions

y_pred = model.predict(X_test)


# 7. Evaluate the model

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test.values)
print("MSE:", mse)
print("R2 Score:", r2)