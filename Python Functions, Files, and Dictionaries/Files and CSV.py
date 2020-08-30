Q-1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number
of characters in the file and save to the variable num.

file = open("travel_plans.txt", "r")
a = file.read()
num = len(a)
print(num)
