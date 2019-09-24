import sys,pickle
from flask import Flask,flash, redirect, url_for, request, render_template, abort, jsonify,g
from socket import socket, AF_INET, SOCK_STREAM
from connection import setConnection
app = Flask(__name__)
@app.route('/start_trip/', methods=['POST'])
def start_trip():
    if request.method == 'POST':
        lis = [request.form["source"],request.form["destination"],request.form["cost"]]
        flash(setConnection(lis))
        return redirect(url_for('vehicle'))

@app.route('/insurance/', methods=['POST'])
def insurance():
    if request.method == 'POST':
        lis = [request.form["ins_no"],request.form["validf"],request.form["validu"],request.form["cost"]]
        flash(setConnection(lis))        
        return redirect(url_for('vehicle'))

@app.route('/permit/', methods=['POST'])
def permit():
    if request.method == 'POST': 
        lis = [request.form["pno"],request.form["validf"],request.form["validu"],request.form["icomp"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))


@app.route('/loan/', methods=['POST'])
def loan():
    if request.method == 'POST':
        lis = [request.form["lno"],request.form["lid"],request.form["costt"],request.form["costp"],request.form["lcomp"],request.form["dur"],request.form["int"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))

@app.route('/maintenance/', methods=['POST'])
def maintenance():
    if request.method == 'POST':    
        lis = [request.form["rmk"],request.form["plc"],request.form["cost"],request.form["vend"],request.form["dom"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))

        
@app.route('/tax/', methods=['POST'])
def tax():
    if request.method == 'POST':
        lis = [request.form["tno"],request.form["cost"],request.form["validf"],request.form["validu"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))


@app.route('/add_customer/', methods=['POST'])
def add_customer():
    if request.method == 'POST':
        lis = [request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('/'))
@app.route('/add_driver/', methods=['POST'])
def add_driver():
    if request.method == 'POST':
        # lis = [request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('/'))
@app.route('/add_vehicle/', methods=['POST'])
def add_vehicle():
    if request.method == 'POST':
        # lis = [request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('/'))
@app.route('/add_dependent/', methods=['POST'])
def add_dependent():
    if request.method == 'POST':
        # lis = [request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('driver'))
@app.route('/add_salary/', methods=['POST'])
def add_salary():
    if request.method == 'POST':
        # lis = [request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('driver'))
@app.route('/')
def index():
        vehicles=["a","b","c","d"]
        return render_template('Mainboot.html',vehicles=vehicles)

@app.route('/driver/')
def driver():
        driver=["a",112,32423]
        return render_template('Driver.html',driver=driver)

@app.route('/vehicle/')
def vehicle():
        vehicle=["diesel","tax","challan"]
        return render_template('Vehicle.html',vehicle=vehicle)


if __name__ == '__main__':
   app.run(debug = True)
