from flask import Flask, render_template, request
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app=Flask(__name__)
category={
    0: 'Bean', 1: 'Bitter_Gourd', 2: 'Bottle_Gourd', 3 : 'Brinjal', 4: "Broccoli", 5: 'Cabbage', 6: 'Capsicum', 7: 'Carrot', 8: 'Cauliflower',
    9: 'Cucumber', 10: 'Papaya', 11: 'Potato', 12: 'Pumpkin', 13 : "Radish", 14: "Tomato"
}

def predict_image(filename,model):
    img_ = image.load_img(filename, target_size=(224, 224))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0) 
    img_processed /= 255.   
    
    prediction = model.predict(img_processed)
    index = np.argmax(prediction)
    return ("{}".format(category[index]))


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    path_to_model='./model_inceptionV3.h5'
    tl_model = load_model(path_to_model)
    cnn_model = load_model('./model_cnn.h5')
    img_prediction_tl = predict_image((image_path),tl_model)
    img_prediction_cnn = predict_image((image_path),cnn_model)

    return render_template('home.html', prediction_tl = img_prediction_tl,prediction_cnn=img_prediction_cnn)
if __name__ == '__main__':
    app.run(debug=True)
