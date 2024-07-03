# Live Streaming Platform

This project is a live streaming platform where users can create, view, and manage live streams. The backend is built using Django Rest Framework.

## Features

- User registration and authentication.
- Create live stream events.
- View active live streams.
- Interact with live streams.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework
- SQLite (default) or PostgreSQL (recommended for production)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kumarawanish/livestreaming.git
   cd livestreaming

2. Create and activate a virtual environment:
    python -m venv stream_env
    source stream_env/bin/activate

3. Install the required packages:
    pip install -r requirements.txt

4. Apply migrations:
    python manage.py migrate

5. Create a superuser for the Django admin:

    python manage.py createsuperuser

6. Run the development server:
     
    python manage.py runserver

## API Endpoints

# User Endpoints
Register a new user: POST /api/register/

Request body: { "username": "user", "password": "password", "email": "email@example.com" }

Obtain authentication token: POST /api/token/

Request body: { "username": "user", "password": "password" }

Response: { "token": "token", "user_id": 1, "email": "email@example.com" }

# Live Stream Endpoints

List active live streams: GET /api/streams/

Create a live stream: POST /api/streams/create/ (Authenticated)

Request body: { "title": "Stream Title", "description": "Stream Description" }


Retrieve /api/streams/<int:pk>/ (Authenticated)

## Authentication

The project uses token-based authentication provided by Django Rest Framework's built-in token authentication. Obtain a token by posting the user's credentials to the /api/token/ endpoint.
