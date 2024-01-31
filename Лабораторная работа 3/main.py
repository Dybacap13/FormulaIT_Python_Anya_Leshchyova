class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str) or not isinstance(author, str):
            raise TypeError("param must can str")
        self._name = name
        self._author = author
    
        

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"
    @property
    def prop_pages(self) -> int:
        return self.pages

    @prop_pages.setter
    def prop_pages(self, value):
        if not isinstance(value, int):
            raise TypeError("value must can int")
        if value < 0:
            raise ValueError("pages > 0")
        self.pages = value

    # Можно унаследовать, если не важно количество страниц
    #def __str__(self):
    #    return f"Печатная {super().__str__()} Страниц {self.pages}"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    @property
    def prop_duration(self) -> float:
        return self.duration

    @prop_duration.setter
    def prop_duration(self, value):
        if not isinstance(value, float):
            raise TypeError("value must can float")
        if value < 0:
            raise ValueError("duration > 0")
        self.duration = value

    # Можно унаследовать, если не важна длительность
    #def __str__(self):
    #    return f"Аудио {super().__str__()}  Длительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

