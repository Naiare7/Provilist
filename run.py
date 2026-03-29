from app import create_app, db
# from app.seeds import run_seeds

app = create_app()
#Correr los seeds al iniciar la app
# @app.cli.command("seed")
# def seed():
#     """Ejecuta los seeds"""
#     run_seeds()
#     print("Seeds ejecutados correctamente")

if __name__ == "__main__":
    app.run(debug=True)