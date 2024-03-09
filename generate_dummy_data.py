import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import string

# Number of rows in the DataFrame
num_rows = 100

# Generate random data
object_data = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(num_rows)]
int64_data = np.random.randint(low=1, high=100, size=num_rows)
float64_data = np.random.uniform(low=0.0, high=100.0, size=num_rows)
bool_data = np.random.choice([True, False], size=num_rows)
datetime64_data = [datetime.now() - timedelta(days=x) for x in range(num_rows)]
category_data = pd.Categorical(np.random.choice(['Category1', 'Category2', 'Category3'], size=num_rows))
complex_data = [complex(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(num_rows)]

# Create a DataFrame
df = pd.DataFrame({
    "ObjectColumn": object_data,
    "Int64Column": int64_data,
    "Float64Column": float64_data,
    "BoolColumn": bool_data,
    "Datetime64Column": datetime64_data,
    "CategoryColumn": category_data,
    "ComplexColumn": complex_data
})

# Write DataFrame to CSV
df.to_csv("random_data_types.csv", index=False)
