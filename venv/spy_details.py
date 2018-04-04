#spy_name="shivam"
#spy_salutation="Mr"
#spy_age=21
#spy_rating=5




class spy:
    def __init__(self,name,salutation,rating,age):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy("Shivam Pahwa", "Mr.", 22, 5)
friend_one = Spy('Aman', 'Mr.', 27, 4.9)
friend_two = Spy('James', 'Mr.', 21, 4.39)
friend_three = Spy('Raghav', 'Mr.', 37, 4.95)

friends=[friend_one,friend_two,friend_three]

class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


