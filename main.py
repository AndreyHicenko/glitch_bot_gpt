import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '6016434617:AAECGvfRVqYJ2zgUOlkyf-wYRn6AxWz2HeE'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

OPENAI_API = "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"
@dp.message_handler()
async def send_message(message: types.Message):
    openai.api_key = OPENAI_API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    item = {"role": "user", "content": message.text}
    messages.append(item)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    await bot.send_message(message.from_user.id, str(response['choices'][0]['message']['content']))

if __name__ == '__main__':
    executor.start_polling(dp)

