from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.rout('/')
def home():
    return "hello world"

if __name__ == '__main__':
    app.run()
