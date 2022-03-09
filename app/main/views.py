from turtle import title
from unicodedata import category
from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import current_user, login_required
from ..models import User, Post, Reaction, PostLike
from .forms import UpdateProfile, PostForm, CommentForm
from .. import db,photos

@main.route("/")
def index():

    
    home = request.args.get('page', 1, type=int)
    pitches = Post.query.order_by(Post.posted_date.desc()).all()
    return render_template('index.html', home = home, pitches = pitches)

@main.route("/post/new", methods=['GET', 'POST'])
def new_pitch():
    pitch_form = PostForm()
    if pitch_form.validate_on_submit():
        pitch = Post(title = pitch_form.title.data, category = pitch_form.category.data,
               post = pitch_form.post.data, by = current_user)

        db.session.add(pitch)
        db.session.commit('You have successfully posted your pitch', 'success')
        return redirect(url_for('index'))
    else:
        pitch = Post.query.order_by(Post.posted_date ).all()
    return render_template('new_pitch.html', title='New Pitch', pitch_form=pitch_form, legend='New Pitch',pitch=pitch)
        



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_pitches():


    return render_template('pitches.html',)

