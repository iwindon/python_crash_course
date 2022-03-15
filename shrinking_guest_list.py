from operator import inv

# original list to invite to my dinner party
invites = ["Christina Ricci", "Emma Watson", "Robert Downey Jr."]
print(f"We have {len(invites)} guests invited.")

# using a for loop to invite each person based on the length of the list.
for i in range(0,len(invites)):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

# Sadly Robert is unable to attend, lets invite Chris Evans instead.
unable_attend = invites.pop(2)
print(f"\n{unable_attend.title()}, is unable to attend.")
invites.append("Chris Evans")
print(f"We have {len(invites)} guests invited.")

# now we resend the list to everyone
print("\n")
for i in range(0,len(invites)):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

# I found a larger table, so now I can invite more people.
print("\n")
for i in range(0,len(invites)):
    print(f"{invites[i].title()}, I found a larger table, so I am inviting 3 more people.")

invites.insert(0, "Patrick Stewart")
invites.insert(2, "Bradley Cooper")
invites.append("Samuel L. Jackson")
print(f"We have {len(invites)} guests invited.")

# now we send out the invite to everyone.
print("\n")
for i in range(0,len(invites)):
    print(f"Greetings {invites[i].title()} you are herby invited to my dinner party, please RSVP")

# turns out the table won't arrive in time, supply chain issues.  So we have to remove everyone but two.
print("\n")
for i in range(0,(len(invites)-2)):
    noroom = invites.pop()
    print(f"Sorry {noroom.title()}, however the table won't arrive in time so I must rescind my invite.")

print(f"We have {len(invites)} guests invited.")
    
# send out the invite again to let the two remaining know they are still invited.
print("\n")
for i in range(0,len(invites)):
    print(f"{invites[i].title()}, you are still invited to my dinner party.")

# remove everyone from the list and validate the list is empty.
del invites[0]
del invites[0]
print(f"We have {len(invites)} guests invited.")
print("\n")
print(invites)

