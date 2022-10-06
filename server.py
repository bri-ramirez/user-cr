from crypt import methods
from flask import Flask, render_template, request, redirect
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


if __name__=="__main__":
    app.run(debug=True)