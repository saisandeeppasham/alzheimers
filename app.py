from flask import Flask, request, jsonify, render_template
import pickle
import numpy as numpy
app = Flask(__name__,template_folder='templates')
model_gb = pickle.load(open('algo_gb.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    Name=str(request.form.get('Name'))
    Email=str(request.form.get('Email'))
    Phone=str(request.form.get('Phone'))
    gender=str(request.form.get('M/F')).lower()
    
    age=float(request.form.get('Age'))
    educ=float(request.form.get('Educ'))
    ses=float(request.form.get('SES'))
    mmse=float(request.form.get('MMSE'))
    etiv=float(request.form.get('eTIV'))
    nwbv=float(request.form.get('nWBV'))
    asf=float(request.form.get('ASF'))
    m_f=-1
    if gender=='m' or gender=='male':
        m_f=1
    else:
        m_f=0
    dic=[]
    dic.append([Name,Email,Phone,gender,age,educ,ses,mmse,etiv,nwbv,asf])
    
    inputs=[[m_f,age,educ,ses,mmse,etiv,nwbv,asf]]
    
    output_gb=model_gb.predict(inputs)[0]
    
    if output_gb==1:
        result='Demented'
    else:
        result='Non-Demented'

    return render_template('index.html', prediction_text='Your Result: '+result)
if __name__ == '__main__':
    app.run(port = 5000, debug=False)
