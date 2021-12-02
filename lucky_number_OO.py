"""
 Use any Object-Oriented language to complete this task.

# Create a class named LuckyNumber.

# The constructor for LuckyNumber should take a single argument: a string called first_name (e.g.: "Marc").

# In the LuckyNumber class create two methods, generate_data and display_data, that take no arguments.

# The generate_data method should create and return a new object everytime it is called. (e.g. Python dictionary, Java Map)

# The object returned by generate_data method should contain 2 things:

# 1) A field named "date" with the current date in string format.

# 2) A field named "lucky_number" with a random floating point number between 0-100 in string format (2 decimal places).

# e.g. { "date": "23 Nov 2021", "lucky_number": "55.67" }

# The display_data method should do two things:

# 1) Call the generate_data method to retrieve a new date and lucky_number.

# 2) Print a message addressed to first_name, along with the date and lucky number.

# e.g.: "Hello Marc, your lucky number for 23 Nov 2021 is: 55.67"

# Finally, create an object of type LuckyNumber and call the display_data method.
"""


import random
from datetime import datetime


names = ['Marc','Alice','Bob','Charlie','Dave','Eve']


def myrand():
    return round(random.uniform(1,101),2)

def mynow():
    return datetime.now().strftime('%Y-%m-%d')


class LuckyNumber():
    def __init__(self,first_name):
        self.first_name = first_name
   #
    def generate_data():
        return {'date':mynow(), 'lucky_number':myrand()}
   #
    def display_data(self):
        name = self.first_name
        mydata = LuckyNumber.generate_data()
        date, num = mydata['date'], mydata['lucky_number']
        return f"Hello, {name}, your lucky number for {date} is {num}"



# demo
#In [94]: foo = LuckyNumber("Alice")
#
#In [95]: foo.first_name
#Out[95]: 'Alice'
#
#In [96]: foo.display_data()
#Out[96]: 'Hello, Alice, your lucky number for 2021-12-02 is 74.63'
#
#
