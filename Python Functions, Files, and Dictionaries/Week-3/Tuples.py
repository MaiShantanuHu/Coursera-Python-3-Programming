''' Q-1. Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.'''

olympics = ("Beijing", "London", "Rio", "Tokyo")
print(olympics)

''' Q-2. The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this
list to the variable country.'''

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = [lis[1] for lis in tuples_lst]
print(country)

 
