from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DB']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello, Docker!' AS message")
        result = cursor.fetchone()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
