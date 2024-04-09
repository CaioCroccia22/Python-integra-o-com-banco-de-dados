import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'root',
    password = 'root',
    host = 'localhost',
    port = '5432',

)