from flask import Flask, flash, render_template, request, json 
import os


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route('/takephoto', methods = ['POST'])
def take_photo():
    import imagerecog
    result = imagerecog.get_nutrition(imagerecog.image_analysis(imagerecog.analyze_data(imagerecog.click_picture("") )))
    return json.dumps(result)


if __name__ == "__main__":   
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(port= 8080)
