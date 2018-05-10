'''
auth_views.py

    all of the routes related to user authorization and credentials

'''

from flask import url_for
from flask_login import logout_user, login_required, login_user
from werkzeug.utils import redirect
from flask_dance.contrib.google import google
from flask_dance.consumer import oauth_authorized

from project import app
from project import google_blueprint

from project.auth.firebase_user import get_firebase_user, create_firebase_user

from project.views.view_utils import logout_required


@app.route('/log_out')
@login_required
def log_out() -> str:
    logout_user()
    return redirect(url_for('index'))


@oauth_authorized.connect_via(google_blueprint)
@logout_required
def log_in():
    # get oauth response
    resp = google.get("/oauth2/v2/userinfo")
    email = resp.json()['email']

    if resp.ok:
        # see if the user already exists
        user = get_firebase_user(email)

        # if they don't exist create a new user
        if not user:
            display_name = resp.json()['name']
            create_firebase_user(display_name, email)

        # login the user
        login_user(user)
