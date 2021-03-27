import flask

app = flask.Flask(__name__)

#ruta pagina inicio
@app.route('/')
def home():
    return flask.render_template('home.html')

#ruta pagina nosotros
@app.route('/about')
def about():
    return flask.render_template('about.html')

#ruta pagina material
@app.route('/estudios')
def material():
    return flask.render_template('estudios.html')

#ruta pagina contactenos
@app.route('/contactenos')
def contactenos():
    return flask.render_template('contactenos.html')

#ruta formulario
@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = flask.request.form.get("nombre")
    apellido = flask.request.form.get("apellido")
    edad = flask.request.form.get("edad")
    email = flask.request.form.get("email")
    return flask.render_template("comprobar.html", 
    nombre=nombre, apellido=apellido, edad=edad, email=email)
    if __name__=='__main__':
        app.run(debug=True)

