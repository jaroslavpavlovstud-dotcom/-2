import csv
import xml.etree.ElementTree as ET


# Читаем книги из CSV-файла
def read_books():
    with open("books.csv", "r", encoding="windows-1251") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader, None)  # Пропускаем заголовок
        return list(reader)


# 1. Считаем книги, названия которых длиннее 30 символов
def count_long_titles(books):
    count = 0

    for book in books:
        if len(book[1]) > 30:
            count += 1

    print("Книг с названием длиннее 30 символов:", count)


# 2. Ищем книги по автору
def search_by_author(books):
    author = input("Введите имя или фамилию автора: ").strip().lower()
    found = 0

    for book in books:
        if author in book[3].lower():
            print(book[1], "-", book[3])
            found += 1

    if found == 0:
        print("Книги не найдены.")
    else:
        print("Найдено книг:", found)


# 3. Создаём библиографические ссылки для 20 книг
def create_bibliography(books):
    with open("result.txt", "w", encoding="utf-8") as file:
        for number, book in enumerate(books[:20], start=1):
            title = book[1]
            author = book[3]
            year = book[6].split()[0].split(".")[-1]

            line = f"{number}. {author}. {title} - {year}\n"
            file.write(line)

    print("Список из 20 записей сохранён в result.txt")


# 4. Получаем два списка из XML
def read_currencies():
    tree = ET.parse("currency.xml")
    root = tree.getroot()

    char_codes = []
    values = []

    for currency in root.findall("Valute"):
        char_code = currency.findtext("CharCode")
        value = currency.findtext("Value")

        char_codes.append(char_code)
        values.append(float(value.replace(",", ".")))

    print("Список кодов валют:")
    print(char_codes)

    print("Список значений валют:")
    print(values)


def main():
    books = read_books()

    count_long_titles(books)
    search_by_author(books)
    create_bibliography(books)
    read_currencies()


if __name__ == "__main__":
    main()
