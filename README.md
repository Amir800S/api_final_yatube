# API Yatube
### Через API Yatube возможно создание, редактирование, просмотр, удаления постов, комментариев и управление подписками в соц.сети Yatube
Использованные технологии:
- Python 3.9,
- Django 3.2,
- DRF,
- JWT & Djoser

### Как пользоваться API?
Клонируем репозиторий:
```python
git clone https://github.com/Amir800S/api_final_yatube.git
```
Создаем и активируем виртульное окружение в терминале:
```python
python -m venv venv
```
```python
venv/Scripts/activate
```
Далее установка зависимостей:
```python
pip install -r requirements.txt
```
Запускаем сервер:
```python
python manage.py runserver
```
### Проект готов к работе
Примеры отправки GET-запросов 
```python
http://127.0.0.1:8000/api/v1/posts/  # Все посты соц.сети
http://127.0.0.1:8000/api/v1/posts/{Номер поста}/  # Определенный пост
http://127.0.0.1:8000/api/v1/posts/{Номер поста}/comments/  # Все комменты определенного поста 
```
### * ДЛЯ POST, DELETE, PUT, PATCH запросов необходима аутентификация!!! 
Пример как отправить POST-запрос
```python
http://127.0.0.1:8000/api/v1/posts/
```
```python
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа с 201 кодом
```python
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
## Как получить `JWT-токен`?
```python
http://127.0.0.1:8000/api/v1/jwt/create/
```
В Payload:
```python
{
"username": "string",
"password": "string"
}
```
Токен получен! 
```python
{
  "refresh": "string",
  "access": "string"
}
```
### *Автор: Сабуров Амир* 
