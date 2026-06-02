from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "companydb")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/api/jobs")
def get_jobs():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT id, role, location FROM jobs")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    jobs = []

    for row in rows:
        jobs.append({
            "id": row[0],
            "role": row[1],
            "location": row[2]
        })

    return jsonify(jobs)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)