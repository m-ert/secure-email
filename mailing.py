import bcrypt
import sqlite3
from random import randbytes

#TODO: complete the functions via sqlite queries and bcrypt
#add requirements.txt
#maybe add some try catch blocks; user exists, wrong password, etc.

#def register(username, passwd):
#def check_inbox(logged-in_user_id)

con = sqlite3.connect("mailing.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user(username VARCHAR(50), passwd VARBINARY(64), publickey VARBINARY(16))")
con.commit()

username = None
passwd = None


def register_nlogin():
    username = input("Enter username:\n")
    passwd = input("Enter password:\n")
    hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    publickey = randbytes(16)
    cur.execute("INSERT INTO user (username, passwd, publickey) VALUES (?, ?, ?)", (username, hashed, publickey))
    con.commit()
    print("Registered Successfully!")
    login(username, passwd)


def login(uname, password):
    global username, passwd
    cur.execute("SELECT passwd FROM user WHERE username = ?", (uname,))
    result = cur.fetchone()
    if bcrypt.checkpw(password.encode('utf-8'), result[0]):
        username = uname
        print("Logged In Successfully!")
        return True
    else:
        print("Login Failed :(")
        return False

#***
register_nlogin()
print(f"Current logged-in user: {username}")
#***


