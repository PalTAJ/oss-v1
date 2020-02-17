from flask import jsonify, request
from flask_jwt import jwt_required, current_identity
from sqlalchemy import and_
from sqlalchemy.types import Float
from flask import Flask, render_template

import time
from ..app import app

from ..models import db




@app.route('/main', methods=['POST','GET'])
def mainPage():
    return render_template('main.html')



@app.route('/add-customers', methods=['POST','GET'])
def add_customer():
    return render_template('add_customers.html')
    
    
@app.route('/add-products', methods=['POST','GET'])
def add_product():
    return render_template('add_products.html')
    
@app.route('/add-trans', methods=['POST','GET'])
def add_tran():
    return render_template('add_trans.html')

@app.route('/search-customers', methods=['POST','GET'])
def search_customer():
    return render_template('search_customers.html')
    
    
@app.route('/search-products', methods=['POST','GET'])
def search_product():
    return render_template('search_products.html')

@app.route('/search-trans', methods=['POST','GET'])
def search_tran():
    return render_template('search_trans.html')
    
    