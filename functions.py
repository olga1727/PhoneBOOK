def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as file:
        for record in phone_book:
            file.write(','.join(record.values()) + '\n')


def print_result(phone_book):
    for record in phone_book:
        print(record)


def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record.get('Фамилия') == last_name]
    return result


def find_by_number(phone_book, number):
    result = [record for record in phone_book if record.get('Телефон') == number]
    return result


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            write_txt('phonebook.txt', phone_book)
            return "Номер успешно изменен."
    return "Абонент с указанной фамилией не найден."



def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            write_txt('phonebook.txt', phone_book)
            return "Абонент успешно удален."
    return "Абонент с указанной фамилией не найден."


def delete_by_number(phone_book, number):
    records_to_delete = [record for record in phone_book if record.get('Телефон') == number]

    if not phone_book:
        return "В телефонной книге записей нет"
    elif not records_to_delete:
        return "Абоненты с указанным номером телефона не найдены."
    
    phone_book[:] = [record for record in phone_book if record.get('Телефон') != number]
    write_txt('phonebook.txt', phone_book)
    return "Абоненты успешно удалены."



def change_description(phone_book, last_name, new_description):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Описание'] = new_description
            write_txt('phonebook.txt', phone_book) 
            return "Описание успешно изменено."
    return "Абонент с указанной фамилией не найден."



def add_user(phone_book, user_data):
    new_record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], user_data.split(', ')))
    phone_book.append(new_record)
    write_txt('phonebook.txt', phone_book)





def change_description(phone_book, last_name, new_description):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Описание'] = new_description
            return "Описание успешно изменено."
    return "Абонент с указанной фамилией не найден."


def show_menu():
    print("\nВыберете необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер телефона абонента\n"
          "5. Изменить описание абонента\n"
          "6. Удалить абонента по фамилии\n"
          "7. Удалить абонента по номеру телефона\n"
          "8. Добавить абонента в справочник\n"
          "9. Закончить работу")
    choice = int(input())
    return choice
