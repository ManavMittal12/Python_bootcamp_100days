import requests

USERNAME = "kakashiofthesharingan"
TOKEN = "(sd234as14/!@41241"

# Advanced Authentication using an HTTP Header
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id" : "meditationgraph1",
    "name" : "Meditation Graph",
    "unit" : "min",
    "type" : "int",
    "color" : "ichou",
}

# What are the header, it contains relevant pieces of information in a letter, and the body is the message part

#  the apikey if we directly use it in our code, is shown in the head of the link, which is not secure. Anyone can use this.
# So, API providers want us to provide the api key in headers.
# using http header

header = {
    "X-USER-TOKEN" : TOKEN
}


# using the HTTP header for authorization
response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)

# our graph --> https://pixe.la/v1/users/kakashiofthesharingan/graphs/meditationgraph1.html
