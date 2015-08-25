# __author__ = 'Jason'
from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(404)
    # this_is_never_executed()


@app.errorhandler(404)
def not_found_page(error):
    return render_template('not_found_page.html'), 404



if __name__ == '__main__':
    app.run()