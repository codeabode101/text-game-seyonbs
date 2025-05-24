#simple infinite chatbot using while true loops
print("Welcome to the Infinite Chatbot! Type 'exit' to end the conversation.")
while True :
    user_input = input("you:")
    if user_input.lower() in ['exit', 'quit']:
        print("goodbye,have a great day")
        break #exit loop
    else:
        print(f"you said {user_input}.that is interesting.")

#hungry pet simulator starts here                   
hunger = 0
while True : 
    hunger += 1
    if hunger == 10:                  
       print("you lose,you pet ran away.")          
    a = input("feed/add")
    if a == "feed":
       hunger =-2      
       if hunger : 0
       print("you won,your pet is not hungry any more.")
       break

         