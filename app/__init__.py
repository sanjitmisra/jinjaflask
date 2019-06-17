from flask import Flask
from config import Config

#__name__ is a predefined variable set to the name of the module in which it is used
app = Flask(__name__)
app.config.from_object(Config)

from app import routes