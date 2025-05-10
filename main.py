from telebot import TeleBot, types

TOKEN = "7452506330:AAH_6c23NH0PIDB9mi9BnSUBFOGs9Q-yDwk"
bot = TeleBot(TOKEN)

regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg'ona", "Namangan", 
    "Andijon", "Xorazm", "Navoiy", "Jizzax", "Sirdaryo", 
    "Qashqadaryo", "Surxondaryo"
]

menu_items = [
    "Купон 1739 - Чизбургер + Напиток - 5.10₽",
    "Купон 1740 - 2 Шефбургер Де Люкс + 10 Наггетс + 2 Напитка - 19.50₽",
    "Купон 1741 - Чизбургер Де Люкс + Байтсы + sous - 8.80₽",
    "Купон 1742 - Шефбургер + Напиток - 6.90₽",
    "Купон 1743 - Шефбургер Джуниор + 6 Наггетс + sous - 8.80₽",
    "Купон 1744 - Наггетсы 6 шт. - 4.40₽",
    "Купон 1745 - Баскет  + 2 Напитка - 21.50₽",
    "Купон 1746 - Твистер + Напиток - 7.00₽",
    "Купон 1747 - 3 Стрипса + sous - 4.50₽",
    "Купон 1748 - 3 sous - 1.80₽",
    "Купон 1749 - Кофе 0.2 + Морковный торт - 6.00₽",
    "Купон 1750 - Капучино 0.3 - 2.99₽"
]

payment_methods = ["Karta", "Kuryerga naxt"]

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "Assalomu alaykum. Men KFC yetkazib berish xizmati botiman!"
    )
    bot.send_message(
        message.chat.id, 
        "Iltimos, qaysi viloyatdan ekanligingizni tanlang.",
        reply_markup=create_region_markup()
    )

def create_region_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(region) for region in regions]
    markup.add(*buttons)
    return markup

@bot.message_handler(func=lambda message: message.text in regions)
def ask_phone_number(message):
    user_data[message.chat.id] = {
        'region': message.text,
        'orders': []
    }
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    contact_button = types.KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
    markup.add(contact_button)
    bot.send_message(
        message.chat.id, 
        "Rahmat! Endi telefon raqamingizni yuboring.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['contact'])
def register_user(message):
    if message.contact:
        user_data[message.chat.id]['phone'] = message.contact.phone_number
        bot.send_message(message.chat.id, "Registratsiya yakunlandi!")
        show_main_menu(message)

def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("Buyurtma berish", "Buyurtmalarini ko'rish")
    markup.add("Sozlamalar")
    bot.send_message(message.chat.id, "Quyidagilardan birini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Buyurtma berish")
def ask_address(message):
    msg = bot.send_message(message.chat.id, "Iltimos, manzilingizni kiriting:")
    bot.register_next_step_handler(msg, show_menu_with_image)

def show_menu_with_image(message):
    user_data[message.chat.id]['address'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(*menu_items)
    image_url = "https://static2.skidka.by/5f/88/66/0_coupons-kfc-by150322-page-0001_5f88669b.jpg"
    bot.send_photo(
        message.chat.id, 
        image_url, 
        caption="Buyurtma uchun mahsulotni tanlang:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text in menu_items)
def handle_order_selection(message):
    selected_item = message.text
    user_data[message.chat.id]['orders'].append(selected_item)
    bot.send_message(message.chat.id, f"{selected_item} buyurtmangiz qabul qilindi.")
    # To'lov usullarini ko'rsatish
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(*payment_methods)
    bot.send_message(message.chat.id, "Iltimos, to'lov turini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in payment_methods)
def handle_payment(message):
    tolov = message.text
    bot.send_message(
        message.chat.id,
        f"To'lov turi: {tolov}. Buyurtmangiz 30 daqiqada yetkaziladi. Rahmat! 😊"
    )
    show_main_menu(message)

@bot.message_handler(func=lambda message: message.text == "Buyurtmalarini ko'rish")
def show_orders(message):
    orders = user_data.get(message.chat.id, {}).get('orders', [])
    if orders:
        order_list = "\n".join(f"🍟 {item}" for item in orders)
        bot.send_message(message.chat.id, f"Buyurtmalar tarixi:\n{order_list}")
    else:
        bot.send_message(message.chat.id, "Buyurtmalaringiz yo‘q.")

@bot.message_handler(func=lambda message: message.text == "Sozlamalar")
def settings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("Viloyatni o'zgartirish", "Bosh menyuga qaytish")
    bot.send_message(message.chat.id, "Sozlamalar:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Viloyatni o'zgartirish")
def change_region(message):
    bot.send_message(message.chat.id, "Yangi viloyatni tanlang:", reply_markup=create_region_markup())

@bot.message_handler(func=lambda message: message.text == "Bosh menyuga qaytish")
def back_to_main(message):
    show_main_menu(message)

if __name__ == "__main__":
    bot.polling()
