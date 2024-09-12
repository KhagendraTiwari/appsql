from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Database configuration from environment variables
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

@app.route('/')
def index():
    return "Hello, this is a Dockerized Flask application!"

@app.route('/db')
def test_db():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        return jsonify({"message": "Connected to database", "database": db_name})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
