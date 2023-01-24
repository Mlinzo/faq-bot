from aiogram import types
from Answers import answers

class Keyboards():
    def __init__(self):
        self._answers = answers
        self.main_label = 'Часто задаваемые вопросы'
    
    @property
    def main(self) -> types.ReplyKeyboardMarkup:
        return types.ReplyKeyboardMarkup([[self.main_label]], resize_keyboard=True, one_time_keyboard=True)

    @property
    def questions(self) -> types.InlineKeyboardMarkup:
        buttons = [ [types.InlineKeyboardButton(q, callback_data=q_hash)] for q, q_hash in zip(self._answers, answers.question_hashes)]
        return types.InlineKeyboardMarkup(inline_keyboard=buttons)