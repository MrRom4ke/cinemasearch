def add_routes(app):
    from ..controllers import index

    app.add_url_rule('/', view_func=index.index)
    app.add_url_rule('/register', view_func=index.register)
