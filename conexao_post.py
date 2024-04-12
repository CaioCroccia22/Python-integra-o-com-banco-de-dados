import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = 'root',
    host = 'localhost',
    port = '5432',
)