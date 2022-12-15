from model import import_data, export_data
from view import input_data, print_data

def sep_is():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def do_it():
    print("Что хотите сделать?\n\
    1 - импорт\n\
    2 - экспорт")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = sep_is()
        import_data(input_data(), sep)
    if ch == '2':
        data = export_data()
        print_data(data)