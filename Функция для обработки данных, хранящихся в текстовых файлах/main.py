import os

def MaxValue(): # функция для поиска максимального значения во втором столбце всех фалов в директории
    OutFile = open("out.txt", "w")

    for filename in os.listdir("D:/8 трим/python/test"): # Перебираем все файлы в директории
        with open(os.path.join("D:/8 трим/python/test", filename), 'r') as f: # открываем файл
            MaxValue = None
            for line in f:
                column = line.split() # Разделяем строку по пробелам
                value = float(column[1].replace('D', 'E'))
                if MaxValue is None or value > MaxValue:
                    MaxValue = value

            name = filename[filename.find(".") + 1:]
            name = name.rstrip("D+04.dat") + "     " + str(MaxValue)
            OutFile.write(name + '\n')

MaxValue()
