# Library API

A RESTful API for managing a library system with user authentication, book borrowing, and reminder functionality. Built with Django, Django REST Framework, Celery, and Redis. Fully containerized with Docker.

## 🚀 Features

- 🔐 JWT Authentication with custom permissions and role-based access
- 📖 Book management (create, update, delete, list)
- 📅 Borrowing system with due dates and return tracking
- 🔔 Telegram reminders for overdue books using Celery + Redis
- ⚙️ Asynchronous task handling via Celery workers
- 🐳 Dockerized for easy local development and deployment
- 🧪 Ready for testing and API documentation

## 🛠️ Tech Stack

- Python 3.11  
- Django 4.x  
- Django REST Framework  
- PostgreSQL  
- Redis  
- Celery  
- Docker & Docker Compose  
- JWT (via `djangorestframework-simplejwt`)

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/IllyaKovaliuk/library_API.git
   cd library_API
2. Create .env file (example below)
3. **Build and start the project**
    ```bash
    docker-compose up --build
4. **Run migrations and create superuse**
    ```bash
   docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser

Author
Illya Kovaliuk
Junior Backend Developer | Python, Django, DRF
