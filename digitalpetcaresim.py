print("DIGITAL PET CARE SIMULATOR")
print("\n")

pet_name = input("Enter a name for your pet: ")

hunger = 5
happiness = 5
energy = 5
turn = 1
actions = ["Feed", "Play", "Sleep"]
while turn <= 10:
    print()
    print("Turn: ", turn)
    print("Pet: ", pet_name)
    print("Hunger: ", hunger)
    print("Happiness: ", happiness)
    print("Energy: ", energy)
    print("\n")
    
    print("1.", actions[0])
    print("2.", actions[1])
    print("3.", actions[2])
    
    choice = input("Action: ")
    turn = turn + 1
    
    if choice == "1":
        hunger = hunger - 2
        energy = energy + 1
        print(pet_name, " enjoyed the food!")
    
    elif choice == "2":
        happiness = happiness + 2
        energy = energy - 2
        hunger - hunger + 1
        print(pet_name, " had fun!")
    
    elif choice == "3":
        energy = energy + 3
        hunger = hunger + 1
        print(pet_name, " slept like a baby!")
    
    else:
        print("Your pet didn't understand.")

print()
print("FINAL PET REPORT")
print("Pet: ", pet_name)
print("Hunger: ", hunger)
print("Happiness: ", happiness)
print("Energy: ", energy)

if hunger <= 3 and happiness >= 7 and energy >= 5:
    print(pet_name, " is healthy and very happy!")
elif hunger >= 8:
    print(pet_name, " is extremely hungry!")
elif energy <= 2:
    print(pet_name, " is exhausted and needs sleep!")
elif happiness <= 3:
    print(pet_name, "is unhappy and needs attention")
else:
    print(pet_name, "is doing well, but still needs some care")
