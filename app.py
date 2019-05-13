import os
from flask import Flask, render_template, session, redirect, request, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','XYZ')


def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))


@app.route("/")

def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
