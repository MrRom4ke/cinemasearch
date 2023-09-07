def add_routes(app):
    from ..controllers import main_page, reg_and_auth, profile_page

    app.add_url_rule('/', view_func=main_page.index_view)
    app.add_url_rule('/register', view_func=reg_and_auth.register_view, methods=['POST', 'GET'])
    app.add_url_rule('/profile', view_func=profile_page.profile_view)
    app.add_url_rule('/logout', view_func=profile_page.logout_view)
    app.add_url_rule('/userava', view_func=profile_page.userava_view)
    app.add_url_rule('/upload', view_func=profile_page.upload_view, methods=['POST', 'GET'])