from flask import Flask, request, jsonify, render_template
import pickle
import numpy as numpy
app = Flask(__name__,template_folder='templates')
model_gb = pickle.load(open('model_gb.pkl', 'rb'))
model_ada = pickle.load(open('model_ada.pkl', 'rb'))
model_et = pickle.load(open('model_et.pkl', 'rb'))
model_rf = pickle.load(open('model_rf.pkl', 'rb'))
model_svc = pickle.load(open('model_svc.pkl', 'rb'))
#model_xgb = pickle.load(open('model_xgb.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    Name=str(request.form.get('Name'))
    Email=str(request.form.get('Email'))
    Phone=str(request.form.get('Phone'))
    gender=str(request.form.get('M/F')).lower()
    
    i2=float(request.form.get('Age'))
    i3=float(request.form.get('Educ'))
    i4=float(request.form.get('SES'))
    i5=float(request.form.get('MMSE'))
    i6=float(request.form.get('eTIV'))
    i7=float(request.form.get('nWBV'))
    i8=float(request.form.get('ASF'))
    i1=-1
    if gender=='m' or gender=='male':
        i1=1
    else:
        i1=0
    dic=[]
    dic.append([Name,Email,Phone,gender,i2,i3,i4,i5,i6,i7,i8])
    
    inputs=[[i1,i2,i3,i4,i5,i6,i7,i8]]
    
    x1=model_gb.predict(inputs)[0]
    #x2=model_ada.predict(inputs)[0]
    x3=model_et.predict(inputs)[0]
    x4=model_rf.predict(inputs)[0]
    #x5=model_svc.predict(inputs)[0]
    #x6=model_xgb.predict(inputs)[0]
    c=[x1,x3,x4]
    
    
    #inputs = [np.array(inputs)]
    #result=str(model.predict(inputs))
    #print(model.predict(inputs))
    if  c.count(1)>c.count(0):
        result='Demented'
    else:
        result='Non-Demented'

    return render_template('index.html', prediction_text='Your Result: '+result)
if __name__ == '__main__':
    app.run(port = 5000, debug=False)
