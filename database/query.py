from db_config import get_connection

def fetch_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products ORDER BY timestamp DESC;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    fetch_all_products()
