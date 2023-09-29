import psycopg2
import datetime

user_login = 1

connection = psycopg2.connect(host="localhost", user="keyenae",
                              password="admin", database="")

# Главное меню
def main_menu():
    if user_login is None:
        print("Вы еще не авторизованы, для прохождения опроса необходимо авторизоваться или зарегистрироваться")
        print("Нажмите 1 для регистрации\nНажмите 2 для авторизации")
    print("""Нажмите 3 для просмотра доступных опросов
    Нажмите 4 для прохождения опроса""")
    result = input()
