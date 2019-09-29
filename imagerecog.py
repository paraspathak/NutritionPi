
def image_analysis(image_path):
    import requests
    import matplotlib.pyplot as plt
    from PIL import Image
    from io import BytesIO
    import os
    import sys
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()
    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    analyze_url = endpoint + "/analyze"
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    return analysis
    # image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    # # Display the image and overlay it with the caption.
    # image = Image.open(BytesIO(image_data))
    # plt.imshow(image)
    # plt.axis("off")
    # _ = plt.title(image_caption, size="x-large", y=-0.1)


def analyze_data(data):
    # Mega tags to store all sample food items in database
    database = ['banana', 'apple', 'donut', 'pasta', 'noodles', 'coffee', 'water']
    description = data['description']
    tags = description['tags']
    output = []
    for item in tags:
        for inventory in database:
            if item == inventory:
                output.append(item)

    return output[0]


def get_nutrition(name_of_item):
    import requests
    headers = {
        'x-app-id': "c42d660d",
        'x-app-key': "8f2662c884bd2f08efe82751e25eb80b",
        'x-remote-user-id': "8f2662c884bd2f08efe82751e25eb80b",
        'accept': 'application/json'
    }
    d = {
        "query": name_of_item
    }
    api_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    result = requests.post(api_url, headers=headers, data=d)
    result = result.text
    from flask import json
    result = json.loads(result)
    data_to_send = {}
    items_to_get = ['food_name',
                    'serving_weight_grams',
                    'nf_calories',
                    'nf_total_fat',
                    "nf_total_fat",
                    "nf_saturated_fat",
                    "nf_cholesterol",
                    "nf_sodium",
                    "nf_total_carbohydrate",
                    "nf_dietary_fiber",
                    "nf_sugars",
                    "nf_protein",
                    "nf_potassium"]
    nutrition = result['foods']
    first = nutrition[0]
    for item in items_to_get:
        try:
            data_to_send[item] = first[item]
        except:
            print("exception", item, ' Not found')
    return data_to_send


def click_picture(current_path):
    from datetime import datetime
    from os import system
    name = ('filename{}.jpg').format(datetime.now().strftime("%m%d%H%M%S"))
    command = 'fswebcam -r 1280x720 {} '.format(name)
    system(command)
    return current_path + name


if __name__ == "__main__":
    # # analyze_data(image_analysis("D:/trial.jpg"))
    # data = {"categories": [{"name": "food_", "score": 0.81640625}], "color": {"accentColor": "B34918", "dominantColorBackground": "Black", "dominantColorForeground": "Black", "dominantColors": ["Black"], "isBWImg": False, "isBwImg": False}, "description": {"captions": [{"confidence": 0.9134966061427492, "text": "a bowl of food"}], "tags": [
    #     "food", "bowl", "dish", "table", "filled", "pasta", "sitting", "pan", "plate", "full", "meat", "large", "broccoli", "fruit", "soup", "rice", "cooking", "sandwich", "stove"]}, "metadata": {"format": "Jpeg", "height": 250, "width": 200}, "requestId": "86e469f9-6e00-4292-bd3a-203336cee577"}
    # description = data['description']
    # tags = description['tags']
    # caption = description['caption']
    # print(tags)
    #print(get_nutrition(analyze_data(image_analysis("D:/th.jpg"))))
    print(get_nutrition("water"))
