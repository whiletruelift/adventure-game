name  = input("Enter your name: ")
print(f"Welcome,{name}, to the Adventure Game!")

should_we_play = input("Do you want to play? (yes/no): ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("Great! Let's start the game.")
    weapon = input("You are in a dark forest. You see a sword and a staff. Which one do you choose? (sword/staff): ").lower()

    direction = input("You are at a crossroad. Where do you want to go? left on the crooked path or right on the smooth road? (left/right): ").lower()
    if direction == "left":
        print("You walk along the crooked path, twist your knee and fall, ending your journey early!")
    elif direction == "right":
        print("You walk along the smooth road, enjoying the beautiful scenery. You see a bridge, do you want to swim under it or cross it? (swim/cross): ")
        action = input().lower()
        if action == "swim" and weapon == "sword":
            print("You try to swim under the bridge, but the sword weighs you down; The current is too strong. You get swept away and die")
            exit()
        if action == "swim" and weapon == "staff":
            print("You swim under the bridge safely and continue your journey. You get to your destination. You won!")
        elif action == "cross":
            print("You cross the bridge safely and continue and get to your destination. You won!")
        else:
            print("Invalid choice. Game Over.")
            exit()
    
    else:
        print("Invalid choice. Game Over.")
        exit()
else:
    print("Maybe next time. Goodbye!")
    exit()
