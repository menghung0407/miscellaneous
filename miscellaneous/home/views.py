from flask import Blueprint, render_template

from miscellaneous.lib import logger

home_blueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/home'
)


@home_blueprint.route('/')
def home():
    """首頁"""
    logger.info('index.html')
    return render_template('index.html')


@home_blueprint.route('/tree/<int:page_number>')
def tree(page_number):
    """樹狀階層控制 Demo"""
    logger.info(f'other_{page_number}.html')
    return render_template(f'tree/tree_{page_number}.html')
