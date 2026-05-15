from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login first!'

from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id, mysql)

from routes import register_routes
register_routes(app, mysql)

from services.ai_scoring import (
    score_communication_text, score_confidence_scale,
    score_teamwork_text, score_leadership_text, score_ei_text,
    score_mcq_answer, safe_avg
)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 AI Personality Assessment System Started!")
    print("="*60)
    print("📍 Open browser: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=app.config['DEBUG'], port=5000)
