import sqlite3

con = sqlite3.connect("mailing.db")
cur = con.cursor()

res = cur.execute("SELECT * FROM user")
print(res.fetchall())
