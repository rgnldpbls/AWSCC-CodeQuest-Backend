import requests

api_url = "https://api.spacexdata.com/v5/launches/latest"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    launch = data["launch"]
    print(f"Launch: {launch}")
else:
    print(f"Request failed with status code: {response.status_code}")