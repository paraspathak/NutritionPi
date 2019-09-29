from flask import Flask, flash, render_template, request, json 
import os


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/second.html")
def hpage():
    return render_template('second.html')

@app.route('/takephoto', methods = ['POST'])
def take_photo():
    return json.dumps({'food_name': 'noodle', 'serving_weight_grams': 124, 'nf_calories': 195.92, 'nf_total_fat': 1.15, 'nf_saturated_fat': 0.22, 'nf_cholesterol': 0, 'nf_sodium': 1.24, 'nf_total_carbohydrate': 38.27, 'nf_dietary_fiber': 2.23, 'nf_sugars': 0.69, 'nf_protein': 7.19, 'nf_potassium': 54.56})
    import imagerecog
    result = imagerecog.get_nutrition(imagerecog.image_analysis(imagerecog.analyze_data(imagerecog.click_picture("./") )))
    return json.dumps(result)


if __name__ == "__main__":   
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(port= 8080)
