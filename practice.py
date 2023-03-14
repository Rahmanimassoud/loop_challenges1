import random
# # DATA TYPES

# # There are 2 Data types in Python PRIMITIVE AND COMPOSITE

# # PRIMITIVE DATA TYPES are (Boolean values, Numbers and Strings).

# # COMPOSITE DATA TYPES (Tuples, Lists, Dictionaries).

# # Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])
# # dog[1] = 'dachshund'  this would error cuz Tuples are immutable and we can't modify it.

# # Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[0])
# ninjas[2] = 'Jamal'
# ninjas.append('Massoud')
# print(ninjas)
# ninjas.pop()
# print(ninjas)
# ninjas.pop(1)
# print(ninjas)

# # Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods.
# empty_dict = {}
# new_person = {"name": "John", "age": 38, "weight": 160.5, "has_glassess": False}
# new_person["name"] = "Jack"
# print(new_person)
# new_person['hobbies'] = ['hikking', 'coding']
# print(new_person)
# copy_age = new_person.pop('age')
# print(new_person)
# print(copy_age)
# print(type('name'))
# print(type(new_person))
# print(type(copy_age))
# # print(len(copy_age)) would error cuz int has no length
# print(len(new_person))
# print(len("CodingDojo"))
# dec = 4.2
# print(type(dec))

# rand_num = random.randint(0,10)
# print(rand_num)
# print(type(3j))
# print(type(4.2))
# print(type(39))

# int_to_complex = complex(35)
# print(int_to_complex)
# print(type(int_to_complex))

first_name  = "Zen"
last_name = "Coder"
age = 17
work = 5
hobby = "Coding"
# print(f"my name is {first_name} {last_name} i'm {age} years old and my hobby is {hobby}.") #this is called string interpolation using the f string method

# print("my name is {} {} i'm {} years old and my hobby is {}.".format(first_name, last_name, age, hobby)) #This called string interpolation using the .format() method

# greeting = "Hello my name is ", first_name, last_name
# print("Hello my name is ", first_name, last_name)
# print("I worked in the field for " + str(age - work) + " years")
# print(f"i worked in the field for {age - work} years")
# print("I worked in the field {} years".format(age - work))

fruits = ['apple', 'banana', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
salad = 3 * fruits
# print(salad)
mixed_list = ['mango', [1213, 14], 'me']
# print(mixed_list)

drawers = ["documents", "envelops", "pens"]
# print(drawers[0])
drawers[0] = "tchotchkes"
# print(drawers[0])
drawers[1] = drawers[0]
# print(drawers)
top_content = drawers[0]
# print(top_content)

words = ["start", "going", "till", "the", "end"]
# print(words[1:])
# print(words[:4])
# print(words[2:4])
copy_of_list = words[:]
# print(copy_of_list)
copy_of_list.append("DOJOOOO")
# print(copy_of_list)


my_list = ["Zen", "John", "Zen","Khan", "Ahmad"]
# print(len(my_list))
# my_list.append(999)
# my_list.reverse()
# my_list.sort()
# my_list.count("Zen")
# print(my_list)

# ===========================Tuples===============================
# We can declare tuples using () like variable = (1,3,"hgghg", 9)
# are same as lists but we they are immutable means we can add or remove things.

# =========================CONDITIONALS==========================

# if, elif, else

# x = 12
# if x > 50:
#     print("Bigger number than 50")
# elif x < 10: 
#     print("Smaller number")
# else:
#     print("Ok good")


# ===================Loops======================
# for i in range(1, 21):
#     print(i)

# for x in "Hello":
#     print(x)

# string = "Hello World"
# for i in string:
#     print(i)

# my_list = ["abc", 123, "xyz"]
# # for i in range(0, len(my_list)):
#     # print("index", i, my_list[i])

# for x in my_list:
#     print(x)

# count = 0
# while count <= 5:
#     print("Looping - ", count , "Times")
#     count += 1

