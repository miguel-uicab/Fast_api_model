import requests
to_predict_dict = {'sepal_length':5.1,
                   'sepal_width': 3.8,
                   'petal_length':1.9,
                   'petal_width':0.4}

url = 'http://127.0.0.1:8000/predict'
r = requests.post(url, json=to_predict_dict)
r.json()


curl -H "Content-Type: application/json" -d '{
  "concavity_mean": 0.3001,
  "concave_points_mean": 0.1471,
  "perimeter_se": 8.589,
  "area_se": 153.4,
  "texture_worst": 17.33,
  "area_worst": 2019.0
}' -XPOST http://0.0.0.0:8000/predict



curl -H "Content-Type: application/json" -d '{"sepal_length":5.1,
"sepal_width": 3.8,
"petal_length":1.9,
"petal_width":0.4}' -XPOST http://0.0.0.0:8000/predict


curl -H "Content-Type: application/json" -d '{"sepal_length":1.1,
"sepal_width": 1.8,
"petal_length":0.1,
"petal_width":0.4}' -XPOST http://0.0.0.0:8000/predict


    Note: To complete installation, ensure `eb` is in PATH. You can ensure this by executing:

    1. Bash:

       echo 'export PATH="/home/ubuntu/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile

    2. Zsh:

       echo 'export PATH="/home/ubuntu/.ebcli-virtual-env/executables:$PATH"' >> ~/.zshenv && source ~/.zshenv

Para pruebas, se tiene que poner en marcha:
docker build . -t fast_api_model
docker run -p 8000:8000 fast_api_model
