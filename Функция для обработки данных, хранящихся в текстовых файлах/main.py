import os

def MaxValue(): # Функция для поиска максимального значения во втором столбце всех фалов в директории
    Out_File = open("out.txt", "w")

    for filename in os.listdir("путь к вашей директории"): # Перебираем все файлы в директории
        with open(os.path.join("D:/8 трим/python/test", filename), 'r') as f: # Открываем файл
            Max_Value = None
            for line in f:
                column = line.split() # Разделяем строку по пробелам
                value = float(column[1].replace('D', 'E'))
                if Max_Value is None or value > Max_Value:
                    Max_Value = value

            name = filename[filename.find(".") + 1:]
            name = name.rstrip("D+04.dat") + "     " + str(Max_Value)
            Out_File.write(name + '\n')

MaxValue()
