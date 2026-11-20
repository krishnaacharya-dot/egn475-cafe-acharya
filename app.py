from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample menu data
MENU_ITEMS = [
    {
        "id": 1,
        "name": "Café con Leche",
        "category": "Coffee",
        "price_cents": 350,
        "description": "Espresso blended with steamed milk."
    },
    {
        "id": 2,
        "name": "Cortadito",
        "category": "Coffee",
        "price_cents": 250,
        "description": "Cuban espresso with a small amount of steamed milk."
    },
    {
        "id": 3,
        "name": "Cuban Espresso",
        "category": "Coffee",
        "price_cents": 200,
        "description": "Strong Cuban espresso with sweet crema."
    },
    {
        "id": 4,
        "name": "Guava Pastry",
        "category": "Pastry",
        "price_cents": 300,
        "description": "Flaky pastry filled with sweet guava."
    },
    {
        "id": 5,
        "name": "Croqueta",
        "category": "Snack",
        "price_cents": 250,
        "description": "Traditional Cuban croquette."
    },
    {
        "id": 6,
        "name": "Cuban Sandwich",
        "category": "Food",
        "price_cents": 850,
        "description": "Ham, roasted pork, Swiss cheese, pickles, and mustard."
    }
]

# Sample kitchen orders
KITCHEN_ORDERS = [
    {
        "id": 101,
        "customer": "Maria",
        "items": "Café con Leche, Guava Pastry",
        "status": "Preparing"
    },
    {
        "id": 102,
        "customer": "Carlos",
        "items": "Cuban Sandwich, Cuban Espresso",
        "status": "Ready"
    },
    {
        "id": 103,
        "customer": "Ana",
        "items": "Cortadito, Croqueta",
        "status": "Pending"
    }
]

# Sample order history
ORDER_HISTORY = [
    {
        "id": 101,
        "customer": "Maria",
        "items": "Café con Leche, Guava Pastry",
        "total_cents": 650,
        "status": "Completed"
    },
    {
        "id": 102,
        "customer": "Carlos",
        "items": "Cuban Sandwich, Cuban Espresso",
        "total_cents": 1050,
        "status": "Completed"
    },
    {
        "id": 103,
        "customer": "Ana",
        "items": "Cortadito, Croqueta",
        "total_cents": 500,
        "status": "Pending"
    }
]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Main menu
@app.route("/menu")
def menu():
    return render_template("menu.html", items=MENU_ITEMS)


# Menu item detail
@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next(
        (item for item in MENU_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item_detail.html", item=item)


# New order form
@app.route("/order/new")
def new_order():
    return render_template("order_new.html", items=MENU_ITEMS)


# Kitchen board
@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html", orders=KITCHEN_ORDERS)


# Order history
@app.route("/orders")
def order_history():
    return render_template("orders.html", orders=ORDER_HISTORY)


if __name__ == "__main__":
    app.run(debug=True)