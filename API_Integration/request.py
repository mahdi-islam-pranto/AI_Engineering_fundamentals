import requests

# Define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"
# Send a GET request to the API
response = requests.get(url)

if response.status_code == 200:
    # Get the response data
    data = response.json()
    # print 1st data from the response
    print("Response Data: \n")
    print(data[0])
else:
    print("Request failed with status code:", response.status_code)


# parameterized api request
param_url = "https://jsonplaceholder.typicode.com/posts"
# define the query parameters
parameters = {
    "userId": 1,
    "id": 4
}
# send a GET request to the API with the query parameters
param_response = requests.get(param_url, params=parameters)

if param_response.status_code == 200:
    # Get the response data
    param_data = param_response.json()
    print("Response Data of parameters: \n")
    print(param_data)
else:
    print("Request failed with status code:", param_response.status_code)



# make a post request
post_url = "https://jsonplaceholder.typicode.com/posts"
# define the data to be sent in the request body
post_data_body = {
    "title": "pranto",
    "body": "bar",
    "userId": 1
}

post_response = requests.post(post_url, json=post_data_body)

print(post_response.status_code)
if post_response.status_code == 201:
    print("Post request successful")
    print("Response Data: \n")
    print(post_response.json())
else:
    print("Post request failed with status code:", post_response.status_code)