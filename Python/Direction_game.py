#Direction game:
locations = {0: "You are sitting on your laptop learning 'Python'",
             1: "You are on a road near a block of building.",
             2: "You are in farm surrounded with yields.",
             3: "You are in home studying programming to land job.",
             4: "You are in Akola to buy some essential.",
             5: "You are on a hill relaxing with your family and enjoying the beautiful view."}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

named_exits = {1: {"2" : 2, "3" : 3, "4" : 4, "5" : 5},
               2: {"5" : 5},
               3: {"1" : 1},
               4: {"1" : 1, "2" : 2},
               5: {"2" : 2, "1" : 1}}

vocabulary = {"QUIT" : "Q",
              "WEST" : "W",
              "EAST" : "E",
              "SOUTH": "S",
              "NORTH": "N",
              "ROAD" :  "1",
              "FARM" :  "2",
              "HOME" :  "3",
              "AKOLA":  "4",
              "HILL" :  "5"}
loc = 1
while True:
    available_dir = ", " .join(exits[loc].keys())
    
    print(locations[loc])
    
    if loc == 0:
        break
    else:
        allexits = exits[loc].copy()
        allexits.update(named_exits[loc])
        print(allexits)
    direction = input("Move to: " + available_dir + " ").upper()
    
    if len(direction)>1:
        for word in vocabulary:
            if word in direction:
                direction = vocabulary[word]
    print()
    if direction in allexits:   #exits[loc].keys() access keys of key 1 in exits.
        loc = allexits[direction]
        print(direction)
    else:
        print("You cannot go in that direction")
