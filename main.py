import random
destinations = ["Upstate New York", "Salem, Massachusetts", "Portland, Oregon", "Austin, Texas", "Baltimore, Maryland", "Jim Thorpe, Pennsylvania","Miami, Florida", "Phoenix, Arizona"]
def destination_choice():
    random_destination = random.choice(destinations)
    user_dest_reply = input(f"Your destination will be: {random_destination}. Do you like the choice? Type yes or no: ").lower()
    if user_dest_reply == "yes":
        return random_destination
    while user_dest_reply == "no":
        if user_dest_reply == "no":
            random_destination = random.choice(destinations)
            user_dest_reply = input(f"Sorry you didn't like the former destination. What about {random_destination}. ").lower()
        if user_dest_reply == "yes":
            return random_destination

transportations = ["bus", "subway", "Uber", "cab", "rent-a-car", "biking"]
def transportation_choice():
    random_transport = random.choice(transportations)
    user_transport_reply = input(f"When you get there, your transportation method will be by {random_transport}. Do you like the choice? Type yes or no: ").lower()
    if user_transport_reply == "yes":
        return random_transport
    while user_transport_reply == "no":
        if user_transport_reply == "no":
            random_transport = random.choice(transportations)
            user_transport_reply = input(f"Sorry you didn't like the choice of transportation. What about: {random_transport}. ")
        if user_transport_reply == "yes":
            return random_transport

restaurants =["Vetri's Pizza", "Zoe's Kitchen", "Outback Steakhouse", "Olive Garden", "LaScala", "Mod's Pizza","Red Lobster", "The Cheesecake Factory"]
def restaurant_choice():
    random_restaurant = random.choice(restaurants)
    user_rest = input(f"Your restaurant will be: {random_restaurant}. Do you like the choice? Type yes or no: ").lower()
    if user_rest == "yes":
        return random_restaurant 
    while user_rest == "no":
        if user_rest == "no":
            random_restaurant = random.choice(restaurants)
            user_rest = input(f"Sorry you didn't like the former restaurant. What about {random_restaurant}. ").lower()
        if user_rest == "yes":
            return random_restaurant

entertainments = ["movie", "concert", "hiking/biking Trail", "sporting event", "comic convention", "comedy club show"]
def entertainment_choice():
    random_entertain = random.choice(entertainments)
    user_entertain = input(f"Your entertainment will be a {random_entertain}. Do you like the choice? Type yes or no: ").lower()
    if user_entertain == "yes":
        return random_entertain
    while user_entertain == "no":
        if user_entertain == "no":
            random_entertain = random.choice(entertainments)
            user_entertain = input (f"Sorry you didn't like the choice of entertainment. What about: {random_entertain}. ")
        if user_entertain == "yes":
            return random_entertain

def complete(dest,rest,trans,entertain):
    satisfied = input("Are you satisfied with your choices? ").lower()
    if satisfied == "yes":
        print(f"You will enjoy a day trip at {dest} where you will enjoy a meal at {rest}. You will use {trans} to get there. You will enjoy a {entertain}!")
    while satisfied == "no":
        change = input("Type 1 for change destination, 2 for restaurant, 3 for transportation or 4 for entertainment. Press 0 for no more changes: ").lower()
        if change == "1":
            dest = destination_choice()
        elif change == "2":
            rest = restaurant_choice()
        elif change == "3":
            trans = transportation_choice()
        elif change == "4":
            entertain = entertainment_choice() 
        else:
            satisfied = input("Are you satisfied with your choices: ")
            print(f"You will enjoy a day trip at {dest} where you will enjoy a meal at {rest}. You will use {trans} to get there. You will enjoy a {entertain}!")
            return

final_destination = destination_choice()
final_restaurant = restaurant_choice()
final_transportation = transportation_choice()
final_entertainment = entertainment_choice()
complete(final_destination,final_restaurant, final_transportation, final_entertainment)

