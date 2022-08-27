from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def connect_to_db():
    conn = psycopg2.connect(database="restaurants", user="ryando")
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
    return jsonify(restaurants)


@app.route("/restaurants/<int:restaurant_id>")
def show_restaurant(restaurant_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurants WHERE id = %s", (restaurant_id,))
    restaurant = cursor.fetchone()
    return jsonify(restaurant)


app.run(debug=True)
