documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def people_name(doc_number):
    for id in documents:
        if id["number"] == doc_number:
            return (f'Документ принадлежит: {id["name"]}')
            break
    else:
        return ('Нет такого номера документа')


def shelf_id(dirs):
    user_input = input('Введите номер документа ')
    for key in dirs:
        if user_input in dirs.get(key):
            return key
    return 'Нет такого документа'


def info_list(docs):
    for rec in docs:
        rec_2 = list(rec.values())
        return f'{rec_2[0]} "{rec_2[1]}" "{rec_2[2]}"'

def add_info(docs_1, docs_2):
    user_input = input('Введите номер полки куда положить документ. ')
    if user_input not in docs_2:
        return 'Нет такой полки'
    doc = {}
    for info in ('type', 'number', 'name'):
        doc[info] = input(f'{info}: ')
    docs_1.append(doc)
    docs_2[user_input].append(doc['number'])
    return 'Документ добавлен'

def main():
    print('Возможные команды: p, s, l, a, q')
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people_name(documents)
        elif user_input == 's':
            print(shelf_id(directories))
        elif user_input == 'l':
            info_list(documents)
        elif user_input == 'a':
            print(add_info(documents, directories))
        elif user_input == 'q':
            print('До свидания!')
            break

if __name__ == '__main__':
    main()
