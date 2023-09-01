def add_routes(app):
    from ..controllers import main_page, reg_and_auth, profile

    app.add_url_rule('/', view_func=main_page.index_view)
    app.add_url_rule('/register', view_func=reg_and_auth.register_view, methods=['POST', 'GET'])
    app.add_url_rule('/profile',view_func=profile.profile_view)
    app.add_url_rule('/logout', view_func=profile.logout_view)