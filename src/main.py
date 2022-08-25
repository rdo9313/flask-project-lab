import psycopg2

conn = psycopg2.connect(database="restaurants", user="ryando")
cursor = conn.cursor()
cursor.execute("SELECT * FROM restaurants LIMIT 10;")
print(cursor.fetchall())
