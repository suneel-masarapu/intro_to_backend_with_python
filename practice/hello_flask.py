from flask import Flask

app = Flask(__name__)

@app.route('/')

def home() :
    a = 'hello bro'
    b = 9
    return f"<p>{a + b}</p>"

