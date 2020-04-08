#BookStore project


Создать небольшое веб-приложение : маркетплейс книжных магазинов.
Модель данных: Магазин - Книги.

Опишем Магазин: 
1) Название
2) ИНН
3) электронная почта
4) Пароль для входа 
5) Связь с книгами этого магазина


Опишем Книгу:
1) Автор
2) Название 
3) Номер склада, где она хранится
4) Поле, связывающее эту книгу с магазином


@login_required
/home ---> Отображает все имеющиеся в базе данных книги в формате :
"Store_name содержит книгу: Book_author Book_name и хранит ее в Номер_склада"

/login (аутентификация объекта МАГАЗИН)
/logout
/register (регистрация объекта МАГАЗИН)