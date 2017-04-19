#! /usr/bin/python3
# 11/09/16 Sandy L. Ortiz INFO 246-13 Python Lab #5 exercise 3 amended powerball program

"""
Author: Sandy L. Ortiz INFO 246-13 FALL 2016

Algorithim:
Use a single function to run multiple lottery numbers. Request input of lottery parameter. Print one set of numbers. Ask to repeat
for each lottery random number generator.
(PB)
PowerBall will select 5 different numbers from 1-69 and powerball 1-26.
(NYSMM)
New York State Mega Millions will select 5 different numbers from 1-75
and powerball 1-15.
(NYSL)
New York State Lotto will select 6 numbers from 1-59. No powerball number.

Test Cases:
Provide input parameter for each case, PB, NYSMM, NYSL and print one set
of random numbers for each case.
"""



def func_lottery(lotto) :

    ####Powerball (PB)###            
    if  lotto=="pb" :
        
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
            print("NYS Powerball lottery numbers ", list.pop(0), end=", \n")
        print ("Powerball" , randint(1,15), "\n")

        #Return to main function
        repeat = (input("Would you like to play another lottery? Y or N?  "))
        repeat.lower
        if repeat == "y" :
            main()
        else :
            print("Ok. Goodbye.")

    ###New York State Mega Millions (NYSMM)###
    elif lotto=="nysmm" :
        
        # Generate empty list of numbers
        from random import randint
        list = [] 

        #Pick 5 random numbers
        for x in range(5):
            next = randint(1,69)
            while next in list:
                next = randint(1,69)
            list.append(next)
            
        #Sort list into ascending order, print list and powerball number
        list.sort() 
        for x in range(5):
            print("NYSMM lottery numbers ", list.pop(0), end=", \n")
        print ("Powerball" , randint(1,26), "\n")
        #Return to main function
        repeat = (input("Would you like to play another lottery? Y or N?  "))
        repeat.lower
        if repeat == "y" :
            main()
        else :
            print("Ok. Goodbye.")
            
    ###New York State Lottery (NYSL)###         
    elif lotto=="nysl" :
        
        # Generate empty list of numbers
        from random import randint
        list = [] 

        #Pick 5 random numbers
        for x in range(5):
            next = randint(1,59)
            while next in list:
                next = randint(1,59)
            list.append(next)
            
        #Sort list into ascending order, print list and powerball number
        list.sort() 
        for x in range(5):
            print("NYSL lottery numbers ", list.pop(0), end=", \n")

        #Return to main function
        repeat = (input("Would you like to play another lottery? Y or N?  "))
        repeat.lower
        if repeat == "y" :
            main()
        else :
            print("Ok. Goodbye.")

def main() :
        lotto = input("Please pick your New York State lottery, PB, NYSMM or NYSL. ")
        lotto.lower  
        func_lottery(lotto)
        

main()


