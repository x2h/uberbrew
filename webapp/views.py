# -*- coding: utf-8 -*-

from flask import render_template, jsonify
from webapp import app
import time
import math

@app.route('/')
def index():
    return render_template('index.html')

time_ = time.time()

@app.route('/api/getTemp', methods=['GET'])
def get_temp():
    return jsonify({'value' : math.sin((time.time() - time_)/10.0)})