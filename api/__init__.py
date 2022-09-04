from flask import Flask, jsonify
import psycopg2
from api.models import Restaurant


def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(DATABASE=database, USER=user)

    def connect_to_db():
        conn = psycopg2.connect(
            database=app.config["DATABASE"], user=app.config["USER"]
        )
        return conn

    @app.route("/")
    def index():
        return "Hello World"

    @app.route("/restaurants")
    def show_restaurants():
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurants")
        restaurants = cursor.fetchall()
        restaurant_objs = [
            Restaurant(restaurant).__dict__ for restaurant in restaurants
        ]
        return jsonify(restaurant_objs)

    @app.route("/restaurants/<int:restaurant_id>")
    def show_restaurant(restaurant_id):
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurants WHERE id = %s", (restaurant_id,))
        restaurant = cursor.fetchone()
        return jsonify(Restaurant(restaurant).__dict__)

    return app
