# Little Lemon Restaurant API
 
A Django REST API for the Little Lemon restaurant, built as the capstone project for the Meta Back-End Developer Professional Certificate. The API supports menu management and table booking, with token-based authentication and a MySQL database backend.
 
## Features
 
- **Menu API** — full CRUD for menu items (title, price, inventory)
- **Table Booking API** — full CRUD for bookings (name, number of guests, booking date)
- **User authentication** — registration, login, and logout via [Djoser](https://djoser.readthedocs.io/), with token-based auth securing the Booking API
- **Unit tests** — model and view tests using Django's test framework
- **MySQL** — production-style relational database backend (instead of SQLite)
## Tech Stack
 
- Python / Django
- Django REST Framework
- Djoser (authentication)
- MySQL
## Setup
 
1. Clone the repository:
```
   git clone https://github.com/awjenson/LittleLemon.git
   cd LittleLemon
```
 
2. Create and activate a virtual environment:
```
   python3 -m venv .venv
   source .venv/bin/activate
```
 
3. Install dependencies:
```
   pip3 install django djangorestframework djoser mysqlclient
```
 
4. Set up MySQL:
   - Install and start MySQL locally.
   - Create the database:
```sql
     CREATE DATABASE LittleLemon;
```
   - Update the `DATABASES` section in `littlelemon/settings.py` with your MySQL credentials.
5. Run migrations:
```
   python manage.py migrate
```
 
6. Create a superuser:
```
   python manage.py createsuperuser
```
 
7. Start the development server:
```
   python manage.py runserver
```
 
## API Endpoints
 
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/restaurant/menu/` | List all menu items / create a new one |
| GET, PUT, DELETE | `/restaurant/menu/<id>` | Retrieve, update, or delete a single menu item |
| GET, POST | `/restaurant/booking/tables/` | List all bookings / create a new one (requires authentication) |
| GET, PUT, DELETE | `/restaurant/booking/tables/<id>/` | Retrieve, update, or delete a single booking (requires authentication) |
| POST | `/auth/users/` | Register a new user |
| POST | `/auth/token/login/` | Log in and obtain an auth token |
| POST | `/auth/token/logout/` | Log out (invalidate token) |
| POST | `/api-token-auth/` | Obtain an auth token (alternative endpoint) |
 
## Authentication
 
The Booking API requires a valid auth token. After logging in, include the token in the `Authorization` header of your requests:
 
```
Authorization: Token <your-token-here>
```
 
## Running Tests
 
```
python manage.py test
```
 
## Admin Panel
 
Django's built-in admin interface is available at `/admin/` for managing menu items, bookings, and users directly.