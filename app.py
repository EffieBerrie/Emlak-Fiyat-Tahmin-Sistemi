from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Eğittiğimiz modeli yüklüyoruz
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Arayüzden gelen metrekare bilgisini al
    input_value = float(request.form['area'])
    
    # Modelin beklediği formata getir (2D array)
    prediction = model.predict([[input_value]])
    
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Tahmin Edilen Fiyat: {output} Rs.')

if __name__ == "__main__":
    app.run(debug=True)