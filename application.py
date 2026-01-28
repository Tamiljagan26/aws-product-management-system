import os
import pymysql
from flask import Flask

application = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306)),
        connect_timeout=5
    )

@application.route("/")
def home():
    return "App is running and ready to connect to DB!"

@application.route("/db-test")
def db_test():
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
        conn.close()
        return f"DB Connection SUCCESS: {result}"
    except Exception as e:
        return f"DB Connection FAILED: {str(e)}", 500

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
