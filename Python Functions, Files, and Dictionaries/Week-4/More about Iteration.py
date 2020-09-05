''' Q-1. Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a
sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should
not contain the number 5).'''

def sublist(x):
    sub = []
    x = (num for num in x)
    num = next(x, 5)
    while num != 5:
        sub.append(num)
        num = next(x, 5)
    print(sub)
    return sub
x = [1, 2,3,4,5,1,2,3]
sublist(x)

''' Q-2. Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element
of the list is the number 7. What is returned is a list of all of the numbers up until it reaches '''

def check_nums(x):
    sub = []
    x = (num for num in x)
    num = next(x, 7)
    while num != 7:
        sub.append(num)
        num = next(x, 7)
        
    
    return sub

''' Q-3. Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist
of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not
contain the string “STOP”).'''

def sublist(list):
    i = 0
    while i < len(list):
        if list[i] == "STOP":
            return list[0:i]
        i+=1
    return list[0:i]

print(sublist(["mujju", "randi", "shona", "dhona", "STOP"]))

''' Q-4. '''



''' Q-5. Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem,
vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.'''

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
s = list(s)
num_vowels = 0
for i in s:
    for j in i:
        if j in vowels:
            num_vowels+=1

print(num_vowels)    
