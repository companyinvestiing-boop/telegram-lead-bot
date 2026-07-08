from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
TOKEN=os.getenv("BOT_TOKEN")
CHANNEL="@arbltrage_oleg"
ARTICLE="https://telegra.ph/Kak-vyjti-na-dohod-ot-500-000-rublej-v-mesyac-iz-doma-razbor-mehaniki-sovremennyh-cifrovyh-professij-07-07"
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    kb=[[InlineKeyboardButton("📢 Подписаться",url=f"https://t.me/{CHANNEL[1:]}")],[InlineKeyboardButton("✅ Проверить подписку",callback_data="check")]]
    await update.message.reply_text("🎁 Подпишитесь на канал и нажмите «Проверить подписку».",reply_markup=InlineKeyboardMarkup(kb))
async def check(update:Update,context:ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    m=await context.bot.get_chat_member(CHANNEL,q.from_user.id)
    if m.status in ["member","administrator","creator"]:
        await q.message.reply_text(f"Спасибо!\n\nВот ваша статья:\n{ARTICLE}")
    else:
        await q.message.reply_text("❌ Сначала подпишитесь на канал.")
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(check))
app.run_polling()
