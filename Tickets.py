x = 0 
while x == 0:
    age = input("enter your age: ")
    age = int(age)

    #condition_1
    if age < 3 or age == 3 :
        print("the ticket is free for age 3 below")
    elif age > 3 and age <= 12 :
        print("The ticket  price for ages between 3 and 12 is MWK 1,000")
    else :
        print("the price for ages above 12 is MWK 1,500")        