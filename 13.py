import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.phone("Bert")
#555-ITALY
#italy.html
