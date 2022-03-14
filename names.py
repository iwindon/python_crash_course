names = ["Chris", "Justin", "Nathan", "Ethan"]
# what the assignment asked for
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# better way to do it
for i in range(0,4):
    print(names[i].title())

