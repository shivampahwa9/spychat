import spy_details
print("Spychat")

spy_salutation=input("What should we call you(Mr. or Ms.)?")

print(spy_salutation)

spy_name=input("What is your name?")

print(spy_name)

print("Welcome to spychat" +" "+ spy_salutation +" "+ spy_name)

print("Alright"+" "+ spy_salutation +" "+spy_name+" " +"I'd like to know a little bit more about you....")
####### new user or default ####
user=input("Do you want to create as a new user(YES) or continue as a default user (NO)")
print(user)
if len(user)>=3:
    spy_name1=input("what is your name?")
    print(spy_name1)
    spy_salutation1=input("what should we call you(Mr. or Ms.)?")
    print(spy_salutation1)
    spy_age=input("What is your age?")
    print(spy_age)
    spy_rating=int(input("what rating you want to give?"))
    print("spy_rating")
    if spy_rating>4:
        print("great app")
    elif spy_rating>3 and spy_rating<=4:
        print("nice app")
    else:
        print("not good")
    print("welcome to spychat" +" "+spy_salutation1+" "+spy_name1+".You are"+" "+str(spy_age)+" "+"years old."+" "+str(spy_rating)+" "+"rating you have given")
else:
    print("continue as a "+spy_details.spy_salutation+" "+spy_details.spy_name)
    print(spy_details.spy_salutation+" "+spy_details.spy_name)
    print("Age"+str(spy_details.spy_age))



