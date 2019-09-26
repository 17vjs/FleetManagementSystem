import sys,pickle
from flask import Flask,flash, redirect, url_for, request, render_template, abort, jsonify,g
from socket import socket, AF_INET, SOCK_STREAM
from connection import setConnection
app = Flask(__name__)
app.secret_key = 'my unobvious secret key'

@app.route('/start_trip/', methods=['POST'])
def start_trip():
    if request.method == 'POST':
        lis = [request.form["source"],request.form["destination"],request.form["cost"]]
        flash(setConnection(lis))
        return redirect(url_for('vehicle'))
@app.route('/deleteVehicle/', methods=['POST'])
def deleteVehicle():
    if request.method == 'POST':
        flash(setConnection(["delete_vehicles","mh14hs6097"]))        
        return redirect(url_for('index'))
@app.route('/deleteDriver/', methods=['POST'])
def deleteDriver():
    if request.method == 'POST':
        flash(setConnection(["delete_drivers","2"]))        
        return redirect(url_for('index'))

@app.route('/insurance/', methods=['POST'])
def insurance():
    if request.method == 'POST':
        lis = ["write_insurances","mh14hs6097",request.form["ins_no"],request.form["validf"],request.form["validu"],request.form["cost"],request.form["icomp"]]
        flash(setConnection(lis))        
        return redirect(url_for('vehicle'))

@app.route('/permit/', methods=['POST'])
def permit():
    if request.method == 'POST': 
        lis = ["write_permits","mh14hs6097",request.form["pno"],request.form["validf"],request.form["validu"],request.form["cost"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))


@app.route('/loan/', methods=['POST'])
def loan():
    if request.method == 'POST':
        lis = ["write_loans","mh14hs6097",request.form["lno"],request.form["costt"],"0",request.form["lcomp"],request.form["dur"],request.form["intr"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))

@app.route('/maintenance/', methods=['POST'])
def maintenance():
    if request.method == 'POST':    
        lis = ["write_maintenance","mh14hs6097",request.form["rmk"],request.form["plc"],request.form["cost"],request.form["vend"],request.form["dom"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))

        
@app.route('/tax/', methods=['POST'])
def tax():
    if request.method == 'POST':
        lis = ["write_taxes","mh14hs6097",request.form["tno"],request.form["validf"],request.form["validu"],request.form["cost"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle'))


@app.route('/add_customer/', methods=['POST'])
def add_customer():
    if request.method == 'POST':
        lis = ["write_customers",request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('index'))
@app.route('/add_driver/', methods=['POST'])
def add_driver():
    if request.method == 'POST':
        lis = ["write_drivers",request.form["driver_name"],request.form["License_no"],request.form["contact_no"]]
        flash(setConnection(lis))                 
        return redirect(url_for('index'))
@app.route('/add_vehicle/', methods=['POST'])
def add_vehicle():
    if request.method == 'POST':
        lis = ["write_vehicles",request.form["veh_no"],request.form["chassis_no"],request.form["vehicle_class"],request.form["vehicle_capacity"]]
        flash(setConnection(lis))
        return redirect(url_for('index'))
@app.route('/add_dependent/', methods=['POST'])
def add_dependent():
    if request.method == 'POST':
        lis = ["write_dependents","4",request.form["nm"],request.form["rel"],request.form["cnt"]]
        flash(setConnection(lis))                 
        return redirect(url_for('driver'))
@app.route('/add_salary/', methods=['POST'])
def add_salary():
    if request.method == 'POST':
        lis = ["write_salary","2",request.form["salary"],"2019-09-02"]
        flash(setConnection(lis))                 
        return redirect(url_for('driver'))
@app.route('/')
def index():
        vehicles=setConnection(["read_vehicles"])
        drivers=setConnection(["read_drivers"])
        customers=setConnection(["read_customers"])

        return render_template('Mainboot.html',vehicles=vehicles,drivers=drivers,customers=customers)

@app.route('/driver/')
def driver():
        driver=["a",112,32423]
        return render_template('Driver.html',driver=driver)

@app.route('/vehicle/<veh_no>')
def vehicle(veh_no):
        vehicle=setConnection(["read_vehicle",veh_no])
        # vehicle=["A"]
        return render_template('Vehicle.html',vehicle=vehicle)


if __name__ == '__main__':
   app.run(debug = True)
