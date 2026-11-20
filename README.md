# DA Notes – Backend

REST API for the DA Notes Angular frontend, built with Django and Django REST Framework.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API runs at `http://127.0.0.1:8000/`. CORS is enabled for the Angular dev server (`http://localhost:4200`).

## Endpoints

| Method | URL             | Action                                         |
|--------|-----------------|------------------------------------------------|
| GET    | `/notes/`       | List all notes                                 |
| POST   | `/notes/`       | Create a note                                  |
| GET    | `/notes/<id>/`  | Retrieve a note                                |
| PUT    | `/notes/<id>/`  | Update a note (edit, mark, move to/from trash) |
| DELETE | `/notes/<id>/`  | Delete a note permanently                      |

## Note model

| Field     | Type    | Default |
|-----------|---------|---------|
| `id`      | integer | auto    |
| `title`   | string  | –       |
| `content` | string  | `""`    |
| `marked`  | boolean | `false` |
| `trash`   | boolean | `false` |

## Tests

```sh
python manage.py test
```
