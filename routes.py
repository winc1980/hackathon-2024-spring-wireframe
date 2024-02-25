from flask import render_template, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email ,EqualTo
from werkzeug.security import check_password_hash

from . import app, db, login_manager
from .models import User, Post, Favorite, Mission, Follow

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# signup_login
@app.route('/entry', methods=['GET', 'POST'])
def entry():
    # すでにログイン済みの場合
    if current_user.is_authenticated:
        return redirect(url_for('timeline'))

    signup_form = SignupForm()
    login_form = LoginForm()

    # サインアップフォームを送られた時の処理
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            return redirect(url_for('timeline'))

        new_user = User(
            username = username,
            email = email,
        )

        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('timeline'))

    # ログインフォームが送られた時の処理
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('timeline'))

    return render_template('signup_login.html', signup_form=signup_form, login_form=login_form)

# timeline
# profile
@app.route('/', methods=['GET'])
def timeline():
    return render_template('timeline.html', user=current_user)


# profile
@app.route('/profile/<string:username>', methods=['GET'])
@login_required
def profile(username):
    # ログインユーザーのプロフィール
    profile = User.query.filter_by(username=username).first()
    profile = {
        'user_id':profile.id,
        'username':profile.username,
        'caption': profile.caption,
        'image':profile.image,
        'randaction_count':profile.randaction_count,
        'follow_count':profile.follow_count,
        'follow_count':profile.follower_count,
    }
    print(profile)

    # ログインユーザーの投稿
    posts = Post.query.filter_by(user_id=current_user.id).all()
    my_posts = [post.to_dict() for post in posts]

    # ログインユーザーが「いいね」した投稿
    my_favorite = db.session.query(Post).join(
        Favorite, Favorite.post_id == Post.id
    ).filter(
        Favorite.user_id == current_user.id
    ).all()
    my_favorite_posts = [my_favo.to_dict() for my_favo in my_favorite]


    return render_template(
        'profile.html',
        profile = profile,
        my_post = my_posts,
        my_favorite_posts = my_favorite_posts,
    )

# フォロー処理
@app.route('/follow', methods=['POST'])
@login_required
def follow():
    new_follow = Follow(
        follower_id = current_user.id,
        followed_id = request.args.get('followed_id'),
    )

    db.session.add(new_follow)
    db.session.commit()

    return redirect(url_for('profile'))


# edit_profile
class EditForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    content = StringField('profile', validators=[DataRequired()])

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    profile = {
        'user_id': current_user.id,
        'email': current_user.email,
        'content': current_user.content #未実装
    }

    # 更新
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        user = User.query.filter_by(id=profile.user_id).first()
        user.username = edit_form.username.data
        user.email = edit_form.email.data
        user.content = edit_form.content.data

        db.session.commit()

        return redirect(url_for('profile'))

    return render_template('edit_profile.html', profile=profile)



# logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('entry'))


if __name__ == '__main__':
    app.run(debug=True)

