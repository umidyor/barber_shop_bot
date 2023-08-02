import sqlite3

from env import TOKEN, ADMIN_ID
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler
from telegram import BotCommand
from conversation import NAME, PHONE_NUMBER, start_cons, get_name, get_phone_number, cancel, check_user_id_exists
from inlines import inbuttons_m, time_select, change_my_data
from knbuttons import before_buttons, after_buttons
import admin_bot
import json




def start_command(update,context):
    if update.message.from_user.id in ADMIN_ID:
        update.message.reply_text(
            f"Assalomu aleykum!Hurmatli admin {update.message.from_user.full_name}😊Botimiz haqidagi ma'lumotlar uchun buyruqlar marhamat...\n"
            f"/users -> Jami botdan necha kishi foydalanagan?\n"
            f"/zakaslar -> Barcha foydalanuvchilarni bugungi zakaslari\n"
            f"/tozalash -> Bugungi ma'lumotlarni tozalash")

    else:
        update.message.reply_text(text=f"Salom hurmatli {update.message.from_user.full_name}! Ushbu botimiz orqali siz biror vaqtni band qilgan holda sartaroshxonamizga kelishingiz mumkin.\nJoy band qilish uchun👉 /register")
        existing_data =admin_bot.load_data()
        chat_id=update.message.from_user.id
        if chat_id in existing_data:
            pass
        else:
            # Get the bot ID
            bot_id = context.bot.id

            # Add the user's chat ID and bot ID to the existing data dictionary
            existing_data[chat_id] = bot_id

            # Write the updated data back to the JSON file
            with open('users_data.json', 'w') as file:
                json.dump(existing_data, file, indent=4)


def register(update, context):
    update.message.reply_text(
        f"Yaxshi!Unday bo'lsa ro'yxatdan o'ting va o'zingizga ma'qul vaqtni tanlang⏳...",
        reply_markup=inbuttons_m)
    con=sqlite3.connect("barber_database.db")
    c=con.cursor()

    c.execute("SELECT time  FROM user_info")
    all_data = c.fetchall()
    con.close()
    time_list=[]
    for i in all_data:
        time_list.append(i)

    # update.message.reply_text(f"Iltimos!Ushbu vaqtlar bizda band qilingan🙅.Ushbu vaqtlarni band qilishga urinmang‼️\nShulardan boshqa vaqtni band qiling✊:\n<strong>{[i for i in time_list]}</strong>",parse_mode="html")
    time_list = [i[0] for i in all_data]  # Extracting the first element from each tuple

    if not time_list:
        pass
    else:
        update.message.reply_text(
            f"Iltimos! Ushbu vaqtlar bizda band qilingan🙅. Ushbu vaqtlarni band qilishga urinmang‼️\nShulardan boshqa vaqtni band qiling✊:\n<strong>{[i for i in time_list]}</strong>",
            parse_mode="html")
    if check_user_id_exists(update.message.from_user.id):
        my_commands = [
            BotCommand("start", description="Botni ishga tushirish"),
            BotCommand('register',description="Joy band qilish"),
            BotCommand("change_data", description="Ma'lumotlarimni o'chirish"),
            BotCommand("cancel", description="Ro'yxatdan o'tishbi to'xtatish")
        ]
        context.bot.set_my_commands(my_commands)
    else:
        my_commands = [
            BotCommand("start", description="Botni ishga tushirish"),
            BotCommand('register', description="Joy band qilish"),
            BotCommand("cancel", description="Ro'yxatdan o'tishbi to'xtatish")
        ]
        context.bot.set_my_commands(my_commands)


def message_handler(update, context):
    text = update.message.text
    if text in before_buttons or after_buttons:
        start_cons(update, context)


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('register', register))
    dp.add_handler(CommandHandler('users',admin_bot.users_infos_bot))
    dp.add_handler(CommandHandler('zakaslar',admin_bot.orders_by_users))
    dp.add_handler(CommandHandler('tozalash',admin_bot.clear_all_data))
    dp.add_handler(CallbackQueryHandler(time_select))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, start_cons)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            PHONE_NUMBER: [MessageHandler(Filters.text & ~Filters.command, get_phone_number)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('change_data', change_my_data))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
