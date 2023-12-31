Проект интернет-магазина на Python с использованием фреймворка Django. 

Начало работы

Создайте свой файл с переменными окружения .env (шаблон - .env.template).

Если БД не создана, необходимо её создать и заполнить данными, последовательно наберите команды:
1. Перейдите в приложение mysite. Миграции моделей приложения myshop подготовлены:
python manage.py migrate
2. Создайте администратора:
python manage.py createsuperuser
3. Создайте профиль для администратора:
python manage.py create_profile_for_superuser
4. Для создания обычного пользователя наберите команду:
python manage.py create_user
5. Заполните БД изображениями, находящимися в папке /images/:
python manage.py upload_images_to_db
6. Заполнение БД категориями и продуктами происходит через административную панель из файлов csv.
Запустите сайт:
python manage.py runserver.
Наберите http://127.0.0.1:8000/admin/ и зайдите в админ.панель с логином и паролем администратора.
В приложении "MYSHOP" выберите модель "Categorys", нажмите кнопку "IMPORT CSV" и загрузите файл categories.csv. Произошло создание категорий.
После этого в приложении "MYSHOP" выберите модель "Products", нажмите кнопку "IMPORT CSV" и загрузите файл products.csv. Произошло создание товаров.
Сайт готов к работе.


Сайт представляет собой интернет-магазин мебели.

Отображение страниц происходит через приложение diploma-frontend (создано ранее), обращение за данными происходит по
API - приложения myauth (всё, что связано с авторизацией и регистрацией пользователей) и myshop (информация
о товарах и заказах).

Что можно делать на сайте:

Авторизация пользователя происходит по адресу /sign-in/: представление SignInView (приложение myauth);
регистрация - /sign-up/: представление SignUpView (приложение myauth); выход - sign-out: SignOutView (приложение myauth).
По адресу /profile/ находится информация из профиля пользователя: представление ProfileView (приложение myshop); здесь он может изменить свои данные, сменить аватар: представление AvatarView (приложение myshop) и 
изменить пароль: представление ChangePasswordView (приложение myshop).

На главной странице сайта есть три основных раздела.
Первый - три товара из случайных категорий: представление ProductBannersSaleView (приложение myshop);
Второй - товары с лучшим рейтингом: представление ProductsPopularView (приложение myshop);
Третий - товары с ограниченным тиражом: представление ProductsLimitedView (приложение myshop).
Также на главной странице есть выпадающий список "ALL DEPARTMENTS", в котором указаны категории и подкатегории
товаров: представление CategoriesView (приложение myshop).

Каталог товаров находится по адресу catalog/: представление CatalogView (приложение myshop); товары можно фильтровать и сортировать, а также выбирать по тегам (представление TagView - (приложение myshop).

По адресу http: sale/ указаны товары, участвующие в распродаже: представление ProductSaleView
(приложение myshop).

При переходе на страницу любого товара выводится полная информация о нём: представление ProductView
(приложение myshop). Там же указаны отзывы о товаре: представление ReviewView
(приложение myshop); отзывы могут оставлять все пользователи.

Заказы пользователя находятся по адресу /history-order/: представление OrdersView (приложение myshop);
информация о конкретном заказе - orders/<id>/: представление OrderView (приложение myshop).
После оформления заказа его можно оплатить: представление PaymentView (приложение myshop).


Модели находятся в файле myshop/models.py.

Управление моделями производится через административную панель, модели реализованы в файле myshop/admin.py.

На разных страницах сайта отображение моделей необходимо разное - сериализаторы для этих целей реализованы
в файле myshop/serializers.py.

Документация API: JSON-схема находится по адресу api/schema/, конечные точки - api/schema/swagger/.

 
