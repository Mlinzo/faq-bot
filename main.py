from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import link
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
    await message.answer('Привіт, тут можна знайти відповіді на поширені питання щодо факультету "Кібербезпеки та інформаційних технологій" НУ "ОЮА"', reply_markup=keyboards.main)

@dp.message_handler(Text(keyboards.main_label))
async def questions_handler(message: types.Message):
    await message.answer('Оберіть питання, що Вас цікавить', reply_markup=keyboards.questions)

@dp.callback_query_handler(lambda call: call.data in answers.question_hashes)
async def answer_handler(callback: types.CallbackQuery):
    question = answers.question_hashes[callback.data]
    await callback.answer()
    await callback.message.edit_reply_markup(None)
    await callback.message.answer(answers[question], parse_mode='Markdown', reply_markup=keyboards.questions)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
