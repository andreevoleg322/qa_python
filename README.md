# qa_python

1) test_add_new_book_with_long_name - тест, проверяющий, что книга с названием длиннее 40 символов не добавится
2) test_add_new_book_duplicate - тест, проверяющий, что книга с одним и тем же названием в словарь не добавится
3) test_add_new_book_with_zero_name - тест, проверяющий, что книга с названием длиной 0 символов не добавится
4) test_get_book_genre - тест, проверяющий вывод жанра книги по ее названию
5) test_set_book_genre_not_exist_genre - тест, проверяющий, что нельзя установить книге жанр, если она есть в списке books_genre, а жанр не входит в genre
6) test_get_books_with_specific_genre - тест, проверяющий получение книг с опеределлным жанром
7) test_get_books_for_children - тест, проверяющий получение книг, подходящих для детей
8) test_add_book_in_favorites - тест, проверяющий добавление книги в избранное
9) test_delete_book_from_favorites - тест, проверяющий удаление книги из избранного
10) test_get_books_genre - тест, проверяющий получение словаря 
11) test_get_list_of_favorites_books - тест, проверяющий получение списка избранных книг
12) test_get_books_for_children_no_age_rating - тест, проверяющий, что книг с жанром для взрослых нет в списке книг, подходящих детям
