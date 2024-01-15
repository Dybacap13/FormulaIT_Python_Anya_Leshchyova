BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_:int, name:str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})"

# TODO написать класс Library
class Library:
    count = 0
    dist_book_with_id = {}
    def __init__(self, books=[]):
        self.books = books
        for id, name in enumerate(books):
            __class__.dist_book_with_id[name] = id + 1
        __class__.count = len(books)
    def get_next_book_id(self) ->int:
        if __class__.count == 0:
            return 1
        return __class__.count + 1
    def get_index_by_book_id(self, id_:int) -> int:
        index = [i - 1 for i in list(__class__.dist_book_with_id.values()) if i == id_]
        if not index:
            raise ValueError("Книги с запрашиваемым id не существует")
        return int(index[0])

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

