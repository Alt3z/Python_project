import re
import sqlite3

bib_path = 'путь к файлу biblio.bib'
sql_path = 'путь к вашей БД'

def make_field(fields, name):
    if name in fields:
        return fields[name]
    else:
        return ""

def parse_bibtex(bib_path, connection, cursor): # переделанная функция из задания "Работа с библиотекой re"
    with open(bib_path, 'r', encoding='utf-8') as file:
        data = file.read()

    pattern = re.compile(r'@(\w+)\{(.*?),\s*([^@]*)\}', re.DOTALL)
    matches = pattern.findall(data)

    for match in matches:
        typee = match[0].strip()
        key = match[1].strip()
        body = match[2].strip()

        fields = dict(re.findall(r'(\w+)\s*=\s*{(.*?)}', body, re.DOTALL))

        author = make_field(fields, 'Author')
        title = make_field(fields, 'Title')
        journal = make_field(fields, 'Journal')
        year = make_field(fields, 'Year')
        language = make_field(fields, 'Language')

        cursor.execute('INSERT INTO Book (Author, Title, Journal, Year, Language) VALUES (?, ?, ?, ?, ?)', (author, title, journal, year, language))
        connection.commit()

connection = sqlite3.connect(sql_path)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Book (
id INTEGER PRIMARY KEY,
Author TEXT NOT NULL,
Title TEXT NOT NULL,
Journal TEXT NOT NULL,
Year TEXT NOT NULL,
Language TEXT NOT NULL,
UNIQUE ("Title") ON CONFLICT IGNORE
)
''')

parse_bibtex(bib_path, connection, cursor)

cursor.execute("SELECT * FROM Book WHERE Author LIKE '%Путин%'") # делаем запрос, чтобы вывести все книги с автором Путин
books = cursor.fetchall()
for book in books:
    print(book)

connection.close()
