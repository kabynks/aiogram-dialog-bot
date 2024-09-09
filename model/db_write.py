import pandas as pd
import duckdb

def db_write(df:pd.DataFrame, datapath:str) -> None:
    df.to_csv(datapath, index=False)    

