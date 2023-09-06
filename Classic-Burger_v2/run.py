from apps.routes import app
from apps import db
from apps.models import Item

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        items = [
            Item(name="Barbecue Salad", description="Delicious Dish", price=200, source="plate1.png"),
            Item(name="Salad with Fish", description="Delicious Dish", price=150, source="plate2.png"),
            Item(name="Spinach Salad", description="Delicious Dish", price=100, source="plate3.png"),
            Item(name="Fresh Salad", description="Delicious Dish", price=200, source="salad.png"),
            Item(name="Fried Noodles", description="Delicious Dish", price=200, source="noodles.png"),
            Item(name="Roasted Chicken", description="Delicious Dish", price=300, source="chicken.png"),
            Item(name="Cheese Pizza", description="Delicious Dish", price=200, source="pizza.png"),
            Item(name="Barbecue Salad", description="Delicious Dish", price=200, source="plate1.png"),
            Item(name="Salad with Fish", description="Delicious Dish", price=150, source="plate2.png")
        ]

        # Add all items to the session
        db.session.add_all(items)

        # Commit the changes to the database
        db.session.commit()

        

        # Run the Flask app in debug mode
        app.run(debug=True)




