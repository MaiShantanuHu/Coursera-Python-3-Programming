####  Q-1. Could aliasing cause potential confusion in this problem?
```
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
```
#Answer: Yes, b and z reference the same list and changes are made using both aliases.

#### Q-2. Could aliasing cause potential confusion in this problem?
```
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
```
#Answer: Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.

#### Q-3. Which of these is a correct reference diagram following the execution of the following code?
```
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
```
#### 1. 
![](https://fopp.umsi.education/books/published/fopp/_images//week3a1_1.png)
#### 2. 
![](https://fopp.umsi.education/books/published/fopp/_images//week3a1_2.png)

#Answer: 1

#### Q-4:  Which of these is a correct reference diagram following the execution of the following code?
```
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
```
#### 1.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_1.png)
#### 2.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_2.png)
#### 3.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_3.png)
#### 4. 
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_4.png)

#Answer: 4

#### Q-5. Which of these is a correct reference diagram following the execution of the following code?
```
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
```
#### 1. 
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_1.png)
#### 2.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_2.png)
#### 3. 
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_3.png)
#### 4.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_4.png)

#Answer: 1
