import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname = "ebay_db",
        user = "ebay_user",
        password = "pakistan",
        host = "localhost",
        port = "5432"
    )

