import pandas as pd

def infer_and_convert_dtypes(file_path):
    """
    Infers and converts data types in a CSV or Excel file.

    Args:
        file_path (str): Path to the CSV or Excel file.

    Returns:
        pandas.DataFrame: DataFrame with inferred and converted data types.
    """

    # Read the file into a DataFrame
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    # Infer data types for each column
    df = df.infer_objects()

    # Convert columns to more efficient data types where possible
    for col in df.columns:
        if df[col].dtype == "object":
            # Check if the column can be converted to category
            if df[col].nunique() / len(df) < 0.5:  # If less than 50% unique values, consider category
                df[col] = df[col].astype("category")

    return df

# Example usage
file_path = "your_data.csv"  # Replace with your actual file path
df = infer_and_convert_dtypes(file_path)
print(df.dtypes)
