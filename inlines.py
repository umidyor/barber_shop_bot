from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
from knbuttons import after_buttons_m,before_buttons_m
import sqlite3
from env import Main_admin
inbuttons=[
    [InlineKeyboardButton("Tushlikdan avval",callback_data="t_a")],
    [InlineKeyboardButton("Tushlikdan keyin",callback_data="t_k")]
]
inbuttons_m=InlineKeyboardMarkup(inbuttons)


delete_buttons=[
    [InlineKeyboardButton("Ha✅",callback_data="yes"),InlineKeyboardButton("Yo'q!Hozir emas❌",callback_data="no")]
]
delete_buttons_m=InlineKeyboardMarkup(delete_buttons)
change_data_buttons=[
    [InlineKeyboardButton("Ma'lumotlarni qayta yozaman",callback_data="change_data")],
    [InlineKeyboardButton("Yo'q!Hammasi to'g'ri",callback_data="not")]
]
change_data_buttons_m=InlineKeyboardMarkup(change_data_buttons)

def time_select(update,context):
    query=update.callback_query
    chat_id = query.message.chat_id
    if query.data=="t_a":
        context.bot.send_message(chat_id=chat_id,text="Ushbu vaqt oralig'idan birini tanlang",reply_markup=before_buttons_m)
    if query.data=="t_k":
        context.bot.send_message(chat_id=chat_id, text="Ushbu vaqt oralig'idan birini tanlang",
                                 reply_markup=after_buttons_m)
    if query.data=="change_data":

        conn = sqlite3.connect('barber_database.db')
        c = conn.cursor()

        # Delete the user with the specified user_id from the 'user_info' table
        c.execute(f'''DELETE FROM user_info WHERE user_id = {chat_id}''')

        conn.commit()
        conn.close()
        query.message.edit_text(text="Sizning barcha ma'lumotlaringiz o'chirildi.Iltimos, qaytadan ro'yxatdan o'ting va biror vaqtni band qiling👉 /register")

    if query.data=="not":
        query.message.edit_text(text="Sizning ma'lumotlaringiz adminga yuborildi va sizni sartaroshxonamizda kerakli vaqtda kutamiz😊\nLokatsiyamiz📍👇")
        context.bot.send_location(chat_id=update.effective_chat.id,latitude=41.43794640267001,longitude=69.53605186729683)
    if query.data=="yes":

        con=sqlite3.connect("barber_database.db")
        c=con.cursor()

        c.execute("DELETE FROM user_info")

        con.commit()
        con.close()
        query.message.edit_text(text="Hurmatli admin!Agarda bugungi ish kuni tugagan bo'lsa sizning barcha buyurtma ma'lumotlari muvaffaqiyatli o'chirildi")
    if query.data=="no":
        query.message.edit_text(text="Yaxshi!Ammo unutmang, ish vaqti tugagandan so'ng barcha ma'lumotlarni tozalash kerak.Sizdan shunchaki bittagina harakat😊")

def change_my_data(update,context):
    update.message.reply_text(text="Marhamat!Ma'lumotingizni o'chirib, qayta jo'nating😉",reply_markup=change_data_buttons_m)
