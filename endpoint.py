import requests
import json

scoring_uri = 'http://cbce5c7c-b362-49f5-891c-e62d284d6831.southcentralus.azurecontainer.io/score'
key = 'SPVQXTA00qrUBcfQN0eKRsn3AyiKSv24'

data = {
    "data":[
        {
            "Column1": 150,
            "age": 44,
            "sex": 1,
            "cp": 2,
            "trestbps": 120,
            "chol": 226,
            "fbs": 0,
            "restecg": 1,
            "thalach": 169,
            "exang": 0,
            "oldpeak": 0.1,
            "slope": 2,
            "ca": 0,
            "thal": 2
        },
        {
            "Column1": 300,
            "age": 57,
            "sex": 0,
            "cp": 0,
            "trestbps": 140,
            "chol": 241,
            "fbs": 0,
            "restecg": 1,
            "thalach": 123,
            "exang": 1,
            "oldpeak": 0.2,
            "slope": 1,
            "ca": 0,
            "thal": 3         
        }
    ]
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
