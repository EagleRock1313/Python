#! /usr/bin/python3
# 11/03/16 Python Lab 3 Exercise 1 trip_compare.py
'''
Author: Sandy L. Ortiz

Problem: Compute whether it is cheaper to drive your own car or use a rental on a trip from New York suburbs to downtown Washington, DC.

Algorithm:
1. Ask, "What is the distance involved?"
2. Ask miles per gallon(mpg) expected for both own car and rental car
3. Ask for the rental cost per day (and perhaps per mile, if over xxx miles per day of rental)
4. Double the miles to get total miles (since round trip) -- or drop-off charge, if just one way

Assumptions:
1. Gasoline pricing is the same everywhere (obviously not true)
2. Fill tank for the trip and not again later (actually, it would be cheaper to buy gasoline along the way,
but that requires alot of knowledge as to where to refill).
3. the rental car will have to be filled up on return to renting company (generally getting gasoline at
end of trip from the rental company is considerably more expensive)
4. A rental car will different miles per gallon for the trip (probably not true, but it will depend on the
two vehicles)
5. Rental cars have a per day chage + either unlimited mileage or per mileage charge if over day limit
6. Tolls would be the same for both own car and rental (reasonable)
7. Round-trip is required! (did you think about this?)

Updates:
11/03/16
REM 1. Cast to integer gallons_owncar, gallons_rental, owncar_costpermile, rental_costpermile
2. Format ".2f" gallons_owncar, gallons_rental, owncar_costpermile, rental_costpermile

'''

#Get Inputs
distance=eval(input("Please enter the one-way distance involved:\t"))
cost_of_gasoline=eval(input("Please enter your cost for a gallon of gas:\t"))
mpg=eval(input("What is your expected mpg?\t\t\t"))
rental_mpg=eval(input("What is the rental car mpg?\t\t\t"))
rental_perday=eval(input("What is the rental rate per day?\t\t"))

distance*=2    #roundtrip=twice the one-way distance
gallons_owncar= distance/mpg
gallons_rental= distance/rental_mpg
tolls=40        #irrelevant, since same for own car & rental

owncar_costpermile = cost_of_gasoline/mpg
rental_costpermile = cost_of_gasoline/rental_mpg

owncar_totalcost=owncar_costpermile * distance + tolls
rental_totalcost=rental_costpermile * distance + tolls + rental_perday
                    
#Debugging: When not debugging, put "#" in from of each of next 4 active lines
print("Cost per mile for gas (own car)\t\t\t", format(owncar_costpermile,".2f"))
print ("Gallons of gasoline needed (own car)\t\t", format(gallons_owncar, ".2f"))

print("Cost per mile for gas (rental)\t\t\t", format(rental_costpermile, ".2f"))
print("Gallons of gasoline needed (rental)\t\t", format(gallons_rental, ".2f"))

#Print out the conclusion with supporting calculations -- Which is better to drive: own or rental car?
print()
print("Cost, if driving own car, is $", end="")
print(format(owncar_totalcost,".2f"))
print("Cost, if driving rental, is $", end="")
print(format(rental_totalcost,".2f"))

if owncar_totalcost == rental_totalcost:
    print("The costs are the same")
elif owncar_totalcost<rental_totalcost:
    print("Cheaper to use own car")
else:
    print("Cheaper to use rental car")
