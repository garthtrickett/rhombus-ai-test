import pandas as pd
import numpy as np
# Enable the new query planning option
import dask
import dateparser
dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd


# Now you can import dask.dataframe as dd

def infer_and_convert_dtypes(file_path, chunksize=10000, date_format=None):
    """
    Infers and converts data types in a CSV or Excel file.

    Args:
        file_path (str): Path to the CSV or Excel file.
        chunksize (int): Number of rows to read at a time.
        date_format (str): Date format to use for parsing dates.

    Returns:
        pandas.DataFrame: DataFrame with inferred and converted data types.
    """

    def try_convert_to_numeric(df, col):
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
        return df

    def try_convert_to_datetime(df, col):
        try:
            df[col] = df[col].apply(lambda x: dateparser.parse(x) if isinstance(x, str) else x)
        except ValueError:
            pass

        return df

    def try_convert_to_complex(df, col):
        try:
            df[col] = df[col].apply(lambda x: np.complex_(complex(x)) if isinstance(x, str) else x)
        except ValueError:
            pass
        return df

    def convert_chunk(df):
        for col in df.columns:
            if df[col].dtype == "object":
                df = try_convert_to_numeric(df, col)
                df = try_convert_to_datetime(df, col, date_format)
                df = try_convert_to_complex(df, col)

                # If less than 50% unique values, consider category
                if df[col].nunique().compute() / len(df) < 0.5:
                    df[col] = df[col].categorize()

        return df

    # Read the file and convert each chunk
    if file_path.endswith(".csv"):
        df = dd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        df = dd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    df = convert_chunk(df).compute()

    return df


