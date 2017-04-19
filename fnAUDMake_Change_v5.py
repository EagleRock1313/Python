#! /usr/bin/python3
# 11/20/16 Sandy L. Ortiz INFO 246-13 Python Lab #6 exercise 2 function fnAUDMake_change

"""
Author: Sandy L. Ortiz INFO 246-13 FALL 2016

Purpose: Calculate change due and count number of currency and coin needed for change in AUD.

Algorithm:
1. Get the input for amount tender and amount due.
2. Adapt USD variables for use with AUD currency. Maintin legacy code and logic.
3. Include a Try/Except for error handling of amounts over $100.
4. Subtract the amount due from the amount tendered to calcualte the change returned.
5. Cast the dollars variable to integer to remove the float value.
6. Subtract the dollars from total amount due to calculate cents.
7. Convert AUD $2 coin and $1 coin.  Count as dollars and print as cents using global variables.
8. Iterate and count dollars.
9. Iterate and count cents.
10. Print dollar count not equal to zero
11. Print cents count not equal to zero
12. Test for input values over $100
13. Test for input values other than string.

Reference: https://www.dotnetperls.com/divmod-python

Test Case:
1)21.21 amt_due, 51.51 amt_tender = 30.30 ret_chg, count (20), 10(1), .25(1),.05(1)
2)4.50 amt_due, 10 amt_tender = 5.50 ret_chg, count 5(1),.50(1)
3)49 amt_due, 100 amt_tender = 51 ret_chg, count 50(1), 1(1)
4)48 amt_due, 100 amt_tender = 52 ret_chg, count 50(1), 2(1)
5)200 amt_due, 200 amt_tender = exception block
6)spacebar input > ValueError

"""


def fnMake_change(amt_due,amt_tend):
    #calcuate return amount
    ret_amt = amt_tend - amt_due
    #cast to integer dollars
    dollars = int(ret_amt)
    #allow floating point cents
    cents = (ret_amt - dollars)
    print("Amount due and amount tendered:\t",amt_due, amt_tend)
    print ("Return Amount:\t",format(ret_amt,".2f"))

    #iterate through dollars and count
    def make_dollars(dollars) :
        global AUD1
        global AUD2
        parts = divmod(dollars, 100)
        hundreds = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 50)
        fifties = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 20)
        twenties = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 10)
        tens = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 5)
        fives = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 2)
        AUD2 = parts[0]
        dollars_remaining = parts[1]
        parts = divmod(dollars_remaining, 1)
        AUD1 = parts[0]
        dollars_remaining = parts[1]
        print("Dollars:\t", dollars)
        
        #test for zero count and ouput dollars counted
        while hundreds != 0 :
            print("Hundreds:\t", hundreds)
            break
        while fifties != 0 :
            print("Fifties:\t", fifties)
            break
        while twenties !=0 :
            print("Twenties:\t", twenties)
            break
        while tens !=0 :
            print("Tens:\t\t", tens) 
            break
        while fives !=0 :
            print("Fives:\t\t", fives) 
            break
    make_dollars(dollars)

    #iterate through coins and count
    #code adapted from USD program, variables in USD
    #indent code block for variable scope
    def make_cents(cents) :
            global AUD1
            global AUD2
            parts = divmod(cents,(200*.01))           #legacy code ignored by interpreter
            quarters = parts[0]                       #replaced with global variables 
            cents_remaining = parts[1]                #AUD1 and AUD2
            parts = divmod(cents_remaining,(100*.01)) #
            dimes = parts[0]                          #
            cents_remaining = parts[1]                #
            parts = divmod(cents_remaining,(50*.01))
            nickels = parts[0]
            cents_remaining = parts[1]
            parts = divmod(cents_remaining,5)
            pennies = parts[0]
            cents_remaining = parts[1]
            print("Cents:\t\t", float(cents))

        #test for zero count and output coins counted
        #code adapted from USD program, variables in USD
            while AUD2 != 0 :
                print("$2 coin:\t", AUD2)
                break
            while AUD1 != 0 :
                print("$1 coin:\t", AUD1)
                break
            while nickels != 0 :
                print("$.50 coin:\t", nickels)
                break
            while pennies != 0 :
                print("$.05 coin:\t", pennies,"\n") 
                break
    make_cents(cents)

def main():
    try:
        #get inputs and cast from string to float
        amt_due= float(input("Please enter amount due: "))
        amt_tend= float(input("Please enter amount tendered: "))

        #test for value less than or equal to 100, handle input exceptions
        if amt_due <= 100 and amt_tend <= 100 :
            fnMake_change(amt_due, amt_tend) #call fnMake_change and pass float
        else :
            print ("Sorry, amount due or amount tendered must be $100 or less")
            repeat = input ("Would you like to try again? ")
            repeat.lower()
            while repeat == "n":
                exit()
            while repeat == "y":
                main()
                break
            
    #handle value exceptions, incorrect characters or spacebar        
    except (ValueError) as e:
        print ("Sorry, there was an input error.")
        repeat = input ("Would you like to try again? ")
        repeat.lower()
        if repeat == "y":
            main()
        else :
            exit()
main()
