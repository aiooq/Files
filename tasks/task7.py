'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. 
    Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: 
        [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
        Пример json-объекта:
        [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    Подсказка: использовать менеджеры контекста.'''

import json
from contextlib import contextmanager

@contextmanager
def get_dict_firm_profit(item):
    firm = {item[0]:(float(item[2])-float(item[3]))}
    yield firm

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)    

class Task:
    def __call__(self):
        config = (({"out":"Итоговый список: {0}", "def":self.main}))
        return config

    def main(self, value, out):
        data_from_file = list()
        with open("files/task7.txt", "r", encoding="utf8") as file:
            for line in file:
                parts=[i for i in line.rstrip().split(" ") if i != ""]
                # Проверяем что строка в файле состоит из правильного кол-ва частей
                if len(parts)<4:
                    continue
                # Добавляем части в общий список данных из файла
                data_from_file.append(parts)

        # Если тип данных корректный, элемент добавляется в словарь
        firm_dict = dict()
        for item in data_from_file:
            with get_dict_firm_profit(item) as firm:
                firm_dict.update(firm)

        # Рассчитываем среднюю прибыль по фирмам и формируем итоговый список
        result_list = [firm_dict,{"average_profit":mean(firm_dict.values())}]

        # Выгружаем итоговый список в файл
        with open('files/task7_json.txt', 'w') as outfile:
            json.dump(result_list, outfile)

        return out.format(result_list)