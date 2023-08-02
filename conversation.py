# telegramfrom telegram import Update
# from telegram.ext import ConversationHandler, CallbackContext
# import re,sqlite3
# from inlines import change_data_buttons_m
# from env import Main_admin
# NAME, PHONE_NUMBER = range(2)
#
# def validate_phone_number(text):
#     return bool(re.match(r'^\+998\d{9}$', text))
#
# def start_cons(update: Update, context: CallbackContext) -> int:
#     time_=update.message.text
#     context.user_data["time"]=time_
#     user_id = update.message.from_user.id
#     context.user_data["user_id"] = user_id
#     context.user_data["username"] = update.message.from_user.username
#     update.message.reply_text("To'xtatish uchun /cancel buyrug'idan foydalaning")
#     update.message.reply_text("Ismingizni kiriting:")
#     return NAME
#
# def get_name(update: Update, context: CallbackContext) -> int:
#     context.user_data['name'] = update.message.text
#     update.message.reply_text("Telefon raqamingizni kiriting:")
#     return PHONE_NUMBER
#
# def check_user_id_exists(user_id):
#     conn = sqlite3.connect('barber_database.db')
#     c = conn.cursor()
#
#     # Check if the user_id exists in the 'user_info' table
#     c.execute(f'''SELECT * FROM user_info WHERE user_id = {user_id}''' )
#     exists = c.fetchone() is not None
#
#     conn.close()
#
#     return exists
#
# def check_time_slot_exists(time_slot):
#     conn = sqlite3.connect('barber_database.db')
#     c = conn.cursor()
#
#     # Check if the time_slot exists in the 'user_info' table
#     c.execute(f'''SELECT * FROM user_info WHERE time = ?''', (time_slot,))
#     exists = c.fetchone() is not None
#
#     conn.close()
#
#     return exists
#
#
#
# def get_phone_number(update: Update, context: CallbackContext) -> int:
#     phone_number = update.message.text
#     if validate_phone_number(phone_number):
#         context.user_data['phone_number'] = phone_number
#         infos=("<i><strong>Sizning ma'lumotlaringiz</strong></i>:\n\n"
#                                   f"<strong>Order time</strong>: {context.user_data['time']}\n"
#                                   f"<strong>User id</strong>: {context.user_data['user_id']}\n"
#                                   f"<strong>Username</strong>: @{context.user_data['username']}\n"
#                                   f"<strong>Ism</strong>: {context.user_data['name']}\n"
#                                   f"<strong>Telefon raqam</strong>: {context.user_data['phone_number']}\n"
#                                   f"<em>Malumotlar olindi! Raxmat😊</em>")
#         update.message.reply_text(text=infos,parse_mode="html")
#         context.bot.send_message(chat_id=Main_admin,text=f"Bizda yangi buyurtmachi bor⏰😮😮\n\n{infos}",parse_mode="html")
#
#
#         if check_time_slot_exists(update.message.text):
#             conn = sqlite3.connect('barber_database.db')
#             c = conn.cursor()
#             update.message.reply_text("Afsuski bu vaqt allaqachon band qilingan😒")
#             a = c.execute(f'''SELECT user_id FROM user_info WHERE time=="{context.user_data["time"]}"''')
#             print(update.message.text)
#             conn.commit()
#             conn.close()
#
#         if check_user_id_exists(update.message.from_user.id):
#             conn = sqlite3.connect('barber_database.db')
#             c = conn.cursor()
#             update.message.reply_text("Sizning ma'lumotlaringiz allaqachon qo'shilgan.Balkim boshqa vaqtgadir🤷Shu sababli siz /change_data buyrug'idan foydalanib, ma'lumotlaringizni o'zgartiring.")
#             a=c.execute(f'''SELECT user_id FROM user_info WHERE user_id=={update.message.from_user.id}''')
#             conn.commit()
#             conn.close()
#
#         else:
#             conn = sqlite3.connect('barber_database.db')
#             c=conn.cursor()
#         # Insert the new user information into the 'user_info' table
#             c.execute('''INSERT INTO user_info (user_id, username, name, phone_number, time)
#                             VALUES (?, ?, ?, ?, ?)''', (context.user_data['user_id'], context.user_data['username'], context.user_data['name'], context.user_data['phone_number'], context.user_data['time']))
#             update.message.reply_text(f"Hurmatli {update.message.from_user.full_name}!Agarda ma'lumot topshirishda xatolikka yo'l qo'ygan bo'lsangiz yoki uni o'zgartirmoqchi bo'lsangiz,ushbu tugmachalardan birini tanlang🤔",reply_markup=change_data_buttons_m)
#             conn.commit()
#             conn.close()
#
#         return ConversationHandler.END
#     else:
#         update.message.reply_text("Noto'g'ri telefon raqam formati. Iltimos, to'g'ri formatda kiriting. (Masalan, +998901234567)")
#         return PHONE_NUMBER
#
# def cancel(update: Update, context: CallbackContext) -> int:
#     update.message.reply_text("So'rov bekor qilindi.")
#     return ConversationHandler.END

