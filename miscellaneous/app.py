import os
from datetime import timedelta

from flask import Flask
from flask import render_template

from miscellaneous.lib import logger

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def home():
    """首頁"""
    logger.info('index.html')
    return render_template('index.html')


@app.route('/tree/<int:page_number>')
def tree(page_number):
    """樹狀階層控制 Demo"""
    logger.info(f'other_{page_number}.html')
    return render_template(f'tree/tree_{page_number}.html')


@app.route('/other/<int:page_number>')
def other(page_number):
    """其他"""
    logger.info(f'other_{page_number}.html')
    return render_template(f'other/other_{page_number}.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=7000
    )
