from flask import Flask, flash, render_template, request, json, url_for 
import os


app = Flask(__name__)

@app.route("/key")
def key():
    return("""
        https://westcentralus.api.cognitive.microsoft.com/vision/v1.0

https://westcentralus.api.cognitive.microsoft.com/vision/v2.0

https://westcentralus.api.cognitive.microsoft.com/vision/v2.1

Key 1: 5b62dab744a74aa8aeba4c4606fd46a2

Key 2: a1566e95fc7340618cf15b1313531a95
    """)


@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/second.html")
def hpage():
    return render_template('second.html')

@app.route('/takephoto', methods = ['POST'])
def take_photo():
    print(url_for('static',filename='img/p.jpg'))
    return json.dumps({'food_name': 'noodle', 'serving_weight_grams': 124, 'nf_calories': 195.92, 'nf_total_fat': 1.15, 'nf_saturated_fat': 0.22, 'nf_cholesterol': 0, 'nf_sodium': 1.24, 'nf_total_carbohydrate': 38.27, 'nf_dietary_fiber': 2.23, 'nf_sugars': 0.69, 'nf_protein': 7.19, 'nf_potassium': 54.56, 'image':'p.jpg'})
    import imagerecog
    image_name = imagerecog.click_picture("./")
    result = imagerecog.get_nutrition(imagerecog.image_analysis(imagerecog.analyze_data(image_name )))
    result['image'] = image_name
    return json.dumps(result)


if __name__ == "__main__":   
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(port= 8080)
