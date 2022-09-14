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


@app.route('/refactor')
def refactor():
    """重構"""
    logger.info('refactor.html')
    return render_template('refactor.html')


@app.route('/rwd')
def rwd():
    """RWD"""
    logger.info('rwd.html')
    return render_template('rwd.html')


@app.route('/ui_ux_concept')
def ui_ux_concept():
    """UI/UX concept"""
    logger.info('ui_ux_concept.html')
    return render_template('ui_ux_concept.html')


@app.route('/meet/<int:page_number>')
def meet(page_number):
    """會議"""
    logger.info(f'meet_{page_number}.html')
    return render_template(f'meet/meet_{page_number}.html')


@app.route('/tree/<int:page_number>')
def tree(page_number):
    """樹狀階層控制 Demo"""
    logger.info(f'other_{page_number}.html')
    return render_template(f'tree/tree_{page_number}.html')


@app.route('/other/<int:page_number>')
def other(page_number):
    """會議"""
    logger.info(f'other_{page_number}.html')
    return render_template(f'other/other_{page_number}.html')


@app.route('/statechart/<int:page_number>')
def statechart(page_number):
    """會議"""
    logger.info(f'statechart_{page_number}.html')

    previous_page = page_number - 1
    next_page = page_number + 1

    if next_page > 6:
        next_page = 0

    view_model = {
        'previous_page': previous_page,
        'next_page': next_page
    }

    return render_template(f'statechart/statechart_{page_number}.html',
                           view_model=view_model)


@app.route('/activity_diagram/<int:page_number>')
def activity_diagram(page_number):
    logger.info(f'活動圖 {page_number}')

    item_name = 'activity_diagram'
    limit_page = 1

    previous_page = page_number - 1
    if previous_page < 0:
        previous_page = 0

    next_page = page_number + 1
    if next_page > (limit_page - 1):
        next_page = 0

    view_model = {
        'previous_page_route': f'/{item_name}/{previous_page}',
        'next_page_route': f'/{item_name}/{next_page}'
    }

    return render_template(f'{item_name}/{page_number}.html', view_model=view_model)


@app.route('/test_engineer/<int:page_number>')
def test_engineer(page_number):
    logger.info(f'測試工程師 {page_number}')
    previous_page = page_number - 1
    next_page = page_number + 1

    if previous_page < 0:
        previous_page = 0

    if next_page > 0:
        next_page = 0

    view_model = {
        'previous_page_route': f'/test_engineer/{previous_page}',
        'next_page_route': f'/test_engineer/{next_page}'
    }

    return render_template(f'test_engineer/{page_number}.html', view_model=view_model)


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=7000
    )
