from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lonqui',
    'salary': '100 pesos'
  },
  {
    'id': 2,
    'title': 'Cercenador de cabezas',
    'location': 'Temuco',
    'salary': '50 pesos'
  },
  {
    'id': 3,
    'title': 'Aweonador PRO',
    'location': 'Banana DOMINICANA',
    'salary': '1 pesos'
  },
  {
    'id': 4,
    'title': 'Comedor de caca',
    'location': 'NYC',
    'salary': '0 pesos'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
