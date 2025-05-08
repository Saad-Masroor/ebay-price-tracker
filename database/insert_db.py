import pandas as pd
from .db_config import get_connection

def insert_data(csv_path):
    df = pd.read_csv(csv_path)

    insert_query = """
    INSERT INTO PRODUCTS (title, price, link_of_product, condition_of_product, shipping, seller_info)
    VALUES (%s,%s,%s,%s,%s,%s)
    ON CONFLICT (link_of_product) DO NOTHING -- AVOID INSERTING DUPLICATES

    """

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            row['title'],
            row['price'],
            row['link'],
            row.get('condition'),
            row.get('shipping'),
            row.get('seller_info')
        ))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted {len(df)} rows into the database")

if __name__ == "__main__":
    insert_data("data/cleaned_ebay_data.csv")