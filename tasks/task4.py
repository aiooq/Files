'''4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
    При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

class Task:
    def __call__(self):
        config = (({"out":"Данные записаны в файл:\n{0}", "def":self.main}))
        return config

    def main(self, value, out):
        replacements = {
            "One":"Один",
            "Two":"Два",
            "Three":"Три",
            "Four":"Четыре",            
        }

        lines = list()
        with open("files/task4.txt", "r", encoding="utf8") as file:
            for line in file:
                for key in replacements.keys():
                    line=line.replace(key,replacements[key])
                lines.append(line)

        with open("files/task4_new.txt", "w") as outfile:
              outfile.writelines(lines)

        return out.format("".join(lines))