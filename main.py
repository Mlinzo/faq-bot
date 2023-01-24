from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import os

from Answers import answers
from Keyboards import keyboards

from dotenv import load_dotenv
load_dotenv() 
API_TOKEN = os.environ['API_TOKEN']

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer('Привет, здесь можно найти ответы на часто задаваемые вопросы о факультете "Кибербезопасности и информационных технологий" НУ "ОЮА"', reply_markup=keyboards.main)

@dp.message_handler(Text(keyboards.main_label))
async def questions_handler(message: types.Message):
    await message.answer('Выберите интересующий Вас вопрос', reply_markup=keyboards.questions)

@dp.callback_query_handler(lambda call: call.data in answers.question_hashes)
async def answer_handler(callback: types.CallbackQuery):
    question = answers.question_hashes[callback.data]
    await callback.answer()
    await callback.message.answer(answers[question])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)