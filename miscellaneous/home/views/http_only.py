from flask import Blueprint, render_template, make_response

http_only_blueprint = Blueprint(
    'http_only',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@http_only_blueprint.route('/http_only')
def http_only():
    response = make_response(render_template('http_only/index.html'))
    response.set_cookie('name', 'Steven')
    response.set_cookie('age', '34', httponly=True)
    response.set_cookie('job', 'QC')
    return response
