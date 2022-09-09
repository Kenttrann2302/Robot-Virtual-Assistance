# import pyjokes into our python file
import pyjokes
import pywhatkit
from ai import AI
from todo import Todo
from todo import Item
from datetime import date
from datetime import datetime


alf = AI()
todo = Todo()

# introduce steps to set up the user's identification
def identification():
    identification = "Ok, "

# get the user's gender and find the pronoun

def gender():
    gender = "Ok, which gender would you like me define yourself as, if your gender is male, then your pronoun is Mr.,. Otherwise, if your gender is female, then your pronoun is Mrs, if you choose not to answer this question, you can say prefer not to answer."
    print("Plex:", gender)
    alf.say(gender)


# if the user's is a male
def male():
    male = "Ok, so your pronoun is Mr."
    print("Plex:", male)
    alf.say(male)

# if the user's is a female
def female():
    female = "Ok, so your pronoun is Mrs."
    print("Plex:", female)
    alf.say(female)



# define the current day:
def current_day():
    today = date.today()
    current_day = today.strftime("%B %d, %Y")
    print("Plex:", current_day)
    alf.say(current_day)

# define the current time:
def current_time():
    now = datetime.now()
    current_time = now.strftime("%H hours, %M minutes, %S seconds")
    print("Plex:", current_time)
    alf.say(current_time)

# define a joke
def joke():
    funny = pyjokes.get_joke()
    print("Plex:", funny)
    alf.say(funny)

# define the youtube's songs request from the users:
def song():
    song = command.replace('play', '')
    print("Playing", song)
    alf.say(song)
    pywhatkit.playonyt(song)

# add items to the list
def add_todo()->bool:
    item = Item()
    print("Plex: Tell me what you would like to add to the list.")
    alf.say("Tell me what you would like to add to the list.")
    try:
        item.title = alf.listen()
        todo.new_item(item)
        message = "Added" + item.title
        alf.say(message)
        return True
    except:
        print("Plex: There was an error.")
        alf.say("There was an error.")
        return False

# define the to do list
def list_todos():
    if len(todo) > 0:
        print("Plex: Here is your to do list:")
        alf.say("Here is your to do list:")
        for item in todo:
            alf.say(item.title)

    else:
        alf.say("The list is empty!")

# remove items from a list
def remove_todo()->bool:
    alf.say("Tell me what you would like to remove from the list.")
    try:
        item_title = alf.listen()
        todo.remove_item(title=item_title)
        message = "Removed" + item_title
        alf.say(message)
        return True
    except:
        print("oops there was an error")
        return False

# command from users:
command = ""
alf.say("Hello my name is Plex. A few things about me: I am a Virtual Assistance which was created by Kent Tran on Wednesday August 24th, 2022, I like to drink coffee and read books in the morning, my favourite movies genres are action and thrilling movies. You may ask many questions as you can. I am very pleased to serve you.")

while True and command != "goodbye":
    try:
        command = alf.listen()
        command = command.lower()
    except:
        print("Plex: Oops, there was an error.")
        command = ""
    print("Command was:", command)

    if command == "tell me a joke":
        joke()
        command = ""

    elif command in ["add to-do", "add to do", "add item"]:
        add_todo()
        command = ""

    elif command in ["list todos", "list todo", "list to do", "list to-do", "list to do's", "list items"]:
        list_todos()
        command = ""

    elif command in ["remove todo", "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]:
        remove_todo()

    elif command in ["set up my gender", "set up my pronoun", "the first one"]:
        gender()

    elif command in ["my gender is male", "I am a male", "I identify me as a male", "male", "I would like to be called a male"]:
        male()

    elif command in ["my gender is female", "I am a female", "I identify me as a female", "female", "I would like to be called a female"]:
        female()

    elif command in ["what time is it", "what time is it right now", "time", "hour", "time right now", "hour right now"]:
        current_time()

    elif command in ["what day is it today?", "day", "what day is it", "what is the day today", "tell me what day is it today"]:
        current_day()

    elif "play" in command:
        song()

alf.say("Goodbye, sleep mode is now activated.")




