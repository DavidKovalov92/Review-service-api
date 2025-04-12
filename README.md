# Review Service API

# Review Service API — це RESTful API для управління відгуками, категоріями, жанрами, фільмами та користувачами. Проєкт побудований на основі Django та Django REST Framework.

## Встановлення

1. Клонуйте репозиторій:
   ```bash
   git clone <repository_url>
   cd review_service_api

   python -m venv venv
   
   
2.
    ```bash
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
3. ```bash
   pip install -r requirements.txt
4. ```bash
   SECRET_KEY=your_secret_key
5. ```bash
    python manage.py migrate
    python manage.py runserver
### Використання
API доступне за адресою http://127.0.0.1:8000/api/. Основні ендпоінти:

### Користувачі:

> Реєстрація: POST /api/v1/auth/signup/
> Отримання токена: POST /api/v1/auth/token/
> Управління користувачами: GET/POST/PATCH/DELETE /api/v1/users/

### Категорії:

> Список та створення: GET/POST /api/v1/categories/
Видалення: DELETE /api/v1/categories/{slug}/
### Жанри:

> Список та створення: GET/POST /api/v1/genres/
Видалення: DELETE /api/v1/genres/{slug}/
### Фільми:

>Список, створення, оновлення: GET/POST/PATCH /api/v1/titles/
Деталі: GET /api/v1/titles/{id}/
### Відгуки:

>Список та створення: GET/POST /api/v1/titles/{title_id}/reviews/
Деталі: GET/PATCH/DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
### Коментарі:

>Список та створення: GET/POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
Деталі: GET/PATCH/DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

### Особливості
- Аутентифікація за допомогою JWT.
- Розширена система прав доступу.
- Фільтрація, пошук та пагінація для списків.