from telegram import KeyboardButton,ReplyKeyboardRemove,ReplyKeyboardMarkup

before_buttons=[
    [KeyboardButton("9:00-9:40"),KeyboardButton("9:45-10:25")],
    [KeyboardButton("10:30-11:10"),KeyboardButton("11:55-12:35")]
]
before_buttons_m=ReplyKeyboardMarkup(before_buttons,resize_keyboard=True,one_time_keyboard=True)

after_buttons=[
    [KeyboardButton("13:00-13:40"),KeyboardButton("13:55-14:35")],
    [KeyboardButton("15:30-17:10"),KeyboardButton("17:15-18:00")],
    [KeyboardButton("18:05-18:50"),KeyboardButton("18:55-19:40")]
]

after_buttons_m=ReplyKeyboardMarkup(after_buttons,resize_keyboard=True,one_time_keyboard=True)

