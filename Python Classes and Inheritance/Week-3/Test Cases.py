#Q-1.

import test


def mySum(list):
    if len(list) > 0:
        res = 0
        for i in list:
            res += i
        return res
    else:
        return 0 

#Q-2.  Which of the following cases fail for the mySum function?
A. an empty list
B. a list with one item
C. a list with more than one item

Answer A, C

#Q-3. Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?

Answer No

#Q-4.

class Student:
    def __init__(self, name, year_UM, knowledge):
        self.name = name
        self.year_UM = year_UM
        self.knowledge = knowledge

    def study(self):
        self.knowledge += 1
        return None

    def getKnowledge(self):
        return self.knowledge

    def year_at_umich(self):
        return self.year_UM

#Q-5.Which of the following cases fail for the Student class?
A. the method study does not return None
B. the optional integer in the constructor is not optional
C. the attributes/instance variables are not correctly assigned in the constructor
D. the method study does not increase self.knowledge
E. the method year_at_umich does not return the value of self.years_UM

Answer C, D

#Q-6.  Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?

Answer Yes


