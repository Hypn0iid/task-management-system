# Task Management System

## Introduction

This is a Django project developed for managing tasks

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python (version 3.6 or higher)
- Pip (Python package manager)
- Pipenv (optional, but recommended for managing virtual environments)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Hypn0iid/task-management-system.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd taskmanagementsystem
    ```

3. **Install dependencies:**

    ```bash
    pipenv install
    ```

4. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

5. **Configure the database:**

    Open `taskmanagementsystem/settings.py` and configure the `DATABASES` setting according to your database setup (e.g., SQLite, PostgreSQL, MySQL).

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (optional, but recommended):**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

9. **Access the project:**

    Open a web browser and go to `http://localhost:8000`.