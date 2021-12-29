import sqlite3


base = sqlite3.connect('my.sqlite3')
sql = base.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS database (
    note TEXT,
    questions TEXT
    )
    """
)

base.commit()

def creating_note():
    global my_note
    my_note = input('Мои заметки: ')

    sql.execute(f"SELECT note FROM database WHERE note = '{my_note}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO database VALUES (?)",(my_note,))
        base.commit()
        print('Заметка добавлена')
        for value in sql.execute("SELECT * FROM database"):
           print(value)
    else:
        for value in sql.execute("SELECT * FROM database"):
            print(value)
        print('Такая заметка уже существует!')

# creating_note()

def delete():
    global search, ans
    for value in sql.execute("SELECT * FROM database"):
        print(value)
    search = input('Выберите заметку: ')
    sql.execute(f"SELECT note FROM database WHERE note = '{search}'")
    if sql.fetchone():
        while True:
            ans = input(' Удалить, да или нет ?')
            if ans != 'да' and ans != 'нет':
                print('строго да или нет!')
            else:
                break
        if ans == 'да':
            sql.execute(f"DELETE FROM database WHERE note = '{search}'")
            base.commit()
            for value in sql.execute("SELECT * FROM database"):
                print(value)
        else:
            for value in sql.execute("SELECT * FROM database"):
                print(value)
    else:
        print('Такой заметки нет')

delete()