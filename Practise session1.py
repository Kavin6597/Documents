#Python List

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

#Lists allow duplicate values

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#List Length

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

#List items can be of any data type:

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

#A list with strings, integers and boolean values
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

#What is the data type of a list?
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

#Print the second item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

#Print the last item of the list
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

#Return the third, fourth, and fifth item:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

#Range of Negative Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

#Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

#Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

#Append Items

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

#Insert Items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

#Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#Remove Specified Item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


#Sort List Alphanumerically
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

#Sort Descending
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = )
# print(thislist)

#Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

#Tuples are same as list but it cannot alter or change the values in it but can add duplicates

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

#set allows only unique value,duplicates not allowed,unchangeble

# thisset = {"apple", "banana", "cherry", "cherry",}
# print(thisset)

#Dictionaries used to assign a value to a key 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

#if statement

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

#if else

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

#Else

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

#The while Loop

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#For

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
