import sqlite3
import hashlib

# Create DB
conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

conn.commit()
conn.close()

# HASH PASSWORD
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# ADD USER
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

# CHECK LOGIN
def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hash_password(password)))
    data = c.fetchone()
    conn.close()
    return data