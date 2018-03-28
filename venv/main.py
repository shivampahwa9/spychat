from spy_details import spy_name,spy_salutation,spy_age,spy_rating

#print("Spychat")

#spy_salutation=input("What should we call you(Mr. or Ms.)?")

#print(spy_salutation)

#spy_name=input("What is your name?")

#print(spy_name)

#print("Welcome to spychat" +" "+ spy_salutation +" "+ spy_name)

#print("Alright"+" "+ spy_salutation +" "+spy_name+" " +"I'd like to know a little bit more about you....")

####### new user or default ####
STATUS_MESSAGES=["MY NAME IS SHIVAM","SHAKEN,NOT STIRRED"]
friends_name=[]
friends_age= []
friends_rating=[]
friends_is_online=[]

def add_status(current_status):

    if current_status!= None:
        print("your current status is "+ current_status+"\n")
    else:
        print("you do not have any current status")
    default = input("\nDo you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = input("\nWhat status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
            print(STATUS_MESSAGES)

    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print (str(item_position) +"."+message)
            item_position = item_position+1
        message_selection = int(input("\nchoose from the above messages"))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection-1]
    return updated_status_message



def start_chat(spy_name,spy_age):
    show_menu=True
    current_status=None
    while show_menu==True:
        menu_choices = ("what do you want to do \n1.Add a status \n2.exit")
        menu_choice = int(input(menu_choices))

        if menu_choice == 1:
            print("update the status what you want to update")
            current_status=add_status(current_status)
        elif menu_choice== 2 :
            show_menu=False
############# add a friend
def add_friend():
    print("\nAdd a new friend")
    new_name = input("\nYour friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = int(input("Age?"))
    new_rating = int(input("Spy rating?"))

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        print(new_name)

    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(friends_name)


user=("continue as a "+spy_salutation+" "+spy_name+" (Y/N)")
existing=input(user)
if existing == "Y":
    start_chat(spy_name,spy_age)
    add_friend()
else:
    username=input("what is your name")
    if len(username)>=3:

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
        print("welcome to spychat" +" "+spy_salutation1+" "+username+".You are"+" "+str(spy_age)+" "+"years old."+" "+str(spy_rating)+" "+"rating you have given")
        start_chat(spy_name, spy_age)
        add_friend()
    else:
        print("age is not valid")





