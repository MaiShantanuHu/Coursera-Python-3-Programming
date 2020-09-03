''' Q-1. Write a function called int_return that takes an integer as input and returns the same integer.'''

def int_return(x):
    return x

int_return(3)
    
''' Q-2. Write a function called add that takes any number as its input and returns that sum with 2 added.'''

def add(y):
    z = 2 + y
    return z

r = add(2)
print(r)

''' Q-3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.'''

def change(x):
    z = x + "Nice to meet you!"
    return z
r = change("hii bro")
print(r)

''' Q-4. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.'''

def accum(lst):
    j=0
    for i in lst:
        j=j+i
    return j
lst=[1,2,3,4,5,6,7,8,9]
accum(lst)


''' Q-5. Write a function, length, that takes in a list as the input.
If the length of the list is greater than or equal to 5, return “Longer than 5”.
If the length is less than 5, return “Less than 5”.'''


def length(lst):
    if len(lst)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'

lst=list(input())
length(lst)

