'''Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''
class Main:
    def __call__(self):
        config = (
            ({"out":"Общее количество строк в файле = {0}", "def":self.func_main}))
        return config

    def func_main(self, value, out):
        count_lines=0
        with open("files/task2.txt", "r") as file:
            for line in file:
                count_lines+=1
                count_words_in_line=0
                line=line.replace(",","").replace(".","")
                line=line.replace("(","").replace(")","")
                words=line.split(" ")
                for word in words:
                    if word=="":
                        continue
                    else:
                        count_words_in_line+=1
                        print(word)
                print("Строка #{0}, количество слов в строке: {1}".format(count_lines,count_words_in_line))
        return out.format(count_lines)