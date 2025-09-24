# Django Demo App

A simple web application built with Django, integrated with Supabase (PostgreSQL). The app supports CRUD operations through REST APIs and can be shared publicly using ngrok for easy testing and demos.

---

## Features

- CRUD operations (Create, Read, Update, Delete) via REST API
- Supabase PostgreSQL integration
- Easy local setup with Python
- Public access for demos using ngrok

---

## Tech Stack

- Python 3.x  
- Django  
- Supabase (PostgreSQL)  
- ngrok for public sharing

---

## Setup Instructions

### Option 1: Access via ngrok (Quick Demo)

Use the ngrok public URL provided below to access the app from any device. (The Django server and ngrok should be running on the host machine)

Realtime Pune Air Aquality Time-Series Data: https://5a192fc84626.ngrok-free.app/api/dashboard/pune/

In a REST client (such as Postman), use the following options:
1. https://5a192fc84626.ngrok-free.app/api/citydata/ with GET, DELETE, PUT or PATCH method, to perform operations of the full table of city data.
2. https://5a192fc84626.ngrok-free.app/api/fetch_city/ with POST method, to manually retrieve data from the OpenWeatherMap API. Ensure the body contains city name, latitude and longitude in the following format:

{
  "city_name": "Bengaluru",
  "lat": 12.9716,
  "lon": 77.5946
}

This will manually add an entry to the database for the city of your choosing.

### Option 2: Run from GitHub Repository (Full Setup)

1. Clone the repository

git clone <your_repo_url>
cd <repo_folder>


2. Create and activate a virtual environment

python -m venv venv 

source venv/bin/activate (Linux/macOS)

venv\Scripts\activate (Windows)


3. Install dependencies

pip install -r requirements.txt


4. Set environment variables

Create a .env file with:

DATABASE_URL=<your_supabase_database_url>
SECRET_KEY=<your_django_secret_key>
OPENWEATHER_API_KEY=<your_openweather_api_key>
DEBUG=True (For running locally)


5. Run database migrations

python manage.py migrate


6. Start the Django server

python manage.py runserver


7. Collect Realtime Air Quality Data for Pune

In a separate virtual environment instance, run the following command:

python fetch_pune_loop.py

This will run in a continuous loop, allowing realtime data to be collected via OpenWeatherMap API, and stored in Supabase.
To visualise this data, open http://127.0.0.1:8000/api/dashboard/pune/ in your browser.

