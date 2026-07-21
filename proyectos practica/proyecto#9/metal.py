#Importar modulo Flask
#Desde "Un lugar" importa "esto"
from flask import Flask

#Flask en una clase que nos permite crear vel server web
#En algunos cintxtos, llaman al server "app"
#app contiene toda la informacion del server
app = Flask(__name__)
#ruta de inicio
@app.route('/')
#TODAS LAS RUTAS TIENEN QUE RETORNAR ALGO
def inicio ():
    return "Mi primer server web :)"
if __name__ == "__main__":
    app.run(debug = True)