from mcpi.minecraft import Minecraft
mc = Minecraft.create()

sandwich = ["Bread", "Butter", "Tuna", "Lettuce", "Mayonnaise", "Bread"]

for ingredient in sandwich:
    if ingredient == "Mayonnaise":
        print("I don't like mayonnaise on my sandwich.")
        break
    else:
        print(ingredient)
else:
    print("This is the end of the sandwich.")
    
