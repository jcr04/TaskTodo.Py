from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se elas ainda não existem
    app.run(debug=True)