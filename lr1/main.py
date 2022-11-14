#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Используя замыкания функций, объявите внутреннюю функцию,
# которая из переданного ей списка строк формирует многострочную строку вида:
#  и возвращает ее. Где строка1, строка2, … - это строки из переданного функции списка.
# <ol>
# <li>строка_1</li>
# …
# <li>строка_N</li>
# </ol>
# Вызовите внутреннюю функцию замыкания и отобразите на экране результат ее работы.


def get_func(tag):
    tag1 = f"<{tag}>"
    tag2 = f"</{tag}>"
    print("<ol>")


    def func(string):
        nonlocal tag1
        nonlocal tag2
        for i in range(len(string)):
            print(f"{tag1}  {string[i]}  {tag2}")
        print("</ol>")

    return func


# Press the green button in the gutter to run the script.
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    a = ['строка_1', 'строка...', 'строка_N']
    new_tag = get_func("li")
    new_tag(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
