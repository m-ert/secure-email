import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
"""
cur.execute("CREATE TABLE user(uname, passwd)")

con.commit()
"""
name = "name2"
password = "passwrod5"
cur.execute("INSERT INTO user VALUES (?, ?)", (name, password))
res = cur.execute("SELECT * FROM user")
print(res.fetchall())
