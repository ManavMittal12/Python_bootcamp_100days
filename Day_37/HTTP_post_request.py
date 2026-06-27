# HTTP Post Request

# we have been using the request module to make
# HTTP request all over the internet

# we saw get request, it gets pieces of data from the API provider
# there are 4 types of request
# 1) GET    - requests.get(parameters)
# 2) POST - requests.post()
# 3) PUT - requests.put()
# 4) DELETE - requests.delete()


# get - we ask an external system for some data, and it sends us that

# post request - when we give the external system some piece of data and not interested in the response we are getting
# back other than if it was successful or not.
# eg- we want to post a data in Google sheet or tweet on Twitter.

# PUT request - we update the data in an external system we have api of, like we want to update the data from the
# Google sheets

# DELETE requests - where we want to delete a piece of data from an external system, like deleting a tweet


import requests
from urllib3.util import url

user_params = {
    "token" : "(sd234as14/!@41241",
    "username" : "kakashiofthesharingan",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}


# username creation
# our parameter looks like JSON, so we are using the keyword here.
response = requests.post(url="https://pixe.la/v1/users", json=user_params)
print(response.text)
