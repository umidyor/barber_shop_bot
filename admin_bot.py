from inlines import delete_buttons_m
from env import ADMIN_ID,Main_admin
import sqlite3
import json
def load_data():
    try:
        with open('users_data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    return existing_data

def users_infos_bot(update,context):
    existing_data = load_data()
    total_ids = len(existing_data)
    update.message.reply_text(text=f"Jami botimizdan foydalanganlar soni {total_ids}ta👌")

def clear_all_data(update,context):
    if update.message.from_user.id in ADMIN_ID:
        update.message.reply_text(text="Ishonchigzi komilmi?Bugungi buyurtmalar tugadimi?",reply_markup=delete_buttons_m)
    else:
        pass

def orders_by_users(update,context):

    connection = sqlite3.connect('barber_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM user_info')
    all_data = cursor.fetchall()
    connection.close()
    if update.message.from_user.id in ADMIN_ID:
        for row in all_data:
            update.message.reply_text(text=f"<strong>Foydalanuvchi databasedagi idsi</strong>:{row[0]}\n"
                                            f"<strong>Foydalanuvchi telegram idsi</strong>:{row[1]}\n"
                                            f"<strong>Foydalanuvchi telegramdagi usenamesi</strong>:@{row[2]}\n"
                                            f"<strong>Foydalanuvchining ismi</strong>:{row[3]}\n"
                                            f"<strong>Foydalanuvchining telefon raqami</strong>:{row[4]}\n"
                                            f"<strong>Foydalanuvchining band qilgan vaqti</strong>:{row[5]}",parse_mode="html")
    else:
        pass