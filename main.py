import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle '/info'
@bot.message_handler(commands=['info'])
async def send_info(message):
    text = 'This bot is created with telebot library.\nIt can repeat your messages.'
    await bot.reply_to(message, text)


# Handle photo
@bot.message_handler(content_types=['photo'])
async def handle_photo(message):
    await bot.reply_to(message, "You sent a photo!")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())
