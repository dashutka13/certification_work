Платформа торговой сети электроники для разворачивания в docker-compose.
#### Для разворачивания образа вам потребуется
1. Клонировать репозиторий.
2. Выключить базу Postgres "sudo systemctl stop postgresql"
3. Запустить команду "sudo docker-compose build"
4. Запустить команду "sudo docker-compose up"
5. Если приложение не запустилось то:
sudo docker-compose exec db psql -U postgres
create database BulletinBoard 
sudo docker-compose down
6. Повторить пункт 4.
7. Апи доступно по адресу http://127.0.0.1:8001/docs/


## Backend api Retail_platform
1. Регистрация позьзователей, авторизация, удаление.
2. Создание поставщиков и взаимодействие с ними(изменение, удаление).
3. Создание продуктов поставщиков и взаимодействие с ними(изменение, удаление).