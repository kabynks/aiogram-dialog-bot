import time
from db_read import db_read, db_read_duckdb_in_memory, db_read_duckdb_persistent_load, db_read_duckdb_persistent_query

datapath = 'result.csv'
db_path = '../database/database.duckdb'

def test_loading_and_querying_speed():
    # Измеряем время загрузки данных в DuckDB (постоянное хранилище)
    start_time = time.time()
    db_read_duckdb_persistent_load(datapath, db_path)
    loading_time = time.time() - start_time
    print(f"DuckDB persistent storage loading time: {loading_time:.4f} seconds")

    # Измеряем время выборки данных из DuckDB (постоянное хранилище)
    start_time = time.time()
    df_duckdb_persistent = db_read_duckdb_persistent_query(db_path)
    querying_time = time.time() - start_time
    print(f"DuckDB persistent storage querying time: {querying_time:.4f} seconds")

    # Измеряем время чтения данных из CSV
    start_time = time.time()
    df_csv = db_read(datapath)
    csv_time = time.time() - start_time
    print(f"CSV read time: {csv_time:.4f} seconds")

    # Измеряем время чтения данных из DuckDB в памяти
    start_time = time.time()
    df_duckdb_in_memory = db_read_duckdb_in_memory(datapath)
    duckdb_in_memory_time = time.time() - start_time
    print(f"DuckDB in memory read time: {duckdb_in_memory_time:.4f} seconds")

if __name__ == "__main__":
    test_loading_and_querying_speed()
