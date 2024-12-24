import bcrypt
import sqlite3
from random import randbytes

#TODO: complete the functions via sqlite queries and bcrypt
#def register(username, passwd):
#def check_inbox(logged-in_user_id)

con = sqlite3.connect("mailing.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user(username VARCHAR(50), passwd VARBINARY(64), publickey VARBINARY(16))")

def register_nlogin():
    username = input("Enter username:\n")
    passwd = input("Enter password:\n").encode()
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    publickey = randbytes(16)
    cur.execute("INSERT INTO user VALUES (?, ?, ?)", (username, hashed, publickey))
    con.commit()
    res = cur.execute("SELECT * FROM user")
    print(res.fetchall())

register_login()

#    login()
