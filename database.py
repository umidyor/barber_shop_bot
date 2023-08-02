# import sqlite3
#
# def create_database():
#     conn = sqlite3.connect('barber_database.db')
#     c = conn.cursor()
#
#     # Create the 'user_info' table if it doesn't exist
#     c.execute('''CREATE TABLE IF NOT EXISTS user_info (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id INTEGER,
#                     username TEXT,
#                     name TEXT,
#                     phone_number TEXT,
#                     time TEXT
#                 )''')
#
#     conn.commit()
#     conn.close()
#
# if __name__ == "__main__":
#     create_database()
# def add_user_info(user_id, username, name, phone_number, time):
#     conn = sqlite3.connect('barber_database.db')
#     c = conn.cursor()
#
#     # Insert the new user information into the 'user_info' table
#     c.execute('''INSERT INTO user_info (user_id, username, name, phone_number, time)
#                  VALUES (?, ?, ?, ?, ?)''', (user_id, username, name, phone_number, time))
#
#     conn.commit()
#     conn.close()