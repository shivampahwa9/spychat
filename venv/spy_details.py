from datetime import datetime


class Spy:
    def __init__(self, name, salutation, age, rating):
        self.old_friends = []
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = "yoooo :)"


existing_spy = Spy("Shivam", "Mr.", 21, 4.6)

# chat class
class ChatMessage:
    def __init__(self, name, message, isItYou):
        self.name = name
        self.message = message
        self.time = datetime.now()
        self.isItYou = isItYou