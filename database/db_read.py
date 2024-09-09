import duckdb
import pandas as pd


def db_read_duckdb_in_memory(datapath: str) -> pd.DataFrame:
    """Чтение данных из CSV через DuckDB в памяти"""
    conn = duckdb.connect()
    df = conn.execute(f"SELECT * FROM read_csv_auto('{datapath}')").df()
    conn.close()
    return df

def db_read_duckdb_persistent_load(datapath: str, db_path: str) -> None:
    """Загрузка данных в таблицу DuckDB"""
    conn = duckdb.connect(db_path)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS results AS 
        SELECT * FROM read_csv_auto('{datapath}')
    """)
    conn.close()

def db_read_duckdb_persistent_query(db_path: str) -> pd.DataFrame:
    """Выборка данных из таблицы DuckDB"""
    conn = duckdb.connect(db_path)
    df = conn.execute("SELECT * FROM results").df()
    conn.close()
    return df