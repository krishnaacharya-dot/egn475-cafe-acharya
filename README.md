# Café Calle Ocho — Flask Prototype

## EGN 475 Week 3 Assignment 3.1

This project is a Flask-based prototype for Café Calle Ocho, a Cuban-inspired café located in Miami, Florida. It transforms the Week 2 static HTML mockup into a working web application with multiple pages, shared navigation, and sample data.

## Features

- Home page introducing Café Calle Ocho
- Menu page displaying café items
- Individual menu item detail pages
- Order form prototype
- Kitchen order dashboard
- Order history page
- Shared navigation using Jinja template inheritance
- Dynamic content rendered from Python sample data
- Detail route with an integer URL converter
- 404 response for nonexistent menu items

## Technologies Used

- Python
- Flask
- Jinja2
- HTML
- Pico CSS
- Git and GitHub

## Project Structure

```text
egn475-cafe-acharya/
├── app.py
├── requirements.txt
├── .gitignore
├── static/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── menu.html
│   ├── item_detail.html
│   ├── order_new.html
│   ├── kitchen.html
│   └── orders.html
└── mockup/
```

## Installation and Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Start the Flask application:

```bash
flask --app app run --debug
```

5. Open the application in your browser at:

```text
http://127.0.0.1:5000/
```

## Screens

- Home
- Menu
- Menu Item Details
- Place Order
- Kitchen Dashboard
- Order History

## Project Status

This is a prototype developed for EGN 475 Week 3 Assignment 3.1. The application uses sample data stored in Python lists and dictionaries. Database integration and actual order processing will be introduced in a future assignment.

## Author

Krishna Acharya
