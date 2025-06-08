import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

GROUP_ID = -1002512880634  # Replace with your actual group ID
BOT_USERNAME = "https://t.me/share/url?url=t.me/Mamalay223_bot?start=2222 အထန်မမလေးများသီးသန့် မန်ဘာဝင်ရန် join ထားပါ"

# Store user click data
user_click_data = {}  # Format: user_id: {"count": int, "cooldown": timestamp}


# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.first_name or user.username

    keyboard = [
        [
            InlineKeyboardButton("💦 ကြော်ငြာ ", url="https://t.me/GenkiMinerBot/GenkiMiner?startapp=_dOt50SJ"),
            InlineKeyboardButton("📤 Share (4/1)", url="https://t.me/share/url?url=t.me/Mamalay223_bot?start=2222 အထန်မမလေးများသီးသန့် မန်ဘာဝင်ရန် join ထားပါ"),
        ],
        [InlineKeyboardButton(" မန်ဘာဝင်မယ် ", callback_data="check_now")],
    ]

    text = (
        f"🥵 <b>မင်္ဂလာပါနော် အထန်ကြီး {username}ရေ...</b> 😘\n\n"
        "ဒီမှာ VIP ၅ ခုရှိတယ်နော် 💋\n\n"
    "1️⃣ အထန်မလေးတွေနဲ့ 💦 Free Sex Chat*\n"
    "2️⃣ မမကြီးတွေနဲ့ 😍 Free ချက်*\n"
    "3️⃣ ကြိုက်ကုန်းမမများ 👙 VIP GP*\n"
    "4️⃣ စပယားနေသူများ 🌶️🔥\n"
    "5️⃣ အန်တီကြီးများ 👵💦 သီးသန့် VIP*\n\n"
    "👇 ကြိုက်ရာ VIP 3 ခုကို Free ဝင်လို့ရပါတယ်* ✅"
    )

    await update.message.reply_html(text, reply_markup=InlineKeyboardMarkup(keyboard))


# --- Button handler ---
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    user_id = user.id
    chat = query.message.chat

    if query.data == "check_now":
        now = time.time()

        # Get user click data or init
        data = user_click_data.get(user_id, {"count": 0, "cooldown": 0})

        # Cooldown active?
        if data["cooldown"] > now:
            remaining = int((data["cooldown"] - now) / 60)
            await query.answer(f"▶ ကြော်ငြာ အပြီးထိ ကြည့်ပေးပါ ◀\n\n"
    "▶ Share 4 ကြိမ် လုပ်ပါ ◀\n\n"
    "အကုန်ပြီးသွားရင် မန်ဘာဝင်လို့ရပါပြီ✅💦", show_alert=True)
            return

        # Add click
        data["count"] += 1

        if data["count"] >= 2:
            # Set cooldown (30 min)
            data["cooldown"] = now + 180
            data["count"] = 0
            await query.answer("💋လုပ်ဆောင်ချက် စစ်ဆေးနေပါပြီ..🟢", show_alert=True)
        else:
            user_click_data[user_id] = data

            if chat.type == "private":
                await query.answer("လုပ်ဆောင်ချက် စစ်ဆေးနေပါပြီ..🟢", show_alert=True)

                group_text = (
                    f"🆔 <b>{user_id}</b> ကို VIP Group မှ လက်ခံလိုက်ပါပြီ။\n\n"
                    "VIP Free ဝင်လို့ရတုန်း အမြန်ဝင်ထားပေးပါနော်✅\n\n"
                    "မြန်မာ 18 + မမလေးများ သီးသန့် VIP [Free] ✅"
                )

                keyboard = [
                    [
                        InlineKeyboardButton("💦  ကြော်ငြာ ", url="https://t.me/GenkiMinerBot/GenkiMiner?startapp=_dOt50SJ"),
                        InlineKeyboardButton("📤 Share (4/2) ",  url="https://t.me/share/url?url=t.me/Mamalay223_bot?start=2222 အထန်မမလေးများသီးသန့် မန်ဘာဝင်ရန် join ထားပါ"),
                    ],
                    [InlineKeyboardButton(" မန်ဘာဝင်မယ် ", callback_data="check_now")],
                ]

                await context.bot.send_message(
                    chat_id=GROUP_ID,
                    text=group_text,
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
            else:
                await query.answer("📌 VIP ဝင်ရန် Share 4 ကြိမ်လုပ်ပေးပါ‌နော် 😘", show_alert=True)


# --- Main ---
def main():
    app = Application.builder().token("7863260296:AAG38lfZ5UDZp1RyPOTsFS2TNdf4UOoVsMk").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot running... 🔥")
    app.run_polling()


if __name__ == '__main__':
    main()
