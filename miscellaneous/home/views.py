from flask import Blueprint, render_template

home_blueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@home_blueprint.route('/')
def home():
    """首頁"""
    return render_template('index.html')


@home_blueprint.route('/tree/<int:page_number>')
def tree(page_number):
    """樹狀階層控制 Demo"""
    return render_template(f'tree/tree_{page_number}.html')


@home_blueprint.route('/choose_one_or_not/<int:page_number>')
def choose_one_or_not(page_number):
    """樹狀階層控制 Demo"""
    return render_template(f'choose_one_or_not/choose_one_or_not_{page_number}.html')
