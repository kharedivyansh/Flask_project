from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure secret key
oauth = OAuth(app)

# Configure OAuth for Google
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    authorize_params=None,
    authorize_params=None,
    authorize_params=None,
    token_url='https://accounts.google.com/o/oauth2/token',
    redirect_uri=os.getenv('GOOGLE_REDIRECT_URI'),
    client_kwargs={'scope': 'openid profile email'},
)

# Configure OAuth for Facebook
facebook = oauth.register(
    name='facebook',
    client_id=os.getenv('FACEBOOK_CLIENT_ID'),
    client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    authorize_params=None,
    authorize_params=None,
    authorize_params=None,
    token_url='https://graph.facebook.com/v3.3/oauth/access_token',
    redirect_uri=os.getenv('FACEBOOK_REDIRECT_URI'),
    client_kwargs={'scope': 'email'},
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/google')
def login_google():
    return google.authorize_redirect(redirect_uri=url_for('authorize_google', _external=True))

@app.route('/authorize/google')
def authorize_google():
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    # You can now use the user information, e.g., user['name'], user['email'], etc.
    # Store the user information in the session or your database as needed.
    session['user'] = user
    return redirect(url_for('profile'))

@app.route('/login/facebook')
def login_facebook():
    return facebook.authorize_redirect(redirect_uri=url_for('authorize_facebook', _external=True))

@app.route('/authorize/facebook')
def authorize_facebook():
    token = facebook.authorize_access_token()
    user = facebook.parse_id_token(token)
    # You can now use the user information, e.g., user['name'], user['email'], etc.
    # Store the user information in the session or your database as needed.
    session['user'] = user
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user = session.get('user')
    if user:
        return render_template('profile.html', user=user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
