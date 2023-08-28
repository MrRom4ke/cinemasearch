from app import create_app

app = create_app()

if __name__ == "__main__":
    """
    Запускает Flask-приложение.
    """
    app.run()
