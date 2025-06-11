import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Load CSVs into DataFrames
orders_df = pd.read_csv('d:\dbt\dbt_dev_project\orders_raw.csv')
orders_df.columns = [col.upper() for col in orders_df.columns]

customers_df = pd.read_csv('d:\dbt\dbt_dev_project\customers_raw.csv')
customers_df.columns = [col.upper() for col in customers_df.columns]

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='awaissaleem',
    password='Addo@123@123@123',
    account='fbwmida-ft38234',  # like "xy12345.ap-southeast-1"
    warehouse='COMPUTE_WH',
    database='DAP_DB',
    schema='raw'
)

# Load orders
success1, nchunks1, nrows1, _ = write_pandas(conn, orders_df, 'ORDERS_RAW')
print(f"Loaded {nrows1} rows into ORDERS_RAW.")

# Load customers
success2, nchunks2, nrows2, _ = write_pandas(conn, customers_df, 'CUSTOMERS_RAW')
print(f"Loaded {nrows2} rows into CUSTOMERS_RAW.")