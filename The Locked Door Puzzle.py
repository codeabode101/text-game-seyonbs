has_key = False
user_input = input("look/don't look")
if user_input == "look":
    has_key = True
    hello = input("use key / don't use key ")
    if hello == "use key" and has_key == True:
        print("you unlocked the door!!")
        inventory = "key"
    if has_key == False and hello == "use key":
        print("you don't have key")         
    if inventory == "key":
        print("you are good to go")       