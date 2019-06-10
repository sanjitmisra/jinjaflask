from flask import Flask

#__name__ is a predefined variable set to the name of the module in which it is used
app = Flask(__name__)

from app import routes