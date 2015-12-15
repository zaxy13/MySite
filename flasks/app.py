from flask import Flask, jsonify, render_template, request, url_for, redirect
from libz import jsonPosts
from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required


class simpleTextform(Form):
    post = TextField('post', validators=[Required()])


data = jsonPosts.Loader("test.json")
app = Flask(__name__,  instance_relative_config=True)
app.config.from_pyfile('config.py')


# todo, add post system
posts = data.posts


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('home.html', posts=posts)

@app.route('/postnew', methods=["GET", "POST"])
def postnew():
	form = simpleTextform()
	if form.validate_on_submit():
		newPost = form.post.data
		buff = {"name":str(newPost)}
		data.posts.append(buff)
		return redirect(url_for('index'))
	return render_template('postnew.html', form=form)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/data')
def names():
	data = {"names":['bob','joe','cindy','dina']}
	return jsonify(data)

if __name__ == '__main__':
	app.debug = True
	
	app.run()
