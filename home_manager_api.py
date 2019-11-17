from flask import Flask, request
from home_manager import HomeManager
from condo import Condo
from detached_home import DetachedHome

import json

app = Flask(__name__)

filepath = "FILE PATH HERE" #TODO
manager = HomeManager(filepath)

# This is where the API methods will go
#TODO
