# Gonna ask the user many questions and make them do a decision. 

# Introcuding
print("Hello,", input("Welcome to this marvelous adventure! Before we start, may I learn your name please?\n"), "!" )

# Entrance speech
print("You find yourself in a dense, shadowy forest. ")
print("The air is thick with the scent of damp earth, and the trees seem to close in around you. ")
print("Ahead, the path splits in two. ")
print("To your left, a narrow trail disappears into a tangle of vines and darkness.")
print("There's an odd stillness here, like the forest itself is holding its breath.")
print("To your right, a wider path winds through the trees, but you hear something unsettling")
print("—a low growl in the distance.")

# First choice 
choiceOne = input("Which do you select? Left or Right? ").lower()

if choiceOne == "left":

    # Explanatory speech
    print("You bravely step into the overgrown path, feeling the cool vines brush against your skin...")
    print("Suddenly, you notice something strange ahead—a faint, glowing light in the distance. It's small, flickering like a candle")
    print("As you approach, you realize it's coming from a small, weathered lantern hanging from a tree branch.")
    print("The lantern swings gently, though there's no wind.")
    print("Will you investigate the lantern, or will you turn back and try another path?")

    # Second choice 
    choiceTwo = input("Yes or No?").lower()


    if choiceTwo == "yes":

        # Texts
        print("You approach the lantern, curiosity outweighing your caution.")
        print("As you crouch down to inspect the freshly disturbed earth beneath it, you notice something half-buried—a small, weathered box.")
        print("You carefully pry it open, revealing a handful of delicate, shimmering stones.")
        print("Before you can examine them further, you hear a soft whisper—barely audible—calling your name from the shadows.")
        print("You look around, but there's no one there.")
        print("Yet, the feeling of being watched grows stronger.")

        # Another choice 
        choiceThree = input("Will you take the stones, yes or no? ").lower()

        if choiceThree == "yes":

            # Text
            print("You decide to take the shimmering stones, placing them carefully in your pocket.")
            print("A figure emerges from the shadows")
            print("Its hand stretches toward the stones, and as it takes them, the light from the stones fades, plunging you into absolute darkness")
            print("you realize that the stones were never meant to be touched.")
            print("You were the final offering.")

            # Ending
            exit()

        elif choiceThree == "no":

            # Text
            print("You decide against touching the stones, a deep sense of foreboding settling over you. ")
            print("You may never know what the stones were for, but your choice to leave them behind has spared you a greater danger.")
            print("With one last glance at the now distant lantern, you walk away,")
            print("the weight of the forest lifting as you step into the open world once more.")
            print("You managed to escape, but the feeling of those unseen eyes watching you never quite leaves.")

            # Ending
            exit()

        else:

            # Text
            print("You stand frozen, unsure whether to investigate the lantern or leave it behind. ")
            print("Before you can move, the vines tighten, pulling you toward the lantern.")
            print("With a final, desperate struggle, you break free—")
            print("a reminder that hesitation in this place comes with a cost.")
            print("You bled to death.")

            # Ending
            exit()


        
    elif choiceTwo == "no":
         # Text
        print("You decide to leave the lantern behind, trusting your instincts.")
        print("As you retrace your steps, the forest begins to shift unnervingly, as though it resents your choice.")
        print("Panic sets in as you quicken your pace, the shadows growing longer around you.")
        print("Just when you think you are lost, you see a break in the trees ahead. ")
        print("You managed to escape, but the feeling of those unseen eyes watching you never quite leaves.")

        # Ending
        exit()


    else:
        # Text
        print("You linger near the lantern, torn between curiosity and caution")
        print("Suddenly, the lanterns light flares brightly, almost blinding you.")
        print("When your vision clears, the lantern is gone, and so is the path beneath your feet.")
        print("The forest has shifted entirely, and now, you are standing in an unfamiliar clearing")
        print("surrounded by towering, twisted trees that werent there before.")
        print("You had your chance to choose, but the forest has made its choice. And now, you belong to it.")

        # Ending
        exit()







elif choiceOne == "right":

    # Text 
    print("You cautiously follow the clearer path, but the growling grows louder with each step...")
    print("You push deeper into the clearing, where the shadows coalesce into a towering figure cloaked in darkness")
    print("Its glowing eyes lock onto yours, and a chilling smile spreads across its face")
    print("\“Welcome, traveler,\” it hisses, “I ve been waiting for you.”")
    print("Before you can turn to flee, the shadows lash out, wrapping around you like chains")
    print("As you re pulled into the suffocating darkness, the sinister laughter echoes in your ears,")
    print("...and you realize too late that you ve become another soul claimed by the evil of the forest.")

    # Exit
    exit()





else:
    # Text 
    print("Confused by the choices, you stand still, unable to make a decision.")
    print("Time seems to stretch, and suddenly, the forest around you grows silent. ")
    print("A voice, calm yet amused, breaks the tension.")
    print("“Ah, a classic case of indecision,” it says, echoing from the shadows.")
    print("“Welcome to the narrative loop! You see, dear player, while your character ponders their fate, you have stalled the story itself.”")
    print("You have realized the ultimate truth. ")

    # Ending
    exit()
