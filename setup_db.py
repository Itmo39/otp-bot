import sqlite3

conn = sqlite3.connect('otps.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE otps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone_number TEXT NOT NULL,
    otp_code TEXT NOT NULL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
