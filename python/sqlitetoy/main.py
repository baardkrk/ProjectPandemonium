import sqlite3
import json
import re


def create_database(path: str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
    except sqlite3.Error as e:
        raise e
    return connection


def create_user_table(connection: sqlite3.Connection):
    create_objects = """
        CREATE TABLE IF NOT EXISTS user (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            birthyear integer NOT NULL
        )
        """
    cursor = connection.cursor()
    cursor.execute(create_objects)
    connection.commit()
    return cursor.lastrowid


def minimize_query(query: str) -> str:
    # Reomve excessive spaces, newlines and ending semicolon
    return re.sub(r'\s+', ' ', query).strip().rstrip(';')


def match_table(create_table: str, connection: sqlite3.Connection) -> bool:
    vanilla = create_table.replace('IF NOT EXISTS ', '')
    table_name = re.match(r'.*CREATE TABLE (\w+).*', vanilla.strip()).group(1)
    cursor = connection.cursor()
    cursor.execute(f'SELECT sql FROM sqlite_master WHERE type=\'table\' AND name=\'{table_name}\'')
    table = cursor.fetchone()
    if table is None:
        # Return true, as the table isn't created yet
        return True
    existing_table_sql = minimize_query(table[0])
    vanilla = minimize_query(vanilla)
    return existing_table_sql == vanilla


def check_database_empty(connection: sqlite3.Connection) -> bool:
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM sqlite_master')
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f'SELECT * FROM {table[0]}')
        if cursor.fetchall():
            # Not empty
            return False
    return True


if __name__ == '__main__':
    db = create_database('/home/bard/sqlitetoy/test.db')
    create_user_table(db)
    print(check_database_empty(db))
    create_objects = """
        PRAGMA foreign_keys = ON;
        CREATE TABLE IF NOT EXISTS user (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            birthyear integer NOT NULL
        )
        """
    print(match_table(create_objects, db))
    another = """
       CREATE TABLE IF NOT EXISTS non (
           id integer PRIMARY KEY AUTOINCREMENT,
           test text
       )
       """
    print(match_table(another, db))
    create_user_table(db)
    cursor = db.cursor()
    cursor.execute('INSERT INTO user (name, birthyear) VALUES (?, ?)', ("John Doe", 1998))
    print(f'Empty before commit: {check_database_empty(db)}')
    db.commit()
    print(f'Empty after commit: {check_database_empty(db)}')
    print('hello')
