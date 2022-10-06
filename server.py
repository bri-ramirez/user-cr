from crypt import methods
from flask import Flask, render_template, request, redirect
from friend import Friend
from user import User

app = Flask(__name__)

@app.route("/users")
def listUsers():
    users = User.get_all()
    return render_template("users/list.html", users=users)

@app.route("/users/new")
def createUser():
    return render_template("users/create.html")

@app.route("/users", methods = ["POST"])
def processUser():

    data = {
        "fname": request.form["first_name"],
        "lname": request.form["last_name"],
        "email": request.form["email"]
    }

    userId = User.save(data)

    print("UserID:", userId)
    return redirect('/users')






@app.route('/create_friend', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Friend.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)