#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для своего варианта лабораторной работы 2.8 необходимо дополнительно реализовать
# сохранение и чтение данных из файла формата JSON. Необходимо также проследить за тем,
# чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
# работы.
# Вариант 15
import json
from datetime import datetime


def add_person_to_list(people_list):
    person = {}
    person["фамилия"] = input("Фамилия: ")
    person["имя"] = input("Имя: ")
    person["знак Зодиака"] = input("Знак Зодиака: ")
    birthday = datetime.strptime(input("Дата рождения (дд/мм/гггг): "), '%d/%m/%Y')
    person["дата рождения"] = [int(part) for part in birthday.strftime('%d %m %Y').split()]
    people_list.append(person)
    people_list.sort(key=lambda x: tuple(x["дата рождения"]))
    print("Данные добавлены и упорядочены по датам рождения.")


def display_people_by_zodiac_sign(people_list, search_zodiac_sign):
    found = False
    print(f"Люди с знаком Зодиака '{search_zodiac_sign}':")
    for person in people_list:
        if person["знак Зодиака"] == search_zodiac_sign:
            print(f"{person['фамилия']} {person['имя']} - {person['дата рождения'][0]}.{person['дата рождения'][1]}.{person['дата рождения'][2]}")
            found = True
    if not found:
        print(f"Нет людей с знаком Зодиака '{search_zodiac_sign}'.")


def save_to_json(people_list, filename):
    with open(filename, "w") as f:
        json.dump(people_list, f, indent=4, ensure_ascii=False)
    print(f"Данные сохранены в файл {filename}.")


def load_from_json(filename):
    with open(filename, "r") as f:
        people_list = json.load(f)
    return people_list


if __name__ == "main":
    people_data = []

    while True:
        command = input("Введите команду: ").lower()
        if command == "add":
            add_person_to_list(people_data)
        elif command == "list":
            searched_zodiac_sign = input("Введите знак Зодиака для поиска: ")
            display_people_by_zodiac_sign(people_data, searched_zodiac_sign)
        elif command == "save":
            filename = input("Введите имя файла для сохранения: ")
            save_to_json(people_data, filename)
        elif command == "load":
            filename = input("Введите имя файла для загрузки: ")
            people_data = load_from_json(filename)
        elif command == "exit":
            break
        else:
            print("Неизвестная команда.")


