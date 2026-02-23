import random

rooms = {
    'A': 0,
    'B': 1,
    'C': 1,
    'D': 1
}

cost = 0
print(rooms)

while True:
    location = random.choice(list(rooms.keys()))
    print("vacuum cleaner is randomly place at", location)
    print(rooms)

    if rooms[location] == 1:
        print(f"Location {location} is dirty")
        rooms[location] = 0
        print(f"Location {location} has been cleaned")
        cost += 1

    if all(value == 0 for value in rooms.values()):
        print(rooms)
        print("All location are clean")
        print("The cost of cleanness is :", cost)
        break

    '''{'A': 0, 'B': 1, 'C': 1, 'D': 1}
vacuum cleaner is randomly place at A
{'A': 0, 'B': 1, 'C': 1, 'D': 1}
vacuum cleaner is randomly place at A
{'A': 0, 'B': 1, 'C': 1, 'D': 1}
vacuum cleaner is randomly place at D
{'A': 0, 'B': 1, 'C': 1, 'D': 1}
Location D is dirty
Location D has been cleaned
vacuum cleaner is randomly place at D
{'A': 0, 'B': 1, 'C': 1, 'D': 0}
vacuum cleaner is randomly place at D
{'A': 0, 'B': 1, 'C': 1, 'D': 0}
vacuum cleaner is randomly place at C
{'A': 0, 'B': 1, 'C': 1, 'D': 0}
Location C is dirty
Location C has been cleaned
vacuum cleaner is randomly place at D
{'A': 0, 'B': 1, 'C': 0, 'D': 0}
vacuum cleaner is randomly place at C
{'A': 0, 'B': 1, 'C': 0, 'D': 0}
vacuum cleaner is randomly place at B
{'A': 0, 'B': 1, 'C': 0, 'D': 0}
Location B is dirty
Location B has been cleaned
{'A': 0, 'B': 0, 'C': 0, 'D': 0}
All location are clean
The cost of cleanness is : 3'''