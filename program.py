try:
    from include.main import Main as main
    # Конфигурируем программу добавляя задачи в список
    # В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
    # Последовательноть выволнения задач будет в соответствии со списком tasks 
    # Если необходимо, то список задач можно сортировать, так как номера задач весьма условны
    tasks = list()
    
    try:
        from tasks.task1 import Main as task1
        tasks.append(task1()())
    except ImportError:
        pass

    try:
        from tasks.task2 import Main as task2
        #tasks.append(task2()())
    except ImportError:
        pass

    try:
        from tasks.task3 import Main as task3
        #tasks.append(task3()())
    except ImportError:
        pass

    try:
        from tasks.task4 import Main as task4
        #tasks.append(task4()())
    except ImportError:
        pass

    try:
        from tasks.task5 import Main as task5
        #tasks.append(task5()())
    except ImportError:
        pass

    try:
        from tasks.task6 import Main as task6
        #tasks.append(task6()())
    except ImportError:
        pass

    try:
        from tasks.task7 import Main as task7
        #tasks.append(task7()())
    except ImportError:
        pass    

    main()(tasks)
except ImportError:
    print("import error!")
