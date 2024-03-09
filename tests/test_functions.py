# test_functions.py

import pytest
import numpy as np  # Add this line
from src.generate_data import generate_data, generate_known_data
from src.infer_and_convert_dtypes import infer_and_convert_dtypes
import pandas as pd


def test_generate_known_data():
    generate_known_data(num_rows=100, file_path="test.csv")
    df = pd.read_csv("test.csv")
    assert df.shape[0] == 100


def test_infer_and_convert_dtypes():
    # Generate known data
    generate_known_data(num_rows=100, file_path="test.csv")

    # Infer and convert data types
    df = infer_and_convert_dtypes("test.csv")

    # Check that the number of rows is correct
    assert df.shape[0] == 100

    # Check that the data types have been correctly inferred and converted
    # assert df["ObjectColumn"].dtype == np.object
    assert df["Int64Column"].dtype == np.int64
    assert df["Float64Column"].dtype == np.float64
    assert df["BoolColumn"].dtype == np.bool_
    # assert df["Datetime64Column"].dtype == 'datetime64[ns]'
    assert df["CategoryColumn"].dtype.name == "category"
    # assert df["ComplexColumn"].dtype == np.complex128



def test_large_file_handling():
    # Generate a large DataFrame and write it to a CSV file
    generate_data(num_rows=100, file_path="test.csv")

    # Infer and convert data types
    df = infer_and_convert_dtypes("test.csv")

    # Assert that the DataFrame is not empty
    assert not df.empty


# Run the tests
pytest.main(["-v", "test_functions.py"])
