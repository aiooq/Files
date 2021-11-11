'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

class Task:
    def __call__(self):
        config = (
            ({"out":"Общее количество строк в файле = {0}", "def":self.main}))
        return config

    def main(self, value, out):
        count_lines=0
        with open("files/task2.txt", "r", encoding="utf8") as file:
            for line in file:
                count_lines+=1
                count_words_in_line=0
                
                for symbol in (".",",","(",")","\n"):
                    line=line.replace(symbol,"")

                words=line.split(" ")
                for word in words:
                    if word=="":
                        continue
                    count_words_in_line+=1

                print("Строка #{0}:'{1}', слов в строке = {2}".format(count_lines,line,count_words_in_line))
        
        return out.format(count_lines)