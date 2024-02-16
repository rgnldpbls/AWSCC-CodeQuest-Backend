import requests 

# API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"
post_url = "https://jsonplaceholder.typicode.com/create"

# Set Custom Headers
headers = {
    "User-Agent":"MyApp/1.0"
}

# Send the Get Request
response = requests.get(api_url, headers=headers)

# Display HTTP Status Code
print("Response Status Code:", response.status_code)

# Display Response Headers
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Display Response Content
print("Response Content:", response.text)

# Prepare Data for POST Request
data = {
    "title": "",
    "body": ""
}

# Send a Post Request
post_response = requests.post(post_url, json=data)

# Display HTTP Status Code
print("Response Status Code: ", post_response.status_code)

# Display Response Content
print("Response Content:", post_response.text)