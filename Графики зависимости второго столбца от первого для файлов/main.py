import matplotlib.pyplot as plt
import os
import re

def Print_Graph(path_to_file):
  with open(path_to_file, 'r') as f: # открываем файл
    lines = f.readlines() # берем строку, после чего первое число заносит в 1 список, а второе число во второй список
    x_psi = [float(line.split()[0].replace('D', 'E')) for line in lines]
    y_psi = [float(line.split()[1].replace('D', 'E')) for line in lines]

  zipped_lists = list(zip(x_psi, y_psi))  # объединяем списки
  sorted_zipped_lists = sorted(zipped_lists)  # сортируем по первому списку
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)  # разделяем списки

  plt.plot(sorted_list1,sorted_list2)

def Main_Print_Graph(path_to_directory): # функция для отрисовки зависимостей второго столбца от первого в файлах
    for file in os.listdir(path_to_directory): # перебираем все файлы в директории
      if file.startswith("psi_G="): # если файл начинается с psi (это нужно, чтобы сейчас сразу открыть psi и psi2)
        path_to_file = os.path.join(path_to_directory, file) # получаем путь к файлу, объединяя путь к директории и имя файла
        G = re.search(r'(\d+\.\d+D[+-]\d+)', file)  # Ищем в имени файла значение G
        G2 = G.group(1) # сохраняем найденное значение
        Print_Graph(path_to_file)
        path_to_file =f"{path_to_directory}/psi2_G= {G2}.dat" # получаем путь к файлу psi2
        Print_Graph(path_to_file)
        plt.xlabel('Значения первого столбца')
        plt.ylabel('Значения второго столбца')
        G = re.search(r'(\d+\.\d+D[+-]\d+)', path_to_file)
        G2 = G.group(1)
        G2 = float(G2.replace('D', 'E'))
        plt.title(f'График зависимости второго столбца от первого файал: {G2}')
        plt.show() # выводим график

def Print_Graph_2(path_to_directory): # функция для отрисовки зависимости максимального значения psi2 от G
    x = []
    y = []
    for file in os.listdir(path_to_directory): # перебираем все файлы в директории
      if file.startswith("psi2_G="): # если файл начинается с psi2
        path_to_file = os.path.join(path_to_directory, file) # получаем путь к файлу, объединяя путь к директории и имя файла
        G = re.search(r'(\d+\.\d+D[+-]\d+)', file)  # Ищем в имени файла значение G
        G2 = G.group(1) # сохраняем найденное значение
        G2 = float(G2.replace('D', 'E'))
        x.append(G2) # добавляем значение, оно будет координатой x

        with open(path_to_file, 'r') as f: # открываем файл
          lines = f.readlines() # берем строку
          y_psi = [float(line.split()[1].replace('D', 'E')) for line in lines]

        y_psi = y_psi[:len(y_psi)//2]
        y.append(max(y_psi))

        zipped_lists = list(zip(x, y))  # объединяем списки
        sorted_zipped_lists = sorted(zipped_lists)  # сортируем по первому списку
        sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)  # разделяем списки

    plt.plot(sorted_list1,sorted_list2)
    plt.xlabel('Значения G')
    plt.ylabel('Значения psi2')
    plt.title(f'График зависимости значений psi2 от G')
    plt.show() # выводим график
