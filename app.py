from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="your-rds-endpoint",
        database="yourdbname",
        user="yourusername",
        password="yourpassword"
    )

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO test (value) VALUES (%s)", (data['value'],))
    conn.commit()
    cur.close()
    conn.close()
    return "Data added!", 200

@app.route('/view')
def view():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)
