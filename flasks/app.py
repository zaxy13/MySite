from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/data')
def names():
	data = {"names":['bob','joe','cindy','dina']}
	return jsonify(data)

if __name__ == '__main__':
	app.run()

