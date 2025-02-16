# Telegram Sovg'alar Katalogi

> Ushbu README bilan bir qatorda boshqa tillarda ham README fayllari mavjud:
>
> - [Ruscha](RU.README.md)
> - [Ukraincha](UK.README.md)
> - [O'zbekcha](UZ.README.md)
>
> Ushbu fayllar ushbu README bilan bir xil ma'lumotlarni o'z ichiga oladi, lekin tegishli tillarga tarjima qilingan.

Ushbu loyiha ikki asosiy qismdan iborat:
1. Telegram botlari foydalanuvchilarga yuborishi mumkin bo'lgan sovg'alar katalogi, Python skripti yordamida muntazam ravishda yangilanadi va GitHub Pages-ga joylashtiriladi.
2. Telegramdagi barcha mavjud sovg'alarni yuklab olish uchun aiogram yordamida skript.

---

## Xususiyatlar

- Sovg'alar ro'yxatini ularning ID, narxlari va boshqa tafsilotlari bilan ko'rsatadi.
- Bir nechta tillarni qo'llab-quvvatlaydi: Inglizcha, Ruscha, Ukraincha va O'zbekcha.
- Katalogni eng so'nggi ma'lumotlar bilan avtomatik ravishda yangilaydi.
- Turli qurilmalarda yaxshiroq foydalanuvchi tajribasi uchun moslashuvchan dizayn.
- Telegramdagi barcha mavjud sovg'alarni yuklab oladi.
- Sovg'a ma'lumotlari va rasmlarini mahalliy saqlaydi.

---

## Loyihaning Tuzilishi

```plaintext
telegram-gifts-catalogue/ 
├── .github/ 
│ └── workflows/ 
│ │ └── generate.yml # Katalogni yaratish va joylashtirish uchun GitHub Actions ish jarayoni 
├── src/ 
│ └── collector.py # Sovg'alarni yuklab olish uchun Python skripti
├── web/ 
│ ├── index.html # Katalogning inglizcha versiyasi 
│ ├── ru.index.html # Katalogning ruscha versiyasi 
│ ├── uk.index.html # Katalogning ukraincha versiyasi 
│ ├── uz.index.html # Katalogning o'zbekcha versiyasi 
│ └── style.css # Katalog uchun uslub fayli 
├── .gitignore # Git e'tiborsiz fayli
├── pyproject.toml # Loyiha konfiguratsiya fayli
└── README.md # Loyiha hujjatlari
```

---

## Boshlash

### Talablar

- Python 3.12 yoki undan yuqori
- Git
- Katalogni joylashtirish uchun GitHub hisob qaydnomasi va ombori

### O'rnatish

#### Barcha Sovg'alarni Yuklab Olish uchun Mahalliy Sozlash

1. Omborni klonlash:
    ```sh
    git clone https://github.com/MasterGroosha/telegram-gifts-catalogue.git
    cd telegram-gifts-catalogue
    ```

2. Virtual muhit yaratish va faollashtirish:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Windowsda `venv\Scripts\activate` ni ishlating
    ```

3. Kerakli kutubxonalarni o'rnatish:
    ```sh
    pip install -r requirements.txt
    ```

4. Asosiy katalogda `.env` faylini yarating va Telegram bot tokeningizni qo'shing:
    ```sh
    BOT_TOKEN=your_bot_token_here
    OUTPUT_DIR=/path/to/output/directory
    ```

5. Barcha mavjud sovg'alarni yuklab olish uchun skriptni ishga tushirish:
    ```sh
    python src/collector.py
    ```

#### GitHub Pages-da O'z-o'zini Joylashtirish uchun Sozlash

1. Omborni GitHub hisob qaydnomangizga fork qiling.

2. Ombor sozlamalariga o'ting va `BOT_TOKEN` nomli maxfiy ma'lumot qo'shing.

3. Omboringizda GitHub Actions-ni yoqing.

4. "Generate and Deploy" (o'chirilgan) nomli ish jarayonini ko'rasiz. Uni bosing va faollashtiring.

5. Katalogni yaratish uchun ish jarayonini qo'lda ishga tushiring.

6. Ombor sozlamalariga o'ting, Pages bo'limiga o'ting va `web` tarmog'i uchun uni yoqing. Yo'l sifatida `/root` ni ishlating (standart).

7. Saytingizga yoki sozlangan domeningizga tashrif buyuring va katalogni ko'ring.

---

## Litsenziya

Ushbu loyiha MIT litsenziyasi ostida litsenziyalangan. Tafsilotlar uchun [LICENSE](LICENSE) faylini ko'ring.