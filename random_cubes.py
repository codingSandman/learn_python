"""
exercise: random integer counter. How often do you roll the dice?
Work with variables, dictionaries, random and for-loops
2024-01-23 // @author codingSandman // free to use and copy
"""

from random import randint

count_dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} #counter for all rounds
cube_number = randint(1,6) #random number between 1-6
count = int(input("How often would you roll the dice?: "))

for num in range(count):
    cube_number = randint(1,6) #cube number 
    count_dic[cube_number] += 1

print(count_dic)
