'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
   
from random import randint
class Task:
    def __call__(self):
        config = (({"out":"Cумма чисел в файле = {0}", "def":self.main}))
        return config

    def main(self, value, out):
        self.list_gen=[str(randint(1, 100)) for i in range(1,10)]

        with open("files/task5.txt", "w+") as file:
            file.write(" ".join(self.list_gen))
            file.seek(0)
            for line in file:
                self.result=sum([int(i) for i in line.rstrip().split(" ") if i != ""])

        print("Числа в файле: {0}".format(self.list_gen))
        return out.format(self.result)