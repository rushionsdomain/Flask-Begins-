from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Configurations for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize migration tool
migrate = Migrate(app, db)

# Import models (which we will create later)
import models

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # Render homepage template

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
