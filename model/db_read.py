import duckdb
import pandas as pd

def db_read(datapath: str) -> pd.DataFrame:
    df = pd.read_csv(datapath)
    return df


