from flask import Blueprint

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    return "contacs list"

@contacts.route('/new')
def add_contact():
    return "saving a contact"