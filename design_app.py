from enum import unique
from flask import Flask, request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql.selectable import Select

sample = Flask(__name__)
sample.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Accounts.sqlite'
sample.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(sample)
ma = Marshmallow(sample)

class Accounts(db.Model):
    __tablename__ = "accounts"
    account_id = db.Column(db.String(50), primary_key=True)
    account_username = db.Column(db.String(50), unique=True)
    account_password = db.Column(db.String(50))
    account_firstName = db.Column(db.String(255))
    account_midName = db.Column(db.String(255))
    account_lastName = db.Column(db.String(255))
    account_email = db.Column(db.String(255))

    def __init__(self, account_id, 
                       account_username,
                       account_password,
                       account_firstName,
                       account_midName,
                       account_lastName,
                       account_email):

        self.account_id = account_id
        self.account_username = account_username
        self.account_password = account_password
        self.account_firstName = account_firstName
        self.account_midName = account_midName
        self.account_lastName = account_lastName
        self.account_email = account_email

db.create_all()

class AccountSchema(ma.Schema):
    class Meta:
        fields = ("account_id",
                  "account_username",
                  "account_password",
                  "account_firstName",
                  "account_midName",
                  "account_lastName",
                  "account_email")

account_Schema = AccountSchema()
accounts_Schema = AccountSchema(many=True)

@sample.route("/")
def main():
    return render_template("login.html")

@sample.route("/register")
def register():
    return render_template("register.html")

@sample.route("/create_account", methods=['POST'])
def create_account():
    row = db.session.query(Accounts).count() + 1
    print(row)
    if request.method == "POST":
        account_username = request.form['username']
        account_password = request.form['password']
        account_firstName = request.form['first_name']
        account_midName = request.form['middle_name']
        account_lastName = request.form['last_name']
        account_email = request.form['email']
    new_account = Accounts(row,
                           account_username, 
                           account_password, 
                           account_firstName,
                           account_midName,
                           account_lastName,
                           account_email)
    db.session.add(new_account)
    db.session.commit()
    return redirect('/', code=302)

@sample.route("/login", methods=['POST'])
def login():
    password_db = Accounts.query.filter(Accounts.account_username==request.form['username']).first()
    if password_db == None:
        return redirect("/", code=302)
    elif password_db.account_password == request.form['password']:
        return redirect(f"/home/{password_db.account_username}", code=302)
    else:
        return redirect("/", code=302)

@sample.route("/home/<account_username>")
def home(account_username):
    return render_template("index.html", user=account_username)

@sample.route("/dashboard/<account_username>")
def dashboard(account_username):
    return render_template("dashboard.html", user=account_username)

@sample.route("/about_us/<account_username>")
def about_us(account_username):
    return render_template("about.html", user=account_username)

@sample.route("/contact/<account_username>")
def contact(account_username):
    return render_template("contact.html", user=account_username)

@sample.route("/accounts/<account_username>")
def accounts(account_username):
    current_account = Accounts.query.filter(Accounts.account_username == account_username).first()
    return render_template("account.html", user=account_username
                                         , first_name = current_account.account_firstName
                                         , middle_name = current_account.account_midName
                                         , last_name = current_account.account_lastName
                                         , email = current_account.account_email)

@sample.route("/update_info/<account_username>")
def up_info(account_username):
    current_account = Accounts.query.filter(Accounts.account_username == account_username).first()
    return render_template("update_form.html", user=account_username
                                         , first_name = current_account.account_firstName
                                         , middle_name = current_account.account_midName
                                         , last_name = current_account.account_lastName
                                         , email = current_account.account_email)

@sample.route('/update', methods=['POST', 'PUT'])
def update():
    account_info = Accounts.query.filter(Accounts.account_username==request.form['original']).first()
    print(account_info)
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        mid_name = request.form['middle_name']
        last_name = request.form['last_name']
        email = request.form['email']

    account_info.account_username = user
    account_info.account_password = password
    account_info.account_firstName = first_name
    account_info.account_midName = mid_name
    account_info.account_lastName = last_name
    account_info.account_email = email

    db.session.commit()
    
    return redirect(f"/accounts/{user}", code=302)

@sample.route("/del_prompt/<account_username>")
def del_prompt(account_username):
    return render_template("del_prompt.html",
                            user = account_username)

@sample.route("/account_deleted", methods=['DELETE', 'POST'])
def account_deleted():
    if request.method == "POST":
        account_username = request.form['username']
    password_db = Accounts.query.filter(Accounts.account_username==account_username).first()
    db.session.delete(password_db)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port = 7070)
