import pandas as pd
import numpy as np
from geopy import distance

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == "red":
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise ValueError("Undefined instruction for color:", light)

# def car_at_light(light):
#     if light == 'red':
#         return 'stop'
#     elif light == 'green':
#         return 'go'
#     elif light == 'yellow':
#         return 'wait'
#     else:
#         raise Exception("Undefined instruction for color:", light)

# def car_at_light(light):
#     try:
#         if light == 'red':
#             message = 'stop'
#         elif light == 'green':
#             message = 'go'
#         elif light == 'yellow':
#             message = 'wait'
#         return message
#     except UnboundLocalError:
#         print("Undefined instruction for color: " + light)
#         raise

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(val1: int,val2: int):
    try: 
        result = val2 - val1
        return result
    except TypeError: 
        return 'None'

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': Doe, 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

    
def retrieve_age_lbyl(person):
    if 'name' in person and 'birth' in person:
        age = 2021 - person['birth']
        return person['name'] + " is " + str(age) + " years old"
    else:
        return "Some keys are missing"


def retrieve_age_eafp(person):
    try:
        age = 2021-person['birth']
        return person['name'] + " is " + str(age) + " years old"
    except KeyError:
        return "Some keys are missing"
    
# dic1 =dict({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
# dic2 =dict({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
# retrieve_age_lbyl(dic1)
# retrieve_age_eafp(dic1)
# retrieve_age_lbyl(dic2)
# retrieve_age_eafp(dic2)

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

# def read_data(file_name):
#     try:
#         open(file_name, "r")
#         return 1
#     except IOError:
#         print ("Error: File does not appear to exist.")
#         return 0

def read_data(file_name):
    try:
        return pd.read_csv(file_name)
    except IOError:
        return "Error: File does not appear to exist."

# read_data("testfile")
# print(result)

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them

### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double # it should add double of elem
    #total_double_sum += elem

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings+"_"+string # it should refer to the cummulative variable
    # strings = string+"_"+string

### (c) Careful!
j=10
while j > 0:
    j -= 1 # if j increases, the while condition will never be false and stop the loop
    # j += 1

### (d)
# productory = 0 # it is a product, if it starts as 0, it will always be 0
productory = 1
for elem in [1, 5, 25]:
    productory *= elem


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(text_list):
    return len(list(filter(lambda x: "Simba" in x, text_list)))

# example = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
# count_simba(example)

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(date_list):
    return pd.DataFrame(np.array(list(map(lambda x: x.split("-"), date_list))), 
                        columns = ["year", "month", "day"])

# example = ["2021-11-12", "2018-12-05", "2017-02-17", "2021-11-06", "2019-03-27"]
# get_day_month_year(example)
    
# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

def compute_distance(latlong_tupple):
    return list(map(lambda x: distance.distance(x[0],x[1]).km, latlong_tupple))

# example = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# compute_distance(example)

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(int_list):
    acusum = 0
    for x in int_list:
        if type(x) is not list:
            acusum += x
        else:
            acusum += sum_general_int_list(x)
    return acusum

# example = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
# sum_general_int_list(example)
