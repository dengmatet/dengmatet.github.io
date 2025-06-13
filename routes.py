from flask import render_template, request, redirect, url_for
from flask_session import Session
from flask_login import login_user, logout_user, current_user, login_required

from models import User

def register_routes(app, db, bcrypt):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
           return render_template('index.html')
        elif request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            numb = request.form.get('numb')
            subemail = request.form.get('subemail')
            message = request.form.get('message')

            user = User(name=name, email=email, numb=numb, subemail=subemail, message=message)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    
    @app.route('/login/<uid>')
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
        return 'Success'
    
    @app.route('/logout')
    def logout():
        login_user()
        return 'Success'