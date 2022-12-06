from flask import Blueprint, render_template, request, json, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('index.html')

@routes.route('/prediction')
def prediction():
    return render_template("prediction.html")