from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
import re, sqlite3
from inlines import change_data_buttons_m
from env import Main_admin

NAME, PHONE_NUMBER = range(2)

def validate_phone_number(text):
    return bool(re.match(r'^\+998\d{9}$', text))

def start_cons(update: Update, context: CallbackContext) -> int:
    time_ = update.message.text
    context.user_data["time"] = time_
    user_id = update.message.from_user.id
    context.user_data["user_id"] = user_id
    context.user_data["username"] = update.message.from_user.username
    update.message.reply_text("To'xtatish uchun /cancel buyrug'idan foydalaning")
    update.message.reply_text("Ismingizni kiriting:")
    return NAME

def get_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    update.message.reply_text("Telefon raqamingizni kiriting:")
    return PHONE_NUMBER

def check_user_id_exists(user_id):
    conn = sqlite3.connect('barber_database.db')
    c = conn.cursor()

    # Check if the user_id exists in the 'user_info' table
    c.execute(f'''SELECT * FROM user_info WHERE user_id = ?''', (user_id,))
    exists = c.fetchone() is not None

    conn.close()

    return exists

def git_add(update,context,tekst):
    context.bot.send_message(chat_id=Main_admin,text=tekst)

def check_time_slot_exists(time_slot):
    conn = sqlite3.connect('barber_database.db')
    c = conn.cursor()

    # Check if the time_slot exists in the 'user_info' table
    c.execute(f'''SELECT * FROM user_info WHERE time = ?''', (time_slot,))
    exists = c.fetchone() is not None

    conn.close()

    return exists

def get_phone_number(update: Update, context: CallbackContext) -> int:
    phone_number = update.message.text
    if validate_phone_number(phone_number):
        context.user_data['phone_number'] = phone_number
        global infos
        infos = "<i><strong>Sizning ma'lumotlaringiz</strong></i>:\n\n" \
                f"<strong>Order time</strong>: {context.user_data['time']}\n" \
                f"<strong>User id</strong>: {context.user_data['user_id']}\n" \
                f"<strong>Username</strong>: @{context.user_data['username']}\n" \
                f"<strong>Ism</strong>: {context.user_data['name']}\n" \
                f"<strong>Telefon raqam</strong>: {context.user_data['phone_number']}\n" \
                f"<em>Malumotlar olindi! Raxmat😊</em>"
        update.message.reply_text(text=infos, parse_mode="html")
        # context.bot.send_message(chat_id=Main_admin, text=f"Bizda yangi buyurtmachi bor⏰😮😮\n\n{infos}",
        #                          parse_mode="html")
        if check_user_id_exists(context.user_data['user_id']):
            update.message.reply_text(
                "Sizning ma'lumotlaringiz allaqachon qo'shilgan. Balki boshqa vaqtgadir🤷 Shu sababli siz /change_data buyrug'idan foydalanib, ma'lumotlaringizni o'zgartiring.")

        elif check_time_slot_exists(context.user_data['time']):
            update.message.reply_text("Afsuski bu vaqt allaqachon band qilingan😒Ushbu buyruqdan foydalanib ma'lumotlaringizni o'chiring va qayta yozing👉 /change_data")
            pass
        else:
            conn = sqlite3.connect('barber_database.db')
            c = conn.cursor()
            # Insert the new user information into the 'user_info' table
            c.execute('''INSERT INTO user_info (user_id, username, name, phone_number, time)
                            VALUES (?, ?, ?, ?, ?)''', (context.user_data['user_id'], context.user_data['username'],
                                                       context.user_data['name'], context.user_data['phone_number'],
                                                       context.user_data['time']))
            update.message.reply_text(
                f"Hurmatli {update.message.from_user.full_name}! Agarda ma'lumot topshirishda xatolikka yo'l qo'ygan bo'lsangiz yoki uni o'zgartirmoqchi bo'lsangiz,ushbu tugmachalardan birini tanlang🤔",
                reply_markup=change_data_buttons_m)
            context.bot.send_message(chat_id=Main_admin, text=f"Bizda yangi buyurtmachi bor⏰😮😮\n\n{infos}",
                                     parse_mode="html")
            conn.commit()
            conn.close()

        return ConversationHandler.END
    else:
        update.message.reply_text("Noto'g'ri telefon raqam formati. Iltimos, to'g'ri formatda kiriting. (Masalan, +998901234567)")
        return PHONE_NUMBER

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("So'rov bekor qilindi.")
    return ConversationHandler.END



