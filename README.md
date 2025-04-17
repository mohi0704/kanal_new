Botni ishga tushirish uchun kerakli bog'liqliklarni o'rnatish va Telegram bot tokenini sozlash zarur.

Talablar
Python 3.x

pyTelegramBotAPI kutubxonasi (Telegram API bilan ishlash uchun)

O'rnatish bosqichlari
Repoyni klonlang yoki yangi fayl yaratib botni yozing.

Zarur kutubxonalarni o'rnating:

bash
Копировать
Редактировать
pip install pyTelegramBotAPI
Skriptda TOKEN o'zgaruvchisini o'zingizning Telegram bot tokeningiz bilan almashtiring.

python
Копировать
Редактировать
TOKEN = "YOUR_BOT_TOKEN"
Python skriptini ishga tushiring:

bash
Копировать
Редактировать
python bot.py
Bot polling usulida ishlay boshlaydi va foydalanuvchilar bilan muloqot qilishga tayyor bo'ladi.

Bot qanday ishlaydi
Start komandasi:

Foydalanuvchi /start komandasini yuborganida, bot salomlashadi va foydalanuvchidan viloyatini tanlashni so'raydi.

Viloyatni tanlash:

Bot foydalanuvchiga viloyatlar ro'yxatini taqdim etadi. Foydalanuvchi viloyatni tanlaganidan so'ng, bot telefon raqamini so'raydi.

Telefon raqamini so'rash:

Viloyat tanlangach, bot foydalanuvchidan telefon raqamini yuborishni so'raydi.

Foydalanuvchini ro'yxatdan o'tkazish:

Foydalanuvchi telefon raqamini yuborgach, bot ularni ro'yxatdan o'tkazadi va asosiy menyuga o'tkazadi.

Asosiy menyu:

Asosiy menyuda quyidagi opsiyalar mavjud:

Buyurtma berish

Buyurtmalarini ko'rish

Sozlamalar

Ortga (Asosiy menyuga qaytish)

Buyurtma berish:

Foydalanuvchi "Buyurtma berish" ni tanlaganida, bot menyu rasmiga yuboradi va foydalanuvchidan buyurtmasini tasdiqlashni so'raydi.

Buyurtma tasdiqlash:

Foydalanuvchi o'z tanlovini yuborgach, bot buyurtmani tasdiqlaydi va 30 daqiqa ichida yetkazib berilishini bildiradi.

Buyurtmalarni ko'rish:

Foydalanuvchi "Buyurtmalarini ko'rish" ni tanlaganida, bot hozirgi buyurtmasi bor yoki yo'qligini ko'rsatadi.

Sozlamalar:

"Sozlamalar" opsiyasi hozircha ishlatilmayapti, ammo kelajakda qo'shimcha sozlamalar uchun joy mavjud.

Asosiy menyuga qaytish:

"Ortga" tugmasi foydalanuvchini asosiy menyuga qaytaradi.
