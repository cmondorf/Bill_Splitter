# write your code here
import random

num_people = int(input("Enter the number of friends joining (including you):\n"))
if num_people <= 0:
    print("No one is joining for the party")
else:
    i = 0
    friends_list = list()
    print("Enter the name of every friend (including you), each on a new line:")
    while i < num_people:
        friends_list.append(input())
        i += 1
    amount = int(input("Enter the total bill value:\n"))
    game = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if game == "Yes":
        # select and print name
        name = random.choice(friends_list)
        print(f"{name} is the lucky one!")
        friends = dict.fromkeys(friends_list, round(amount / (num_people - 1), 2))
        friends[name] = 0
    else:
        print("No one is going to be lucky")
        friends = dict.fromkeys(friends_list, round(amount / num_people, 2))


    print(friends)

# update the values in the dictionary you have created in the previous stage
# round up the split amount to two decimal places and then update the dictionary with the split values


