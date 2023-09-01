from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)

model_selected_path='model/gb.pkl'

model = pickle.load(open(model_selected_path,'rb'))


@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/thank_you') 
def thank_you():
    fullname = request.args.get('fullname')
    email = request.args.get('email')
    return render_template('thank_you.html',fullname=fullname,email=email)

@app.route('/about') 
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST',"GET"])
def predict():
    if request.method == 'POST':
        Bike_company=request.form.get("Bike_company")
        Bike_Model = request.form.get("Bike_Model")
        Remaining_warranty=request.form.get("Remaining_warranty")
        Engine_Type=request.form.get("Engine_Type")
        Fuel_Type=request.form.get("Fuel_Type")
        CC=request.form.get("CC")
        Fuel_Capacity=request.form.get("Fuel_Capacity")
        print('Bike Company',Bike_company)
        print("Bike_Model",Bike_Model)
        print("Remaining_warranty",Remaining_warranty)
        print("Engine_Type",Engine_Type)
        print("Fuel_Type",Fuel_Type)
        print("CC",CC)
        print("Fuel_Capacity",Fuel_Capacity)
        
        data=np.array([[CC,Fuel_Capacity,Remaining_warranty,Engine_Type,Fuel_Type]])
        print(data)
        print(data.dtype)
        prediction=model.predict(data)

        output=prediction[0]

        if output<0:
            return render_template('predict.html',result=" Sorry you cannot sell this bike. ")

        else:
            return render_template('predict.html',prediction=output)

    else:
        return render_template('solution.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)
