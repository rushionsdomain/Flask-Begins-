from flask import Flask

#create flask instance 
app = Flask(__name__)

@app.get('/') 
def index():
    return {"message": "welcome to Eat-out Restaurant app"}