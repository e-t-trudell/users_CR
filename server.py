# STEP THREE
from flask import Flask, render_template, redirect, request, session
# import the class from model_one.py
from flask_app.models.user import User

app = Flask(__name__)
app.secret_key='0bns834w5jkbnsdv9f8yw4'

@app.route("/")
def index():
    # from flask_app.models.model_one import User
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("create.html", users=users)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["email"]}
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Redirect after saving to the database.
    return redirect('/display')
@app.route("/display")
def display():
    users = User.get_all()
    print("Displaying USERS!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(users)
    return render_template("read_all.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)