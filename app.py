from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the web app!"

@app.route("/data")
def data():
    try:
        conn = psycopg2.connect(
            dbname="myappdb",
            user="postgres",
            password="Gultac2004",
            host="db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM example;")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1010)
