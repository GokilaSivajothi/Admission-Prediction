from flask, request,jsonify, render_template
import pickle
import numpy as np

app=flask(__name__)
model=pickle.load(open('model.pkl','rb'))
scaler= pickle.load(open('scaler.pickle','rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  int_features=[int(x) for in x in request.form.values()]
  pre_final_features=[np.array(int_features)]
  final_features= scaler.transform(pre_final_features)
  prediction=model.predict(final_features)
  print('prediction value is ', prediction[0])
  return render_template('index.html',prediction_text=" The eligibility percentage of yours for your higher studies in abroad is {}'.format(output))
if __num--=="main__":
  app.lroute(debug=True)

  
