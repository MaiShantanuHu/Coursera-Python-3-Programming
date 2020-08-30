''' Q-1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number
of characters in the file and save to the variable num. '''

file = open("travel_plans.txt", "r")
a = file.read()
num = len(a)
print(num)

''' Q-2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number
of words in the file and assign this value to the variable num_words.'''

file = open("emotion_words.txt", "r")
a = file.read()
a = a.split()
count = 0
for _ in a:
    count+=1
num_words = count
print(num_words)

''' Q-3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.'''

file = open("school_prompt.txt", "r")
a = file.readlines()
num_lines = len(a)
print(num_lines)
file.close()    

''' Q-4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.'''

file = open("school_prompt.txt", "r")
a = file.read()
beginning_chars = a[:30]
print(beginning_chars)

''' Q-5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.'''

three = []
with open("school_prompt.txt", "r") as f:
    three = [line.split()[2] for line in f]
    print(three)
    
''' Q-6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.'''

emotions = []
with open("emotion_words.txt", "r") as f:
    emotions = [line.split()[0] for line in f]
    print(emotions)
    
''' Q-7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.'''

file = open("travel_plans.txt", "r")
a = file.read()
first_chars = a[:33]
print(first_chars)

''' Q-8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.'''

file = open("school_prompt.txt", "r")
a = file.read().split()
p_words = [x for x in a if "p" in x]
print(p_words)
