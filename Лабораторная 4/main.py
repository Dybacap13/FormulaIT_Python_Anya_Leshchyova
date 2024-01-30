import json

class  ApolloStore:
    """ Документация на класс.
    Класс описывает инвентарь магазина Апполон - название товара,
    его стоимость и текущий статус (продан, добавлен, в наличии и тп)"""

    DATABASE_FILE_FULL = "database_full.json"  # для всех экземплярод должен быть один файл записи
    database = []  # чтобы хранить информацию о всех созданных экземплярах

    def __init__(self, product: str, cost: float, status="add"):
        """ Инициализация экземпляра класса."""
        self.product = product
        self.cost = cost
        self.status = status

    @property
    def cost(self) -> float:
        """Getter параметра cost"""
        return self._cost
    @cost.setter
    def cost(self, value: float):
        """Setter параметра cost"""
        if not isinstance(value, float):
            raise TypeError("Стоимость типа float")
        if value < 0:
            raise ValueError("Стоимость > 0")
        self._cost = value

    @property
    def status(self) -> str:
        """Getter параметра status"""
        return self._status

    @status.setter
    def status(self, value: str):
        """Setter параметра status"""
        if not isinstance(value, str):
            raise TypeError("Статус типа str")
        if not value:
            raise ValueError("Запишите статус")
        self._status = value

    @property
    def product(self) -> str:
        """Getter параметра product"""
        return self._product

    @product.setter
    def product(self, value: str):
        """Setter параметра product"""
        if not isinstance(value, str):
            raise TypeError("Название товара типа str")
        if not value:
            raise ValueError("Запишите название товара")
        self._product = value

    def __str__(self):
        return f"Product: {self.product} , Cost: {self.cost}, Status: {self.status}"

    def __repr__(self):
        return f"{self.__class__.__name__}(product={self.product!r}, cost={self.cost}, status={self.status})"

    @classmethod
    def number_products_in_database(cls) -> int:
        """ Возвращает количество товаров в базе.
            Наследуется.
            Метод класса - потому что работает с базой данных всех созданных экземпляров
        """
        return len(cls.database)

    @classmethod
    def summ_products(cls) -> float:
        """ Возвращает полную стоимость всех товаров в базе.
            Наследуется.
            Метод класса - потому что работает с базой данных всех созданных экземпляров
        """
        sum_ = 0
        for i in cls.database:
            sum_ += i["Cost"]
        return sum_

    @classmethod
    def save_database(cls):
        """ Записывает базу в файл
            Наследуется
        """
        with open(cls.DATABASE_FILE_FULL, 'w', encoding='utf-8') as f:
            json.dump(cls.database, f, indent=4)

    @staticmethod
    def read_database(name_file):
        """ Читает файл базы и выводет в приятном виде

            :param name_file: Имя файла

            Стаический, потому что работает только с переданным файлом

        """
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                print(i)

    def add_database(self, product: str, cost: float, status: str):
        """ Записывает текущий товар в базу
            при вызове метода для созданного экземпляра ( например магазина)

            :param product: Имя товара
            :param cost: Стоимость товара
            :param status: Статус товара

            Перегружается - у дочернего класса есть дополнительные параметры
        """
        # Необходимо для проверки
        self.product = product
        self.cost = cost
        self.status = status

        dist = {
            "Product": self.product,
            "Cost": self.cost,
            "Status": self.status,
        }
        self.database.append(dist)

    def check_profit(self, expenses: float) -> float:
        """ Возвращает доходы магазина, если база пуста - вернет ноль

            :param expenses  - расходы
        """
        if (self.number_products_in_database() == 0):
            return 0
        return self.summ_products() - expenses

class ClothingApolloStore(ApolloStore):
    """
    Документация на класс.
    Дочерний класс класса ApolloStore
    Хранит в себе товары - одежду, имеет дополнительные параметры ( модель и размер)
    Созраняет параметры основного гласса ( название товара, стоимость и статус)
    """

    def __init__(self, model: str, size: int, product: str , cost: float, status="add" ):
        """ Инициализация экземпляра класса. """
        self.model = model
        self.size = size
        super().__init__(product, cost, status)


    @property
    def model(self) -> str:
        """Getter параметра model"""
        return self._model

    @model.setter
    def model(self, value):
        """Setter параметра model"""
        if not isinstance(value, str):
            raise TypeError("value must can str")
        if not value:
            raise ValueError("Запишите модель одежды")
        self._model = value

    @property
    def size(self) -> int:
        """Getter параметра size"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter параметра size"""
        if not isinstance(value, int):
            raise TypeError("value must can str")
        if value < 0:
            raise ValueError("size > 0")
        self._size = value


    def add_database(self, model: str, size: int, product: str , cost: float, status: str):
        """ Записывает текущий товар в базу
            при вызове метода для созданного экземпляра ( например магазина)

            :param product: Имя товара
            :param cost: Стоимость товара
            :param status: Статус товара
            :param model: Модель одежды
            :param size: Размер одежды

            Перегружается - у дочернего класса есть дополнительные параметры
        """
        #  Нужно для проверки переданных значений
        self.product = product
        self.cost = cost
        self.status = status
        self.model = model
        self.size = size

        dist = {
            "Product": self.product,
            "Cost": self.cost,
            "Status": self.status,
            "Model": self.model,
            "Size": self.size,

        }
        self.database.append(dist)

    def __str__(self):
        return f"Product: {self.product} , Cost: {self.cost}, Status: {self.status}, Model: {self.model}, Size: {self.size}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model}, size={self.size}, product={self.product!r}, cost={self.cost}, status={self.status})"




if __name__ == '__main__':
    #  Для заполнения файла и теста
    appolo_store_clohting = ClothingApolloStore("Adidas", 53, "Джинсы мужские", 3500.0, "add")
    appolo_store_clohting.add_database("Adidas", 50, "Футболка мужская", 1500.0, "add")
    appolo_store_clohting.add_database("Puma", 42, "Кросовки мужские", 5500.0, "add")
    appolo_store_clohting.add_database("JG", 36, "Джинсы женские", 2500.0, "add")
    appolo_store_clohting.add_database("JG", 46, "Куртка женская", 6000.0, "add")
    appolo_store_clohting.save_database()
    appolo_store_clohting.read_database(appolo_store_clohting.DATABASE_FILE_FULL)

    """
    ---
    {'Product': 'Футболка мужская', 'Cost': 1500.0, 'Status': 'add', 'Model': 'Adidas', 'Size': 50}
    {'Product': 'Кросовки мужские', 'Cost': 5500.0, 'Status': 'add', 'Model': 'Puma', 'Size': 42}
    {'Product': 'Джинсы женские', 'Cost': 2500.0, 'Status': 'add', 'Model': 'JG', 'Size': 36}
    {'Product': 'Куртка женская', 'Cost': 6000.0, 'Status': 'add', 'Model': 'JG', 'Size': 46}

    """