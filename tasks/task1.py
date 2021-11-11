'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
    Об окончании ввода данных свидетельствует пустая строка.'''

class Task:
    def __call__(self):
        config = (
            ({"in":"Введите данные: ","out":"Ввод данных завершен!", "def":self.main}))
        return config

    def main(self, value, out):
        if value=="":
            return out

        with open("files/task1.txt", "a") as file:
            file.write(value+"\n")
            print("Данные добавлены в файл!")

        raise Exception("Repeat")
