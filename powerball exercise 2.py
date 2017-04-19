#! /usr/bin/python3
# 11/09/16 Sandy L. Ortiz INFO 246-13 Python Lab #5 exercise 2 powerball program

"""
Author: Sandy L. Ortiz INFO 246-13 FALL 2016

Algorithim:
New York State Mega Millions(NYSMM) - Write a function to select 1 set of 5 random numbers, and powerball and print
Call the function 5 times with a for loop and range() to create 5 sets of numbers
End function by printing message "Good Luck!"

Test Cases:
Run the program to determine if 5 sets of 5 random numbers and powerball
are printed.
"""

def NYSMM() :
    print("\nWelcome to the New York State Mega Millions random number generator.")
    for number in range(5) :

        # Generate empty list of numbers
        from random import randint
        list = [] 

        #Pick 5 random numbers
        for x in range(5):
            next = randint(1,75)
            while next in list:
                next = randint(1,75)
            list.append(next)
            
        #Sort list into ascending order, print list and powerball number
        list.sort() 
        for x in range(5):
            print(list.pop(0), end=", ")
        print ("Powerball" , randint(1,15))
    print ("Good Luck!\n")
NYSMM()
