import os
import logging
import subprocess
from data import format_data
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
import emoji


Token = os.environ.get("BOT_TOKEN")
COIN_DATA = format_data()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi there! I'm here to keep you informed about the crypto market. Get live prices, track your favorite coins, and stay ahead of the curve. \nType /help for a list of commands."
    )


async def helps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""/help - For a list of commands\n/coins - To get the the top 10 cryptocurrency coin prices by market share\n/btc - To get the latest price of Bitcoin\n/eth - To get the latest price of Etherium\n/usdt - To get the latest price of Tether USD\n/bnb - To get the latest price of Binance Coin\n/sol - To get the latest price of Solana\n/xrp - To get the latest price of XRP\n/usdc - To get the latest price of USDC\n/steth - To get the latest price of Lido Staked Ether\n/doge - To get the latest price of Dogecoin\n/ton - To get the latest price of Toncoin"""
    )


async def coins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for coin in coin_data:
        coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"

    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 0:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 1:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 2:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )

async def sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 3:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def bnb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 4:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def xrp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 5:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def usdc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 6:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )

async def doge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 7:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def ton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 8:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )

async def ada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin_data = COIN_DATA
    coin_message = ""
    for i, coin in enumerate(coin_data):
        if i == 9:
            coin_message += f"\n{coin['name']}: ${coin['price_usd']:.2f} (R {coin['price_zar']:.2f})\n {coin['change']:.2f}%  {emoji.emojize(':up-right_arrow:') if coin['change'] >= 0 else emoji.emojize(':down-right_arrow:')}\n\n"
    script_path = "data.py"
    subprocess.call({"python", script_path})
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = coin_message
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. \nType /help for a list of commands.")


if __name__ == "__main__":
    # cryptocurrencypricesupdatebot

    application = ApplicationBuilder().token(Token).build()

    help_handler = CommandHandler("help", helps)
    start_handler = CommandHandler("start", start)
    coins_handler = CommandHandler("coins", coins) 
    btc_handler = CommandHandler("btc", btc)
    eth_handler = CommandHandler("eth", eth)
    usdt_handler = CommandHandler("usdt", usdt)
    sol_handler = CommandHandler("sol", sol)
    bnb_handler = CommandHandler("bnb", bnb)
    xrp_handler = CommandHandler("xrp", xrp)
    usdc_handler = CommandHandler("usdc", usdc)
    doge_handler = CommandHandler("doge", doge)
    ton_handler = CommandHandler("ton", ton)
    ada_handler = CommandHandler("ada", ada)
    unknown_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), unknown)

    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(coins_handler)
    application.add_handler(btc_handler)
    application.add_handler(eth_handler)
    application.add_handler(usdt_handler)
    application.add_handler(sol_handler)
    application.add_handler(bnb_handler)
    application.add_handler(xrp_handler)
    application.add_handler(usdc_handler)
    application.add_handler(doge_handler)
    application.add_handler(ton_handler)
    application.add_handler(ada_handler)
    application.add_handler(unknown_handler)

    application.run_polling()