# Задача 38
'''
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных
'''
from functions import read_txt, write_txt, print_result, find_by_lastname, find_by_number, change_number, \
    delete_by_lastname, delete_by_number, change_description, add_user, show_menu

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    last_name = ''
    first_name = ''
    phone = ''
    description = ''

    while choice != 9:
        if choice == 1:
                print_result(phone_book)
        elif choice == 2:
                last_name = input('Введите фамилию: ')
                print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
                number = input('Введите номер: ')
                print(find_by_number(phone_book, number))

        elif choice == 4:  # Изменить номер телефона
                last_name = input('Введите фамилию: ')
                new_number = input('Введите новый номер: ')
                print(change_number(phone_book, last_name, new_number))
                write_txt('phonebook.txt', phone_book)

        elif choice == 5: # Изменить описание
                last_name = input('Введите фамилию: ')
                new_description = input('Введите новое описание: ')
                print(change_description(phone_book, last_name, new_description))
                write_txt('phonebook.txt', phone_book)  

        elif choice == 6: # Удаление по фамилии
                last_name = input('Введите фамилию: ')
                print(delete_by_lastname(phone_book, last_name))
                write_txt('phonebook.txt', phone_book)

        elif choice == 7: # Удалить по номеру
                number = input('Введите номер: ')
                print(delete_by_number(phone_book, number))

        elif choice == 8: # Добавить абонента
                last_name = input('Введите фамилию: ')
                first_name = input('Введите имя: ')
                phone = input('Введите номер телефона: ')
                description = input('Введите описание: ')
                new_user_data = f'{last_name}, {first_name}, {phone}, {description}'
                new_record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], new_user_data.split(', ')))
                phone_book.append(new_record)
                write_txt('phonebook.txt', phone_book)

        choice = show_menu()

work_with_phonebook()








