from flask import Blueprint, render_template, request, make_response

home_blueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@home_blueprint.route('/')
def home():
    """首頁"""
    response = make_response(render_template('index.html'))
    response.set_cookie('this_is_key', 'this is value', secure=True)
    return response


@home_blueprint.route('/tree/<int:page_number>')
def tree(page_number):
    """樹狀階層控制 Demo"""
    return render_template(f'tree/tree_{page_number}.html')


@home_blueprint.route('/choose_one_or_not/<int:page_number>')
def choose_one_or_not(page_number):
    return render_template(f'choose_one_or_not/choose_one_or_not_{page_number}.html')


@home_blueprint.route('/fetch')
def fetch():
    """Demo Fetch API"""
    return render_template('fetch/index.html')


@home_blueprint.route('/fetch/show')
def fetch_show():
    """Demo Fetch API"""
    return render_template('fetch/show.html')


@home_blueprint.route('/xss')
def xss():
    """Demo XSS"""
    return render_template('xss/index.html')


@home_blueprint.route('/xss/submit', methods=['GET'])
def xss_submit():
    view_model = {
        'username': request.args.get('username')
    }

    return render_template('xss/result.html', view_model=view_model)
