# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



 пример1

импорт запросов

ссылка = 'https://reqres.in/api/users /'
k = запросы.get(ссылка)

m = k.json()
для k в m:
для ключа в k:
печать(ключ)
печать ('\n')

пример 2

импорт запросов

havola = 'http://api.weatherapi.com/v1 '
r = requests.get(havola + '/current.json', параметры={'ключ':'f32b2cd7fe364abd8d8182803230603', 'q': 'Ташкент'})

m = r.json()
для i в m:
для d в i:
печать(d)
печать ('\n')