# 💭 SPA Comments Application

This project allows users to leave comments, which are then stored in a
relational database, including user identification data. The implementation
adheres to the specified requirements and incorporates essential features.

## 🚀 Getting Started

### ⚙️ Installing via GitHub

- Python 3 must be installed
- Create .evn using .env.sample
- Specify `DB_TYPE=sqlite` inside `.env` to be able to run localy
- Run these commands:
    ```bash
    git clone https://github.com/eduardhabryd/django-spa-comments.git
    cd django-spa-comments
    python -m venv venv
    source venv/bin/activate # or venv\Scripts\activate in Windows
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata fixture.json
    python manage.py runserver
    ```

### Run with Docker 🐳

To run the project using Docker, follow these steps:

- Clone and open folder in terminal:

    ```bash
    git clone https://github.com/eduardhabryd/django-spa-comments.git
    cd django-spa-comments
    ```

- Install Docker if it's not already installed. You can download it from [here](https://www.docker.com/products/docker-desktop).
- Create a `.env` file using `.env.sample` and specify `DB_TYPE=postgres` inside the `.env` to run the project with Docker.
- Run the following command to build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

### 🌟 Key Features

- Users can leave comments and comment for comments (cascading comments)
- Captcha for creating comments form
- SQLite database for local run
- PostgreSQL database for run with Docker
- Sort by username, date, or email

### 🪟 Demo