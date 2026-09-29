import pandas as pd
import numpy as np

# Set a seed so the random numbers are the same every time you run it
np.random.seed(42)

# Generate 100 rows of random data
num_houses = 100

# 1. Random area between 500 and 3500 sq ft
area = np.random.randint(500, 3500, size=num_houses)

# 2. Random number of bedrooms between 1 and 5
bedrooms = np.random.randint(1, 6, size=num_houses)

# 3. Create a realistic price based on area and bedrooms + some random noise
price = 50000 + (area * 150) + (bedrooms * 25000) + np.random.randint(-20000, 20000, size=num_houses)

# Combine into a DataFrame
df = pd.DataFrame({
    'area': area,
    'bedrooms': bedrooms,
    'price': price
})

# Save it as "house.data" (which is just a CSV format)
df.to_csv("house.data", index=False)

print("house.data created successfully with 100 rows!")
print(df.head()) # Preview the first 5 rows
