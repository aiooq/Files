class Main:
    def __call__(self, tasks):
        self.IsStopped = False
        # Основной цикл
        while not self.IsStopped:
            # Основная функция
            self.main(tasks)

            if self.IsStopped:
                break

            value = input("Введите 'yes' или 'y', чтобы повторить программу, а для выхода нажмите Enter: ")
            if value != 'y' and value != 'yes':
                break

        print("Завершение программы")

    @staticmethod
    def GetValueByType(value, type_values):
        for item in type_values:
            try:
                if item == str:
                    if len(type_values)==1:
                        try:
                            float(value)
                            continue
                        except ValueError:
                            if value.isnumeric():
                                continue
                    else:
                        return item(value)
            except:
                continue

        for item in type_values:
            try:
                if item == float:
                    if len(type_values)==1:
                        if len(value)>0:
                            if value[0]=='-':
                                    if value[1:len(value)].isnumeric():
                                        continue
                            else:
                                if value.isnumeric():
                                    continue
                elif item == int:
                    if len(type_values)==1:
                        try:
                            if len(value)>0:
                                if value[0]=='-':
                                    if not value[1:len(value)].isnumeric():
                                        continue
                                elif not value.isnumeric():
                                    continue
                        except ValueError:
                                continue
                    else:
                        continue
                return item(value)
            except:
                continue
        return None

    def main(self, tuple):
        i=0
        while len(tuple)>i and not self.IsStopped:
            if not isinstance(tuple[i], dict):
                self.main(tuple[i])
                i+=1
                continue

            out = None
            value = None
            if "in" in tuple[i]:  
                if "out" in tuple[i]:
                    out = tuple[i]["out"]

                value = input(tuple[i]["in"])

                if "type" in tuple[i]:
                    try:
                        type_values=tuple[i]["type"]
                        if type(type_values)==type:
                            type_values={type_values}
                        
                        value=Main.GetValueByType(value, type_values)
                        if value==None:
                            raise Exception()
                        
                    except:
                        print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                        continue
            elif "out" in tuple[i]:
                out = tuple[i]["out"]
                value = out

            try:
                if "def" in tuple[i]:
                    value = tuple[i]["def"](value,out)
                if value != None:
                    print(value)
            except Exception as e:
                if str(e)=="PositiveNumber":
                    i-=1
                    print("Некорректное значение, ожидается положительное число, пожалуйста повторите ввод!")
                elif str(e)=="NegativeNumber":
                    i-=1
                    print("Некорректное значение, ожидается отрицательное число, пожалуйста повторите ввод!")                    
                elif str(e)=="StrIsNotNumeric":
                    i-=1
                    print("Некорректное значение, ожидается число, пожалуйста повторите ввод!")
                elif str(e)=="StrFormatIsNotValid":
                    i-=1
                    print("Некорректный формат, пожалуйста смотрите пример и повторите ввод!")
                elif str(e)=="ValueOutOfRange":
                    i-=1
                    print("Значение вне диапазона, пожалуйста повторите ввод!") 
                elif str(e)=="ValueIsNull":
                    i-=1
                    print("Некорректное значение, оно не должно быть равно нулю, пожалуйста повторите ввод!")
                elif str(e)=="Repeat":
                    i-=1                    
                elif str(e)=="ProgramStop":
                    self.IsStopped=True                
                else:
                    print("Ошибка в конфигурации: "+str(e))               
                continue
            finally:
                i+=1        