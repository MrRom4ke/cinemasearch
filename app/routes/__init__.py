def add_routes(app):
    from ..controllers import main_page, reg_and_auth

    app.add_url_rule('/', view_func=main_page.index_view)
    app.add_url_rule('/register', view_func=reg_and_auth.register_view, methods=['POST', 'GET'])