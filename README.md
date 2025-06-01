# Django REST Framework Learning Project

This project is a hands-on learning exercise to understand and practice Django REST Framework fundamentals. It implements a simple Patient management API to demonstrate core DRF concepts.

## 📚 Learning Purpose

This project was created specifically to learn and practice:
- Django REST Framework setup and configuration
- API view creation with function-based views
- Serializers for data validation and transformation
- HTTP methods handling (GET, POST, PUT)
- Error handling and status codes

## 🛠️ Prerequisites

- Python 3.8+
- pip (Python package installer)

## 🚀 Django REST Framework Initialization

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install Django and Django REST Framework
pip install django
pip install djangorestframework

# Or install from requirements.txt if available
pip install -r requirements.txt
```

### 3. Create Django Project

```bash
# Create Django project
django-admin startproject your_project_name .

# Create Django app
python manage.py startapp patients
```

### 4. Configure Django Settings

Add to your `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Add Django REST Framework
    'patients',        # Add your app
]

# Optional: REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
```

### 5. Run Migrations

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## 📡 API Endpoints

### Patients API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients/` | List all patients |
| POST | `/api/patients/` | Create a new patient |
| GET | `/api/patients/{id}/` | Get a specific patient |
| PUT | `/api/patients/{id}/` | Update a specific patient |

## 🧪 Testing the API

### Using curl

```bash
# Get all patients
curl -X GET http://127.0.0.1:8000/api/patients/

# Create a new patient
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30}'

# Get a specific patient
curl -X GET http://127.0.0.1:8000/api/patients/1/

# Update a patient
curl -X PUT http://127.0.0.1:8000/api/patients/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "age": 31}'
```

### Using Insomnia/Postman

1. Set the base URL to `http://127.0.0.1:8000`
2. Add `/api/patients/` or `/api/patients/{id}/` to the endpoint
3. Set appropriate HTTP method (GET, POST, PUT)
4. For POST/PUT requests, set Content-Type to `application/json`
5. **Important**: Always include trailing slash (`/`) in URLs

## 📁 Project Structure

```
rest-framework/
├── patients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── your_project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── venv/
└── README.md
```

## 🎯 Learning Objectives Covered

- ✅ Django REST Framework installation and setup
- ✅ Creating API views with `@api_view` decorator
- ✅ Implementing serializers for data validation
- ✅ Handling different HTTP methods (GET, POST, PUT)
- ✅ Error handling with try-catch blocks
- ✅ Using `raise_exception=True` for automatic error responses
- ✅ Understanding Django URL patterns
- ✅ Working with database models

## 📝 Notes

- This is a learning project and should not be used in production
- Error handling is basic and can be improved
- Authentication and permissions are not implemented
- Database is SQLite (default Django database)

## 🤝 Contributing

This is a personal learning project. Feel free to fork and experiment with your own modifications!

---

**Happy Learning! 🚀** 