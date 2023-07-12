# Python Dates  
# import datetime

# x = datetime.datetime.now()
# print(x)

# import datetime
# x =datetime.datetime.now()
# print(x.year)
# print(x.strftime("%a"))


#month 
# import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%B"))

#Maths
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x)

# x = pow(4, 3)

# print(x)

# import math

# x = math.sqrt(64)

# print(x)

# import math

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1

# JSON
# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

# import json

# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))
