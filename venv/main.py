from spy_details import spy_name,spy_salutation,spy_age,spy_rating
from spy_details import spy

#print("Spychat")

#spy_salutation=input("What should we call you(Mr. or Ms.)?")

#print(spy_salutation)

#spy_name=input("What is your name?")

#print(spy_name)

#print("Welcome to spychat" +" "+ spy_salutation +" "+ spy_name)

#print("Alright"+" "+ spy_salutation +" "+spy_name+" " +"I'd like to know a little bit more about you....")

####### new user or default ####
STATUS_MESSAGES=["MY NAME IS SHIVAM","SHAKEN,NOT STIRRED"]
Friends=[]

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



def start_chat(spy_name,spy_age,spy_rating):
    show_menu=True
    current_status=None
    while show_menu==True:
        menu_choices = ("what do you want to do \n1.Add a status \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read chats from user \n6.Close Application")
        menu_choice = int(input(menu_choices))

        if menu_choice == 1:
            print("update the status what you want to update")
            current_status=add_status(current_status)
        elif menu_choice== 2 :
            number_of_friends = add_friend()
            print("You have %d friends"%add_friend())
        elif menu_choice == 6 :
            show_menu == False

############# add a friend
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name']= input("\nYour friend's name:")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = int(input("Age?"))
    new_friend['rating'] = int(input("Spy rating?"))

    if len(new_friend['name']) > 0 and new_friend['age']> 12 and new_friend['rating'] >= spy['rating']:
        Friends.append(new_friend)

    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(Friends)


user=("continue as a "+spy_salutation+" "+spy_name+" (Y/N)")
existing=input(user)
if existing == "Y":
    start_chat(spy_name,spy_age,spy_rating)

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





