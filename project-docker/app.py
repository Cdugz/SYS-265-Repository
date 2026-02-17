from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST","db")
DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "password")

def get_db_connection():
	conn = psycopg2.connect(
		host=DB_HOST,
		database=DB_NAME,
		user=DB_USER,
		password=DB_PASS
	)
	return conn

@app.route("/")
def home():
	conn = get_db_connection()
	cur = conn.cursor()
	
	cur.execute("""
		CREATE TABLE IF NOT EXISTS visits (
			id SERIAL PRIMARY KEY,
			visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		);
	""")

	cur.execute("INSERT INTO visits DEFAULT VALUES;")
	
	cur.execute("SELECT * FROM visits;")
	rows = cur.fetchall()

	cur.close()
	conn.commit()
	conn.close()

	output = "<h1>Visit Log</h1>"
	for row in rows:
		output += f"Visit {row[0]} at {row[1]}<br>"

	return output

app.run(host="0.0.0.0", port=5000)
