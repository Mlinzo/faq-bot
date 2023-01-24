import re
from utils import to_md5

class Answers:
    def __init__(self, path: str = 'questions.txt'):
        content = ''
        with open(path, encoding='utf-8') as f:
            content = f.read()
        content = content.strip()
        q_pattern = r'q:(.+)'
        a_pattern = r'a:(.+)'
        file_questions = re.findall(q_pattern, content)
        file_answers = re.findall(a_pattern, content)

        if not len(file_questions) == len(file_answers):
            raise Exception(f'Unmatched questions with answers in file {path}. Make sure each question corresponds each answer')

        self._questions = dict()
        self.question_hashes = dict()
        for question, answer in zip(file_questions, file_answers):
            self._questions[question] = answer
            self.question_hashes[to_md5(question)] = question
    
    def __getitem__(self, key):
        return self._questions[key]

    def __setitem__(self, key, item):
        self._questions[key] = item

    def __iter__(self):
        return iter(self._questions)

