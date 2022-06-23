import requests
to_predict_dict = {'sepal_length':5.1,
                   'sepal_width': 3.8,
                   'petal_length':1.9,
                   'petal_width':0.4}

url = 'http://127.0.0.1:8000/predict'
r = requests.post(url, json=to_predict_dict)
r.json()

