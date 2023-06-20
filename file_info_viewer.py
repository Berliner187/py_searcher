#!/usr/bin/env python3
import os
import sys


def add_words_in_array():
    """ Добавление вдодящих аргументов в массив """
    words_array = []
    for param in sys.argv:
        words_array.append(param)
    words_array.pop(0)
    return words_array


def converting_to_a_directory():
    """ Преобразование в директорию массива из входящих аргументов """

    _path, _path_to_file = '', ''
    _words_array = add_words_in_array()
    for i in range(len(_words_array)):
        if i != len(_words_array):
            _path += _words_array[i] + '/'
    for pwd, folders, files in os.walk(_path):
        for file in files:  # Итерация по файлам
            if _words_array[-1] == file:
                _path_to_file += _path + file    # К пути добавляется дублированное название директории

    return _path_to_file


if __name__ == '__main__':
    # Конечный путь
    path_to_file = converting_to_a_directory()
    try:
        if os.path.exists(path_to_file):
            if os.path.isfile(path_to_file):
                os.system(f'cat {path_to_file}')
            elif os.path.isdir(path_to_file):
                print('Это директория')
            else:
                print('Это не файл и не директория')
        else:
            print('Файла не существует')
    except FileExistsError or FileNotFoundError:
        print('Ошибка FileExistsError или FileNotFoundError')
