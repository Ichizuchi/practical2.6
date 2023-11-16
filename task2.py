#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Создание исходного словаря
    original_dict = {1: "one", 2: "two", 3: "three"}

    reversed_dict = {v: k for k, v in original_dict.items()}

    # Вывод исходного и нового словарей
    print("Исходный словарь:", original_dict)
    print('Новый "обратный" словарь:', reversed_dict)