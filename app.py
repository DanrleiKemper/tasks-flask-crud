from flask import Flask

#cria aplicação Flask
app = Flask(__name__)

#criar rota para comunicar com outros clientes = receber e devolver
@app.route("/") #define a rota - @app.route("/") = rota padrão
def hello_word():
    return "Hello Word!"

#criar outra rota retornando outras informações
@app.route("/about")
def about():
    return "Página sobre"

#modo de execução de desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)
