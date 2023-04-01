import sqlite3

print('Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
print('1 - Tokyo\n'
      '2 - Seoul\n'
      '3 - New Zealand\n'
      '0 - break')

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
      cursor = connection.cursor()
      cursor.execute(sql)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


def add_countries(connection, country):
    try:
        sql = '''INSERT INTO countries (title)
         VALUES (?)
        '''
        cursor = connection.cursor()
        cursor.execute(sql, country)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


def add_cities(connection, city):
    try:
        sql = '''INSERT INTO cities
            (title, area, country_id)
            VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, country)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


def add_people(connection, people):
    try:
        sql = '''INSERT INTO employees
               (first_name, last_name, city_id)
               VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, country)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


data_base_name = 'countries.db'

sgl_create_list_of_countries = '''
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(200) NOT NULL)
'''

data_base_name2 = 'cities.db'

sql_create_list_of_cities = '''
CREATE TABLE cities (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR (200) NOT NULL,
area INTEGER DEFAULT 0,
country_id INTEGER
FOREIGN KEY (country_id) REFERENCES countries (id))
'''

data_base_name3 = 'employees.db'

sql_create_list_of_employees = '''
CREATE TABLE employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR (200) NOT NULL,
last_name VARCHAR (200) NOT NULL,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES cities(id))
# '''
db_connection = create_connection(data_base_name)
db_connection1 = create_connection(data_base_name2)
db_connection2 = create_connection(data_base_name3)
if db_connection is not None:
    print('Connected successfully!')
    # add_countries(db_connection, ('Japan'))
    # add_countries(db_connection, ('Korea'))
    # add_countries(db_connection, ('New Zealand'))
    # add_cities(db_connection1, ('Tokyo', 2194, 81))
    # add_cities(db_connection1, ('HongKong', 1114, 852))
    # add_cities(db_connection1, ('Seoul', 605, 82))
    # add_cities(db_connection1, ('ShanKhai', 6340, 21))
    # add_cities(db_connection1, ('Astana', 722, 997))
    # add_cities(db_connection1, ('Bishkek', 127, 996))
    # add_cities(db_connection1, ('Milan', 181, 2))
    # add_people(db_connection2, ('Anna', 'George'))
    # add_people(db_connection2, ('Jennifer', 'Johnson'))
    # add_people(db_connection2, ('Natalie', 'Robinson'))
    # add_people(db_connection2, ('John', 'Ferguson'))
    # add_people(db_connection2, ('Samuel', 'Abilov'))
    # add_people(db_connection2, ('Ayana', 'Sagynova'))
    # add_people(db_connection2, ('Michael', 'Hamilton'))
    # add_people(db_connection2, ('Elijah', 'Fisher'))
    # add_people(db_connection2, ('Justin', 'Wright'))
    # add_people(db_connection2, ('Paula', 'Reyes'))
    a = '''SELECT first_name, last_name, city_id, country id from employees WHERE country_id is title[0]'''
    b = '''SELECT first_name, last_name, city_id, country id from employees WHERE country_id is title[1]'''
    c = '''SELECT first_name, last_name, city_id, country id from employees WHERE country_id is title[2]'''
    while True:
        n = int(input('Введите Id вашего города:'))
        if n == 1:
            print(a)
        elif n == 2:
            print(b)
        elif n == 3:
            print(c)
        elif n == 0:
            break
        # db_connection.close()
    # db_connection1.close()
    # db_connection2.close()
    print('DONE!')