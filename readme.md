## Тестовое задание

[Описание задачи](task.md)

#### Запуск решения:

```bash
$ git clone ...
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
#### Генерация данных:

```bash
$ python populate.py --n=300 
```

#### Запуск тестов:

```bash
$ python manage.py test 
```

Посмотреть примеры запросов к API можно в тестах или [импортировать коллекцию для postman](test_task.postman_collection.json)