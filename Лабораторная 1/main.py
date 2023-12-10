# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Triangle:
    def __init__(self, side_1: Union[int, float],
                 side_2: Union[int, float], side_3: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side_1: Первая сторона треугольника
        :param side_2: Вторая сторона треугольника
        :param side_3: Третья сторона треугольника

        Примеры:
        >>> triangle = Triangle(3,5,4)  # инициализация экземпляра класса
        """
        self.check_paramets(side_1)
        self.check_paramets(side_2)
        self.check_paramets(side_3)

        self.check_triangle(side_1, side_2, side_3)
        self.check_triangle(side_2, side_3, side_1)
        self.check_triangle(side_3, side_1, side_2)

        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3


    def check_paramets(self, side: Union[int, float]) -> None:
        """
        Проверка стороны треугольника

        :param side: Сторона треугольника
        :raise ValueError: Если сторона меньше или равна нулю
        :raise TypeError: Если сторона не является целым или дробным числом

        :return: None

        Примеры:
        >>> triangle = Triangle(3,3,3)
        >>> triangle.check_paramets(3)
        """
        if not isinstance(side, (int, float)):
            raise TypeError
        if not side > 0:
            raise ValueError


    def check_triangle(self, side_1: Union[int, float], side_2: Union[int, float],
                       side_3: Union[int, float]) -> None:
        """
        Проверка существования треугольника

        :param side_1: Первая сторона треугольника
        :param side_2: Вторая сторона треугольника
        :param side_3: Третья сторона треугольника
        :raise ValueError: Если сумма двух сторон меньше третьей стороны

        :return: None

        Примеры:
        >>> triangle = Triangle(3,3,3)
        >>> triangle.check_triangle(3,3,3)
        """
        if(side_1 + side_2 <= side_3):
            raise ValueError('Triangle is impossible')


    def equilateral_triangle(self) -> bool:
        """
        Функция которая проверяет является треугольник равносторонним

        :return: Является ли треугольник равносторонним

        Примеры:
        >>> triangle = Triangle(3,3,3)
        >>> triangle.equilateral_triangle()
        """
        ...


    def isosceles_triangle(self) -> bool:
        """
        Функция которая проверяет является треугольник равнобедренным

        :return: Является ли треугольник равнобедренным

        Примеры:
        >>> triangle = Triangle(4,3,3)
        >>> triangle.isosceles_triangle()
        """
        ...


    def square(self) -> Union[int, float]:
        """
        Функция которая возвращает площадь треугольника

        :return: Площадь треугольника

        Примеры:
        >>> triangle = Triangle(4,5,3)
        >>> triangle.isosceles_triangle()
        """
        ...


class MortgageCalculation:
    def __init__(self, name: str, mortgage_size: int, monthly_income: int, percent: float):
        """
        Создание и подготовка к работе объекта "Канкулятор Ипотеки"

        :param name: Имя клиента
        :param mortgage_size: Размер ипотеки
        :param monthly_income: Месячный доход
        :param percent: Процент ипотеки


        Примеры:
        >>> mortgage = MortgageCalculation("Alice", 500000, 20000, 0.02)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(monthly_income, int):
            raise TypeError
        if not isinstance(mortgage_size, int):
            raise TypeError
        if not isinstance(percent, float):
            raise TypeError
        if mortgage_size < 0 or monthly_income < 0 or percent < 0:
            raise ValueError
        self.name = name
        self.mortage_size = mortgage_size
        self. monthly_income = monthly_income


    def monthly_payment_calculation (self, year:int) ->int:
        """
        Функция которая считает ежемесячный платёж в зависимости от лет выплат
        :param  year: Время выплаты ипотеки (годы)

        :return: Ежемесячный платёж

        Примеры:
        >>> mortgage = MortgageCalculation("Alice", 500000, 20000, 0.02)
        >>> mortgage.monthly_payment_calculation(10)
        """
        ...


    def duration_calculation(self, monthly_payment) -> int:
        """
        Функция которая считает срок выплаты ипотеки в зависимости от ежемесячного платежа
        :param  monthly_payment: Ежемесячный платёж

        :return: Время выплаты ипотеки (годы)

        Примеры:
        >>> mortgage = MortgageCalculation("Alice", 500000, 20000, 0.02)
        >>> mortgage.duration_calculation(10000)
        """
        ...


    def percentage_increase(self, new_percent: float) -> float:
        """
        Функция которая считает увеличение процента
        :param new_percent: На сколько увеличить процент

        :return: Увеличенный процент

        Примеры:
        >>> mortgage = MortgageCalculation("Alice", 500000, 20000, 0.02)
        >>> mortgage.percentage_increase(0.01)
        """
        ...


class ShoppingCalculator:
    def __init__(self, total_amount_money: int):
        """
        Создание и подготовка к работе объекта "Канкулятор Покупок"

        :param total_amount_money: Максимальна сумма денег

        Примеры:
        >>> shopping = ShoppingCalculator(10000)  # инициализация экземпляра класса
        """
        if not isinstance(total_amount_money, int):
            raise TypeError
        if total_amount_money < 0:
            raise ValueError
        self.shopping_list = { }
        self.total_sum = 0


    def add_purchase (self,product: str, cost: float) -> None:
        """
        Функция которая добавляет товар в список покупок
        :param product: Товар
        :param cost:Стоимость товара

        :return:None

        Примеры:
        >>> shopping = ShoppingCalculator(10000)
        >>> shopping.add_purchase("Apple", 200)
        """
        ...


    def remove_purchase(self,product: str) -> None:
        """
        Функция которая удаляет товар из списока покупок
        :param product: Товар

        :return:None

        Примеры:
        >>> shopping = ShoppingCalculator(10000)
        >>> shopping.remove_purchase("Apple")
        """
        ...


    def checking_enoug_money(self) -> bool:
        """
        Функция которая проверяет достаточно ли денег на текущие покупки

        :return: Достаточно ли денег

        Примеры:
        >>> shopping = ShoppingCalculator(10000)
        >>> shopping. checking_enoug_money()
        """
        ...


    def show_expenses (self) -> int:
        """
        Функция которая выдаёт итоговую стоимость текущих покупок

        :return: Итоговая стоимость текущих покупок

        Примеры:
        >>> shopping = ShoppingCalculator(10000)
        >>> shopping.show_expenses()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
