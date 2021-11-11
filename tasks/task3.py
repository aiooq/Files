'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
    Выполнить подсчет средней величины дохода сотрудников.'''
    
class Task:
    def __call__(self):
        config = (({"out":"Средняя величина дохода сотрудников = {0}", "def":self.main}))
        return config

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def main(self, value, out):
        if value=="":
            return

        with open("files/task3.txt", "r", encoding="utf8") as file:
            profits = list()
            for line in file:
                try:
                    profit=float(line.rstrip())
                    profits.append(profit)
                    if profit<20000:
                        print("Сотрудник: {0}, оклад: {1}".format(self.name,profit))
                except:
                    self.name=line.rstrip()

        return out.format(self.mean(profits))