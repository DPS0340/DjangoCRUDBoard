import psycopg2

import os

conn = psycopg2.connect(host=os.environ['DB_HOST'], port=os.environ['DB_PORT'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'])
cur = conn.cursor()
# cur.execute("DROP TABLE board_post CASCADE;")