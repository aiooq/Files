'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
    Об окончании ввода данных свидетельствует пустая строка.'''
class Main:
    def __call__(self):

        config = (
            ({"in":"Введите данные: ", "def":self.FuncMain}))
        return config

    def FuncMain(self, value, out):
        try:
            file=open("files/task1.txt", "a")
            try:
                file.write(value+"\n")
                print("Данные добавлены в файл!")
            except Exception as e:
                print(e)
            finally:
                file.close()
        except Exception as e:
            print(e)
        raise Exception("Repeat")
