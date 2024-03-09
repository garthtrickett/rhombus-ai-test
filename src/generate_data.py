# generate_data.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import string


def generate_data(num_rows=100, file_path="test.csv"):
    """
    Generates a DataFrame with random data and writes it to a CSV file.

    Args:
        num_rows (int): Number of rows in the DataFrame.
        file_path (str): Path to the CSV file to write.

    Returns:
        None
    """

    # Generate random data
    object_data = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(num_rows)]
    int64_data = np.random.randint(low=1, high=100, size=num_rows)
    float64_data = np.random.uniform(low=0.0, high=100.0, size=num_rows)
    bool_data = np.random.choice([True, False], size=num_rows)
    datetime64_data = [datetime.now() - timedelta(days=x % 365) for x in range(num_rows)]  # Modify this line
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
    df.to_csv(file_path, index=False)


def generate_known_data(num_rows=100, file_path="test.csv"):
    """
    Generates a DataFrame with known data and writes it to a CSV file.

    Args:
        num_rows (int): Number of rows in the DataFrame.
        file_path (str): Path to the CSV file to write.

    Returns:
        None
    """

    # Generate known data
    int64_data = [i for i in range(num_rows)]
    float64_data = [i * 0.1 for i in range(num_rows)]
    bool_data = [i % 2 == 0 for i in range(num_rows)]
    datetime64_data = [datetime.now() - timedelta(days=i % 365) for i in range(num_rows)]
    category_data = ['Category1' if i % 2 == 0 else 'Category2' for i in range(num_rows)]
    complex_data = [complex(i, i) for i in range(num_rows)]

    # Create a DataFrame
    df = pd.DataFrame({
        "Int64Column": int64_data,
        "Float64Column": float64_data,
        "BoolColumn": bool_data,
        "Datetime64Column": datetime64_data,
        "CategoryColumn": category_data,
        "ComplexColumn": complex_data
    })

    # Write DataFrame to CSV
    df.to_csv(file_path, index=False)

