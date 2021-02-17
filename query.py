import psycopg2

import os

conn = psycopg2.connect(host=os.environ['DB_HOST'], port=os.environ['DB_PORT'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'])
conn.autocommit = True
cur = conn.cursor()
cur.execute('SELECT datname FROM pg_database WHERE datistemplate = false;')
print(cur.fetchall())
cur.execute('drop database ebdb;')
# cur.execute("DROP TABLE board_post CASCADE;")
# cur.execute("select 'drop table "' || tablename || '" cascade;' from pg_tables;")