import re
from typing import List, Dict


def process_bank_search(data:List[Dict], search:str)->List[Dict]:
    '''Функция поиска по строке'''
    #автоматически экранируем все специальные символы (метасимволы) в строке через re.escape()
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    result = [
        operation for operation in data
        if 'description' in operation and pattern.search(operation['description'])
    ]
    return result