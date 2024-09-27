from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # # пример теста:
    # # обязательно указывать префикс test_
    # # дальше идет название метода, который тестируем add_new_book_
    # # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

### откуда тут какой-то get_books_rating() , который ломает тест?)


    #напиши свои тесты ниже
    #чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего 28 лет в полном одиночестве на необитаемом острове у берегов Америки близ устьев реки Ориноко')
        assert collector.books_genre == {}

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Трудно быть богом')
        collector.add_new_book('Трудно быть богом')
        assert collector.books_genre == {'Трудно быть богом': ''}

    def test_add_new_book_with_zero_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert collector.books_genre == {}

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', 'Фантастика')
        assert collector.get_book_genre('Понедельник начинается в субботу') == 'Фантастика'

    def test_set_book_genre_not_exist_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        collector.set_book_genre('Война и Мир', 'Роман')
        assert collector.books_genre == {'Война и Мир': ''}


    @pytest.mark.parametrize(
        'fantastic, cartoons',
        [
            ['Понедельник начинается в субботу', 'Трудно быть богом'],
            ['Приключения Карандаша и Самоделкина', 'Белоснежка и семь гномов']
        ]
    )
    def test_get_books_with_specific_genre(self, fantastic, cartoons):
        collector = BooksCollector()
        collector.add_new_book(fantastic)
        collector.set_book_genre(fantastic, 'Фантастика')
        collector.add_new_book(cartoons)
        collector.set_book_genre(cartoons, 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Фантастика') == [fantastic]
        assert collector.get_books_with_specific_genre('Мультфильмы') == [cartoons]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Шрек']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        assert collector.favorites == ['Шрек']


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        collector.delete_book_from_favorites('Шрек')
        assert collector.favorites == []

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Шрек', 'Мультфильмы'],
            ['Собака Баскервилей', 'Детективы']
        ]
    )
    def test_get_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name: genre, name: genre}

    @pytest.mark.parametrize('name', ['Пикник на обочине', 'Понедельник начинается в субботу', 'Трудно быть богом', 'Жук в муравейнике'])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Шрек', 'Мультфильмы'],
            ['Приключения Карандаша и Самоделкина', 'Мультфильмы'],
            ['Оно', 'Ужасы']
        ]
    )
    def test_get_books_for_children_no_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.get_books_for_children()
        assert 'Оно' not in collector.get_books_for_children()