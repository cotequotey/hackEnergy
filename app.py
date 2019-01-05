# -*- coding: utf-8 -*-
from flask import (Flask, url_for, render_template, request, redirect, flash)
import math

app = Flask(__name__)
app.secret_key = 'stringy string'
    
@app.route('/', methods=['GET','POST'])
def compute_cost():
    # the request object is a new import from flask
    if request.method == 'GET':
        return render_template('form.html')
    else:
        num = request.form.get('distance')
        num2 = request.form.get('price/gallon')
        num3 = request.form.get('miles/gallon')
   
    gasCost = float(num) * float(num2) * float(num3)
    electricCost = float(num) * 0.0348 
    try:
        # return render_template('msg.html',
        # msg='Gas Vehicle Data:\n\nDistance(mi): {num}'.format(num=num) +
        #     '\n\nThis trip costs ${cost} with a gas vehicle'.format(cost=cost))
        return render_template('msg.html', num=num,num2=num2, num3=num3,gasCost=gasCost, electricCost=electricCost)
    except:
        #return render_template('msg.html',msg='Error computing cost of this car with price ${num}'.format(num=num))
        return render_template('msg.html', num=num,num2=num2, num3=num3,gasCost=gasCost, electricCost=electricCost)
        
if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8082)