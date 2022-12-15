def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    return [last_name, first_name, brith_name, phone_number]

def print_data(data):
        print("-"*93)
        print("|","Фамилия".center(20),"|", "Имя".center(20),"|", "Дата рождения".center(20), "|","Телефон".center(20), "|")
        print("-"*93)
        for item in data:
            print("|",item[0].center(20),"|", item[1].center(20),"|", item[2].center(20),"|",item[3].center(20),"|")
        print("-"*93)