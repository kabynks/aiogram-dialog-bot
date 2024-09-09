import duckdb

def create_table_and_load_data(csv_path: str, db_path: str) -> None:
    conn = duckdb.connect(db_path)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS results AS 
        SELECT * FROM read_csv_auto('{csv_path}')
    """)
    conn.close()


csv_path = '../model/result.csv'
db_path = '../database/database.duckdb'
create_table_and_load_data(csv_path, db_path)
