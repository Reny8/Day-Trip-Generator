import random
destinations = ["Upstate New York", "Salem, Massachusetts", "Portland, Oregon", "Austin, Texas", "Baltimore, Maryland", "Jim Thorpe, Pennsylvania","Miami, Florida", "Phoenix, Arizona"]
restaurants =["Vetri's Pizza", "Zoe's Kitchen", "Outback Steakhouse", "Olive Garden", "LaScala", "Mod's Pizza","Red Lobster", "The Cheesecake Factory"]
transportations = ["bus", "subway", "Uber", "cab", "rent-a-car", "biking"]
entertainments = ["movie", "concert", "hiking/biking Trail", "sporting event", "comic convention", "comedy club show"]
def display_title():
    print("Welcome to the Day Trip Generator!")
def list_loop(list):
    
    random_pick = random.choice(list)
    user_reply = input(f"How does {random_pick} sound for your? y/n: ").lower()
    if user_reply == "y":
        return random_pick 
    while user_reply == "n":
        if user_reply == "n":
            random_pick = random.choice(list)
            user_reply = input(f"What about {random_pick}? y/n: ").lower()
        if user_reply == "y":
            return random_pick

def complete(dest, rest, trans, entertain):
    satisfied = input("Are you satisfied with all your choices? y/n: ").lower()
    if satisfied == "y":
        print(f"You will enjoy a day trip at {dest} where you will enjoy a meal at {rest}. You will use {trans} to get there. You will enjoy a {entertain}!")
    while satisfied == "n":
        change = input("Type 1 for change destination, 2 for restaurant, 3 for transportation or 4 for entertainment. Press 0 for no more changes: ").lower()
        if change == "1":
            final_destination = list_loop(destinations)
        elif change == "2":
            final_restaurant = list_loop(restaurants)
        elif change == "3":
            final_transportation = list_loop(transportations)
        elif change == "4":
            final_entertainment = list_loop(entertainments)
        else:
            satisfied = input("Are you satisfied with your choices? y/n: ")
            print(f"You will enjoy a day trip at {final_destination} where you will enjoy a meal at {final_restaurant}. You will use {final_transportation} to get there. You will enjoy a {final_entertainment}!")
            return
display_title()
final_destination = list_loop(destinations)
final_restaurant = list_loop(restaurants)
final_transportation = list_loop(transportations)
final_entertainment = list_loop(entertainments)
complete(final_destination,final_restaurant,final_transportation,final_entertainment)

