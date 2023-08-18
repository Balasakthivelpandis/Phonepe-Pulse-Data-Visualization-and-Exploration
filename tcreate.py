import sqlite3
conn = sqlite3.connect("phonepe.db")
cursor = conn.cursor()


sql = """
      CREATE TABLE IF NOT EXISTS map_user (States TEXT,
      Transaction_Year INTEGER,
      Quarters INTEGER,
      District TEXT,
      RegisteredUsers INTEGER
      )"""

cursor.execute(sql)
print("file created")

conn.commit()
conn.close()








