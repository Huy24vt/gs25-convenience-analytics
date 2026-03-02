import pandas as pd
from pathlib import Path

def load_data(data_dir: str):
    \"\"\"Load convenience store dataset from CSV folder.

    Expected files in data_dir:
      - stores.csv
      - products.csv
      - customers.csv
      - transactions.csv
      - transaction_lines.csv
    \"\"\"
    d = Path(data_dir)

    stores = pd.read_csv(d / "stores.csv")
    products = pd.read_csv(d / "products.csv")
    customers = pd.read_csv(d / "customers.csv")
    transactions = pd.read_csv(d / "transactions.csv")
    lines = pd.read_csv(d / "transaction_lines.csv")

    # Parse datetime
    transactions["datetime"] = pd.to_datetime(transactions["datetime"])

    return {
        "stores": stores,
        "products": products,
        "customers": customers,
        "transactions": transactions,
        "lines": lines,
    }
