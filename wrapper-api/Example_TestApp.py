import sys
from WrapperAPI import Wrapper_API

server = "https://198.18.133.8"



ourRequest = Wrapper_API(server, username, password)

print "Authenticating..."
ourRequest.authentication()
print "Successful"

a = ourRequest.GETWhiteList()

print a
