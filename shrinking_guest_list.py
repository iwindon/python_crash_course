from operator import inv

invites = ["Christina Ricci", "Bach", "Mozart"]

for i in range(0,3):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

unable_attend = invites.pop(2)
print(f"{unable_attend.title()}, is unable to attend.")
invites.append("Beethoven")

for i in range(0,3):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

for i in range(0,3):
    print(f"{invites[i].title()}, I found a larger table, so I am inviting 3 more people.")

invites.insert(0, "Patrick Stewart")
invites.insert(2, "Dave")
invites.append("Mark")

for i in range(0,5):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

for i in range(0,4):
    noroom = invites.pop()
    print(f"Sorry {noroom.title()}, however the table won't arrive in time so I must recend my invite.")
    

for i in range(0,2):
    print(f"{invites[i].title()}, you are still invited to my dinner party.")

del invites[0]
del invites[0]
print(invites)

