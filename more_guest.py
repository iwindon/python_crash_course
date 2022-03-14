from operator import inv

invites = ["Christina Ricci", "Patrick Stewart", "Mozart"]



for i in range(0,3):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

unable_attend = invites.pop(2)
print(f"{unable_attend.title()}, is unable to attend.")
invites.append("Beethoven")

for i in range(0,3):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

for i in range(0,3):
    print(f"{invites[i].title()}, I found a larger table, so I am inviting 3 more people.")

invites.insert(0, "Bach")
invites.insert(1, "Dave")
invites.append("Mark")

for i in range(0,6):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")


