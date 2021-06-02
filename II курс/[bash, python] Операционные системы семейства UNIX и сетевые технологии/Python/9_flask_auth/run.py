from my_app import app, create_tables, register_blueprints

if __name__ == '__main__':
    create_tables()
    register_blueprints()
    app.run()
