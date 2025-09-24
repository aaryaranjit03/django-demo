# Django Demo App

A simple web application built with Django, integrated with Supabase (PostgreSQL). The app supports CRUD operations through REST APIs and can be shared publicly using ngrok for easy testing and demos.

---

## Features

* CRUD operations (Create, Read, Update, Delete) via REST API
* Supabase PostgreSQL integration
* Easy local setup with Python
* Public access for demos using ngrok

---

## Tech Stack

* Python 3.x
* Django
* Supabase (PostgreSQL)
* ngrok for public sharing

---

## Setup Instructions

### **Option 1: Access via ngrok (Quick Demo)**

Use the ngrok public URL below to access the app from any device. *(The Django server and ngrok should be running on the host machine.)*

**Realtime Pune Air Quality Time-Series Data:**
[https://5a192fc84626.ngrok-free.app/api/dashboard/pune/](https://5a192fc84626.ngrok-free.app/api/dashboard/pune/)

**API Endpoints for testing via a REST client (Postman, Insomnia, etc.):**

1. **Full city data operations**

```
GET, DELETE, PUT, PATCH
https://5a192fc84626.ngrok-free.app/api/citydata/
```

* Perform operations on the full table of city data.

2. **Manual city data entry**

```
POST
https://5a192fc84626.ngrok-free.app/api/fetch_city/
```

* Body example:

```json
{
  "city_name": "Bengaluru",
  "lat": 12.9716,
  "lon": 77.5946
}
```

* This will manually add an entry to the database for the city of your choosing via the OpenWeatherMap API.

---

### **Option 2: Run from GitHub Repository (Full Setup)**

1. **Clone the repository**

```bash
git clone https://github.com/aaryaranjit03/django-demo.git
cd django-demo
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

Create a `.env` file in the project root with the following content:

```
DATABASE_URL=<your_supabase_database_url>
SECRET_KEY=<your_django_secret_key>
OPENWEATHER_API_KEY=<your_openweather_api_key>
DEBUG=True  # For running locally
```

5. **Run database migrations**

```bash
python manage.py migrate
```

6. **Start the Django server**

```bash
python manage.py runserver
```
* Now, you can perform CRUD operations as explained above, using http://127.0.0.1:8000/api/fetch_city and http://127.0.0.1:8000/api/citydata.

7. **Collect realtime Air Quality data for Pune**

In a separate terminal (or virtual environment instance), run:

```bash
python fetch_pune_loop.py
```

* This will continuously collect realtime data via the OpenWeatherMap API and store it in Supabase.
* To visualize the data, open [http://127.0.0.1:8000/api/dashboard/pune/](http://127.0.0.1:8000/api/dashboard/pune/) in your browser.

---

## Notes

* Ngrok free URLs are temporary; restarting ngrok will change the URL.
* Keep both ngrok and Django server running to maintain public access.
* Ensure your Supabase credentials and OpenWeatherMap API key are correctly set in `.env`.
