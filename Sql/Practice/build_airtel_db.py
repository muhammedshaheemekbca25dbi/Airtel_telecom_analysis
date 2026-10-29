from pathlib import Path
import sqlite3

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / 'data' / 'airtel.db'
CSV_DIR = ROOT / 'data' / 'Raw' / 'Tables'


def main() -> None:
    if not CSV_DIR.exists():
        raise FileNotFoundError(f'CSV directory not found: {CSV_DIR}')

    conn = sqlite3.connect(DB_PATH)
    try:
        for csv_path in sorted(CSV_DIR.glob('*.csv')):
            table_name = csv_path.stem
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f'Loaded {table_name}: {len(df)} rows')
    finally:
        conn.close()

    print(f'Created database: {DB_PATH}')


if __name__ == '__main__':
    main()