from app import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SignupForm, PostForm
from models import db, Posts
from flask.ext.login import login_required, current_user





@app.route('/', methods=['GET', 'POST'])
def hello_world():
	form = PostForm()
	if request.method == 'POST':
	# if current_user.can(Permission.WRITE_ARTICLES) and \
		if form.validate() == True:
			post = Posts(post=form.post.data, author=current_user._get_current_object())
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('/'))
		else:
			flash('an error occured')
		
		posts = Posts.query.order_by(Posts.timestamp.desc()).all()

	return render_template('home.html', form=form)
		
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = SignupForm()
# 	if request.method == 'POST':
# 		if form.validate() == False:
#             return render_template('signup.html', form=form)
# 		else:
# 			newuser = User(form.username.data, form.email.data, form.password.data)
# 			db.session.add(newuser)
# 			db.session.commit()

# 			session['email'] = newuser.email
# 			return redirect(url_for('home'))

# 	elif request.method == 'GET':
# 		return render_template('signup.html', form=form)

# @app.route('/signup', methods=['GET', 'POST'])
# def home('/index'):
# 	return render_template('index.html')


# ==================Route for home where users can post=================


