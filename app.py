from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Private\\Flask\\blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	content = db.Column(db.String(255))
	date_created = db.Column(db.Text)

@app.route('/')
def index():
	posts = Blogpost.query.order_by(Blogpost.date_created.desc()).all()
	return render_template('index.html',posts=posts)

@app.route('/addpost')
def addpost():
	return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
	post = Blogpost.query.filter_by(id=post_id).one()
	return render_template('post.html',post=post)

@app.route('/add',methods=['POST'])
def add():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content = request.form['content']

	post = Blogpost(title=title,subtitle=subtitle,author=author,content=content,date_created=datetime.now())

	db.session.add(post)
	db.session.commit()

	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

